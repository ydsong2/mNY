import Rhino
import scriptcontext as sc

def open_gh_file():
    print("[Mny] open_gh_file called")    # Debug
    gh = Rhino.RhinoApp.GetPlugInObject("Grasshopper")
    if gh is None:
        print("[Mny] Grasshopper not found!")
        return
    print("[Mny] Grasshopper interface found")
    # Get the package location (this script's folder)
    import os
    package_dir = os.path.dirname(__file__)
    gh_file = os.path.join(package_dir, "Direct_Sunlight_Analysis.gh")
    print(f"[Mny] GH File: {gh_file}")
    if not os.path.exists(gh_file):
        print("[Mny] .gh file does not exist!")
        return
    gh.OpenDocument(gh_file)
    print("[Mny] GH file opened")

def RunCommand(is_interactive):
    print("[Mny] RunCommand called")   # Debug
    open_gh_file()
    return 0

# Register command in RhinoPython
if "Mny_command_registered" not in sc.sticky:
    print("[Mny] Registering command...")  # Debug
    import Rhino
    def _cmd():
        RunCommand(True)
    Rhino.RhinoApp.RegisterCommand("Mny", _cmd)
    sc.sticky["Mny_command_registered"] = True
    print("[Mny] Command registered!")
else:
    print("[Mny] Command already registered.")