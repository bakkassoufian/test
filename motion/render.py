"""Motion graphic 8 s, 9:16, 1080x1920 @30 fps, built from the original splash image.

The source image is never redrawn: every effect is a subtle warp, a light
overlay or a camera move on top of the untouched pixels.
"""
import math
import os
import subprocess
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
import imageio_ffmpeg

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS, DUR = 1080, 1920, 30, 8.0
N = int(FPS * DUR)
SRC = Image.open(os.path.join(HERE, "splash.png")).convert("RGB")
S = W / SRC.width  # source (941x1672) -> render space
BASE = np.asarray(SRC.resize((W, H), Image.LANCZOS).filter(ImageFilter.UnsharpMask(1.2, 60, 2)), dtype=np.float32)
YY, XX = np.mgrid[0:H, 0:W].astype(np.float32)


def p(v):
    return v * S


# ---------- easing helpers ----------
def smooth(a, b, t):
    if t <= a:
        return 0.0
    if t >= b:
        return 1.0
    x = (t - a) / (b - a)
    return x * x * (3 - 2 * x)


def bell(a, b, t):
    """0 -> 1 -> 0 between a and b (smooth)."""
    if t <= a or t >= b:
        return 0.0
    return math.sin(math.pi * (t - a) / (b - a)) ** 2


# ---------- masks (render space) ----------
def ellipse_mask(cx, cy, rx, ry, feather=0.35):
    d = np.sqrt(((XX - p(cx)) / p(rx)) ** 2 + ((YY - p(cy)) / p(ry)) ** 2)
    return np.clip((1 - d) / feather, 0, 1).astype(np.float32)


def box_mask(x0, y0, x1, y1, feather=40):
    f = p(feather)
    mx = np.clip(np.minimum(XX - p(x0), p(x1) - XX) / f, 0, 1)
    my = np.clip(np.minimum(YY - p(y0), p(y1) - YY) / f, 0, 1)
    return (mx * my).astype(np.float32)


LION = ellipse_mask(470, 860, 330, 330)
LOGO_ZONE = ellipse_mask(470, 310, 300, 210)
BREEZE = [  # (mask, amplitude px, frequency Hz, phase, spatial freq)
    (box_mask(0, 0, 190, 520, 50) * np.clip(1 - XX / p(190), 0.2, 1), 3.0, 0.45, 0.0, 0.020),
    (box_mask(810, 450, 941, 740, 40), 2.6, 0.38, 1.3, 0.030),
    (box_mask(780, 760, 941, 1010, 40), 2.2, 0.42, 2.1, 0.025),
    (box_mask(0, 640, 170, 860, 40), 2.0, 0.40, 0.7, 0.030),
    (box_mask(0, 1180, 230, 1672, 60), 3.2, 0.33, 2.8, 0.018),
    (box_mask(760, 1420, 941, 1672, 50), 3.0, 0.36, 4.0, 0.018),
    (box_mask(820, 0, 941, 200, 40), 1.8, 0.40, 3.3, 0.030),
]
MANE = ellipse_mask(470, 740, 250, 200) * (1 - ellipse_mask(480, 730, 150, 120, 0.5))

