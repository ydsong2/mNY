import os
import sys

pkg_dir = os.path.dirname(__file__)
mny_script = os.path.join(pkg_dir, "Mny.py")

print("[Mny] Running install.py")
if os.path.exists(mny_script):
    print("[Mny] Loading Mny.py")
    exec(open(mny_script).read())
else:
    print("[Mny] Mny.py not found")