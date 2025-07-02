# install.py  – runs the first time Rhino loads the package
import importlib.resources as pkg
import Grasshopper as gh
import Rhino
import scriptcontext

# Prevent re-import on every Rhino launch -----------------------------
if scriptcontext.sticky.get(__name__):     # already ran once
    raise SystemExit
scriptcontext.sticky[__name__] = True
# ---------------------------------------------------------------------

# 1)  import every .ini inside the display_modes folder
mode_dir = pkg.files(__package__) / "display_modes"
for ini in mode_dir.iterdir():
    if ini.suffix.lower() == ".ini":
        Rhino.Display.DisplayModeDescription.ImportFromFile(str(ini))

# 2)  open the tutorial GH document (only if not open already)
gh_path = pkg.files(__package__) / "Direct_Sunlight_Analysis.gh"
if gh.Instances.DocumentServer.FindDocument(str(gh_path)) is None:
    gh.Instances.DocumentEditorEnabled = True
    gh.Instances.DocumentServer.Open(str(gh_path))