# logo mask: everything inside the logo zone that is not sky blue
arr = np.asarray(SRC, dtype=np.int32)
sky = (arr[..., 2] > arr[..., 0] + 35) & (arr[..., 2] > 140)
logo_src = np.zeros(sky.shape, np.uint8)
logo_src[125:495, 190:760] = (~sky[125:495, 190:760]) * 255
LOGO_MASK = np.asarray(Image.fromarray(logo_src).resize((W, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(3)), np.float32) / 255
BOOK_POLY = [(548, 1043), (628, 838), (755, 902), (690, 1093)]
bm = Image.new("L", (W, H), 0)
ImageDraw.Draw(bm).polygon([(p(x), p(y)) for x, y in BOOK_POLY], fill=255)
BOOK_MASK = np.asarray(bm.filter(ImageFilter.GaussianBlur(4)), np.float32) / 255

# button (pill) crop for the pulse
BX0, BY0, BX1, BY1 = p(160), p(1148), p(785), p(1310)
BTN_BOX = tuple(int(round(v)) for v in (BX0, BY0, BX1, BY1))
bw, bh = BTN_BOX[2] - BTN_BOX[0], BTN_BOX[3] - BTN_BOX[1]
pill = Image.new("L", (bw * 4, bh * 4), 0)
ImageDraw.Draw(pill).rounded_rectangle((6, 6, bw * 4 - 6, bh * 4 - 6), radius=bh * 2 - 6, fill=255)
PILL = pill.resize((bw, bh), Image.LANCZOS)

# eyes for the blink (source coords: centre, rx, ry, eyelid colour sample point)
EYES = [((441, 729), 31, 27), ((552, 709), 27, 27)]


def sample_color(x, y):
    return tuple(int(v) for v in arr[y - 3:y + 3, x - 3:x + 3].reshape(-1, 3).mean(0))




rng = np.random.default_rng(7)
PARTICLES = []
PAL = [(253, 185, 19), (229, 21, 122), (47, 181, 200), (245, 126, 32), (14, 122, 78), (123, 63, 160), (255, 255, 255)]
for i in range(16):
    ang = rng.uniform(0, 2 * math.pi)
    rad = rng.uniform(250, 360)
    PARTICLES.append(dict(
        x=470 + math.cos(ang) * rad, y=320 + math.sin(ang) * rad * 0.7,
        size=rng.uniform(7, 13), col=PAL[i % len(PAL)], kind=i % 3,
        vy=rng.uniform(6, 14), sway=rng.uniform(4, 10), ph=rng.uniform(0, 6.28),
        rot=rng.uniform(0, 360), vr=rng.uniform(-25, 25)))


def star_pts(cx, cy, R, r, n=8, rot=0.0):
    pts = []
    for i in range(2 * n):
        a = math.pi * i / n - math.pi / 2 + rot
        rr = R if i % 2 == 0 else r
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return pts


def remap(img, sx, sy):
    x0 = np.clip(np.floor(sx).astype(np.int32), 0, W - 2)
    y0 = np.clip(np.floor(sy).astype(np.int32), 0, H - 2)
    fx = np.clip(sx - x0, 0, 1)[..., None]
    fy = np.clip(sy - y0, 0, 1)[..., None]
    a = img[y0, x0]; b = img[y0, x0 + 1]; c = img[y0 + 1, x0]; d = img[y0 + 1, x0 + 1]
    return (a * (1 - fx) + b * fx) * (1 - fy) + (c * (1 - fx) + d * fx) * fy


def glow(cx, cy, r, color, strength):
    g = np.exp(-(((XX - cx) ** 2 + (YY - cy) ** 2) / (2 * r * r)))
    return g[..., None] * np.array(color, np.float32)[None, None] * strength


def frame(t):
    # ---- 1. subtle warps: breeze, breathing, welcome, parallax ----
    dx = np.zeros((H, W), np.float32)
    dy = np.zeros((H, W), np.float32)
    breeze_in = 0.35 + 0.65 * smooth(1.6, 2.6, t)
    for m, amp, f, ph, k in BREEZE:
        dx += m * p(amp) * breeze_in * np.sin(2 * math.pi * f * t + ph + YY * k / S)
        dy += m * p(amp) * 0.35 * breeze_in * np.cos(2 * math.pi * f * t + ph + XX * k / S)
    breath = 0.0065 * math.sin(2 * math.pi * t / 2.7)
    dy += LION * (YY - p(1150)) * breath  # grows upward from the table
    dx += MANE * p(1.2) * smooth(1.8, 2.8, t) * np.sin(2 * math.pi * 0.5 * t + YY / p(40))
    welcome = 0.022 * bell(4.0, 6.0, t)
    dx += -LION * (XX - p(400)) * welcome
    dy += -LION * (YY - p(900)) * welcome
    par = smooth(0.0, 6.0, t) - smooth(6.0, 7.6, t)  # parallax follows the push-in
    dx += -LION * (XX - p(470)) * 0.014 * par
    dy += -LION * (YY - p(860)) * 0.014 * par
    dx += -LOGO_ZONE * (XX - p(470)) * 0.008 * par
    dy += -LOGO_ZONE * (YY - p(310)) * 0.008 * par
    img = remap(BASE, XX + dx, YY + dy)

    # ---- 2. light: lanterns, book glint, logo sweep ----
    fl = 0.75 + 0.25 * (0.6 * math.sin(t * 13.1) + 0.3 * math.sin(t * 7.3 + 1) + 0.1 * math.sin(t * 29.0))
    on = 0.55 + 0.45 * smooth(1.8, 2.6, t)
    img += glow(p(80), p(305), p(55), (255, 170, 60), 0.30 * fl * on)
    img += glow(p(848), p(355), p(55), (255, 170, 60), 0.30 * (1.55 - fl) * on)

    def sweep(mask, a, b, width, strength, angle=0.9):
        k = smooth(a, b, t)
        if k <= 0 or k >= 1:
            return
        proj = XX * math.cos(angle) + YY * math.sin(angle)
        lo, hi = float(proj[mask > 0.05].min()), float(proj[mask > 0.05].max())
        c = lo - width + (hi - lo + 2 * width) * k
        band = np.exp(-((proj - c) ** 2) / (2 * width * width))
        img[:] += (band * mask)[..., None] * 255 * strength

    sweep(BOOK_MASK, 4.0, 5.4, p(28), 0.55)
    sweep(LOGO_MASK, 4.6, 5.9, p(45), 0.28, angle=0.7)

    # ---- 3. blink (once, ~1.3 s): curved fur-coloured eyelids ----
    blink = bell(1.15, 1.5, t)
    if blink > 0.02:
        for (ex, ey), rx, ry in EYES:
            cx, cy, RX, RY = p(ex), p(ey), p(rx + 3), p(ry + 3)
            x0, x1 = int(cx - RX - 4), int(cx + RX + 5)
            y0, y1 = int(cy - RY - 4), int(cy + RY + 5)
            xs = XX[y0:y1, x0:x1]; ys = YY[y0:y1, x0:x1]
            u = np.clip((xs - cx) / RX, -1, 1)
            inside = np.clip((1 - np.sqrt(((xs - cx) / RX) ** 2 + ((ys - cy) / RY) ** 2)) / 0.16, 0, 1)
            edge = (cy - RY) + 1.5 * RY * blink * (0.55 + 0.45 * np.sqrt(1 - u * u))
            lid = np.clip((edge - ys) / 1.5, 0, 1) * inside
            # colour of each lid column = fur just above that column of the eye
            row = img[int(cy - RY - p(5)):int(cy - RY - p(2)), x0:x1].mean(0)
            k = np.ones(int(p(9))) / int(p(9))
            top_row = np.stack([np.convolve(np.pad(row[:, c], (len(k) // 2, len(k) - 1 - len(k) // 2), mode='edge'), k, mode='valid') for c in range(3)], -1)[None, :, :]
            shade = 1 - 0.18 * np.clip((ys - (cy - RY)) / (2 * RY), 0, 1)[..., None]
            col = top_row * shade
            region = img[y0:y1, x0:x1]
            region[:] = region * (1 - lid[..., None]) + col * lid[..., None]
            lash = np.exp(-((ys - edge) ** 2) / (2 * p(1.4) ** 2)) * inside * min(1.0, blink * 1.6)
            region[:] = region * (1 - 0.85 * lash[..., None]) + np.array([80, 38, 16], np.float32) * 0.85 * lash[..., None]

    out = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))

    # ---- 4. mint-tea steam + floating zellige particles ----
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    st = 0.4 + 0.6 * smooth(1.8, 2.8, t)
    for j in range(3):
        for s in range(26):
            u = ((s / 26) + t * 0.22 + j * 0.33) % 1.0
            y = 1072 - u * 140
            x = 790 + j * 9 + math.sin(u * 7 + t * 1.6 + j) * (5 + 16 * u)
            a = int(70 * st * math.sin(math.pi * u) ** 1.5)
            r = 5 + 11 * u
            ld.ellipse((p(x - r), p(y - r), p(x + r), p(y + r)), fill=(255, 255, 255, a))
    layer = layer.filter(ImageFilter.GaussianBlur(p(5)))
    ld = ImageDraw.Draw(layer)
    pa = smooth(2.0, 3.2, t) * (1 - 0.35 * smooth(7.5, 8.0, t))
    for q in PARTICLES:
        x = q["x"] + math.sin(t * 0.9 + q["ph"]) * q["sway"]
        y = q["y"] - q["vy"] * (t - 2.0)
        rot = math.radians(q["rot"] + q["vr"] * t)
        sz, (cr, cg, cb) = q["size"], q["col"]
        a = int(230 * pa)
        if a <= 0:
            continue
        cx, cy = p(x), p(y)
        if q["kind"] == 0:
            pts = star_pts(cx, cy, p(sz), p(sz * 0.62), 8, rot)
        elif q["kind"] == 1:
            pts = [(cx + p(sz) * math.cos(rot + k * math.pi / 2), cy + p(sz) * math.sin(rot + k * math.pi / 2)) for k in range(4)]
        else:
            pts = [(cx + p(sz) * math.cos(rot + k * 2 * math.pi / 3), cy + p(sz) * math.sin(rot + k * 2 * math.pi / 3)) for k in range(3)]
        ld.polygon(pts, fill=(cr, cg, cb, a))
    out = Image.alpha_composite(out.convert("RGBA"), layer)

    # ---- 5. "Jouer" pulse (6 - 7.5 s) ----
    pulse = bell(6.0, 7.5, t)
    if pulse > 0.002:
        gl = Image.new("L", (W, H), 0)
        ImageDraw.Draw(gl).rounded_rectangle(BTN_BOX, radius=bh // 2, fill=255)
        gl = gl.filter(ImageFilter.GaussianBlur(p(22)))
        gold = Image.new("RGBA", (W, H), (255, 214, 90, 0))
        gold.putalpha(gl.point(lambda v: int(v * 0.85 * pulse)))
        out = Image.alpha_composite(out, gold)
        sc = 1 + 0.055 * pulse
        crop = Image.fromarray(np.asarray(BASE[BTN_BOX[1]:BTN_BOX[3], BTN_BOX[0]:BTN_BOX[2]]).astype(np.uint8)).convert("RGBA")
        crop.putalpha(PILL)
        nw, nh = int(bw * sc), int(bh * sc)
        crop = crop.resize((nw, nh), Image.LANCZOS)
        cx, cy = (BTN_BOX[0] + BTN_BOX[2]) / 2, (BTN_BOX[1] + BTN_BOX[3]) / 2
        out.alpha_composite(crop, (int(cx - nw / 2), int(cy - nh / 2)))
    out = out.convert("RGB")

    # ---- 6. camera: slow push-in, settle back on the full screen ----
    z = 1 + 0.075 * (smooth(0.0, 6.0, t) - smooth(6.3, 7.8, t))
    fx, fy = p(470), p(820)
    cw, ch = W / z, H / z
    x0 = min(max(fx - cw * fx / W, 0), W - cw)
    y0 = min(max(fy - ch * fy / H, 0), H - ch)
    return out.transform((W, H), Image.EXTENT, (x0, y0, x0 + cw, y0 + ch), Image.BICUBIC)


def main():
    out_mp4 = os.path.join(HERE, "1001-questions-motion.mp4")
    only = [float(a) for a in sys.argv[1:]]
    if only:  # preview stills
        for t in only:
            frame(t).save(os.path.join(HERE, f"preview_{t:.2f}.png"))
        return
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    proc = subprocess.Popen([ff, "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                             "-c:v", "libx264", "-preset", "slow", "-crf", "16", "-pix_fmt", "yuv420p", "-movflags", "+faststart", out_mp4],
                            stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    for i in range(N):
        proc.stdin.write(frame(i / FPS).tobytes())
        if i % 30 == 0:
            print("frame", i, flush=True)
    proc.stdin.close()
    proc.wait()
    print("done", out_mp4)


if __name__ == "__main__":
    main()
