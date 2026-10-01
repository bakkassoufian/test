#!/usr/bin/env bash
# Rebuild every PDF and image for both editions, then package the customer zips.
set -euo pipefail
cd "$(dirname "$0")"

python3 build.py
node render.cjs
python3 build_ar.py
node render.cjs manifest-ar.json

cd ..
python3 - <<'EOF'
import os, zipfile

def package(folder, zip_path):
    if os.path.exists(zip_path):
        os.remove(zip_path)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for name in sorted(os.listdir(folder)):
            if name.endswith(".pdf"):
                # Archive paths are relative to the folder's parent, so the zip unpacks into one named folder.
                z.write(os.path.join(folder, name), os.path.join(os.path.basename(folder), name))
    print("Packaged", zip_path)

package("AI Content Creator Starter Kit", "AI-Content-Creator-Starter-Kit.zip")
package("arabic/حقيبة صانع المحتوى بالذكاء الاصطناعي", "arabic/AI-Content-Creator-Starter-Kit-Arabic.zip")
EOF
