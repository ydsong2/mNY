"""
Runs once per Rhino session after the package is loaded.
Creates/updates a Rhino alias called `Mny`
so the user can simply type `Mny` to open the GH file.
"""

import os
import scriptcontext as sc
import rhinoscriptsyntax as rs

# ---------- DEBUG OUTPUT ----------
print("🟢 Mny install.py starting")

# Prevent re-import every time Rhino loads another plug-in
if sc.sticky.get("Mny_Initialized"):
    print("🔄 Mny already initialized this session – skipping")
    raise SystemExit
sc.sticky["Mny_Initialized"] = True
print("✅ First run in this session")

# ---------- PATH TO THE .GH FILE ----------
pkg_dir = os.path.dirname(__file__)
gh_path = os.path.join(pkg_dir, "Direct_Sunlight_Analysis.gh")
print(f"📄 Grasshopper file resolved to:\n    {gh_path}")

# ---------- BUILD THE MACRO ----------
#  _GrasshopperOpenDocument is a built-in Rhino command.
macro_body = f'! _-GrasshopperOpenDocument "{gh_path}" _Enter'
alias_name = "Mny"

# ---------- CREATE / UPDATE ALIAS ----------
print(f"⚙️  Setting alias {alias_name!r} → {macro_body!r}")
rs.AddAlias(alias_name, macro_body)          # overwrites if it already exists

print("🏁 Mny install.py finished")