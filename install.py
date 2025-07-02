# install.py  – runs the first time Rhino loads the package
import importlib.resources as pkg
import Rhino
import Grasshopper as gh
import scriptcontext

# Prevent re-import on every Rhino launch -----------------------------
if scriptcontext.sticky.get(__name__):     # already ran once
    raise SystemExit
scriptcontext.sticky[__name__] = True
# ---------------------------------------------------------------------

# 1  register the display mode
ini_path = pkg.files(__package__) / "MyDisplay.ini"
Rhino.Display.DisplayModeDescription.ImportFromFile(str(ini_path))   # https://developer.rhino3d.com/api/rhinocommon/rhino.display.displaymodedescription

# 2  open the GH tutorial (only if it’s not already open)
gh_path = pkg.files(__package__) / "Direct_Sunlight_Analysis.gh"
if gh.Instances.DocumentServer.FindDocument(str(gh_path)) is None:
    gh.Instances.DocumentEditorEnabled = True
    gh.Instances.DocumentServer.Open(str(gh_path))