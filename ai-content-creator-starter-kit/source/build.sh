#!/usr/bin/env bash
# Rebuild every PDF and image, then package the customer zip.
set -euo pipefail
cd "$(dirname "$0")"

python3 build.py
node render.cjs

cd ..
rm -f AI-Content-Creator-Starter-Kit.zip
python3 - <<'EOF'
import os, zipfile
folder = "AI Content Creator Starter Kit"
with zipfile.ZipFile("AI-Content-Creator-Starter-Kit.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for name in sorted(os.listdir(folder)):
        if name.endswith(".pdf"):
            z.write(os.path.join(folder, name), os.path.join(folder, name))
print("Packaged AI-Content-Creator-Starter-Kit.zip")
EOF
