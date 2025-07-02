# install.py – runs the first time the package is loaded by Rhino

# Use the 'os' library for reliable path manipulation
import os
import Rhino
import Grasshopper as gh
import scriptcontext

# --- Don't run this script more than once per Rhino session ---
# This part is good, let's keep it.
if "mNY_install_complete" in scriptcontext.sticky:
    raise SystemExit
# ---

print("mNY package: Running install script...") # Add a print statement for debugging!

# Get the directory where this install.py script is located
# This is the most reliable way to find your other package files.
package_dir = os.path.dirname(os.path.realpath(__file__))


# --- 1. Register the display modes ---
# Construct the full path to each .ini file and import it.
try:
    display_modes_dir = os.path.join(package_dir, "display_modes")
    
    # Import Line Drawing
    line_drawing_ini = os.path.join(display_modes_dir, "Line Drawing.ini")
    if os.path.exists(line_drawing_ini):
        Rhino.Display.DisplayModeDescription.ImportFromFile(line_drawing_ini)
        print("  - Imported 'Line Drawing.ini'")
    else:
        print("  - WARNING: 'Line Drawing.ini' not found.")

    # Import Transparent
    transparent_ini = os.path.join(display_modes_dir, "Transparent.ini")
    if os.path.exists(transparent_ini):
        Rhino.Display.DisplayModeDescription.ImportFromFile(transparent_ini)
        print("  - Imported 'Transparent.ini'")
    else:
        print("  - WARNING: 'Transparent.ini' not found.")
except Exception as e:
    print(f"  - ERROR importing display modes: {e}")


# --- 2. Open the Grasshopper tutorial file ---
try:
    gh_path = os.path.join(package_dir, "Direct_Sunlight_Analysis.gh")
    
    # Check if the file exists before trying to open it
    if os.path.exists(gh_path):
        # Check if a document with the same path is already open
        if gh.Instances.DocumentServer.FindDocument(gh_path) is None:
            gh.Instances.DocumentEditorEnabled = True
            gh.Instances.DocumentServer.Open(gh_path)
            print("  - Opened 'Direct_Sunlight_Analysis.gh'")
    else:
        print("  - WARNING: 'Direct_Sunlight_Analysis.gh' not found.")
except Exception as e:
    print(f"  - ERROR opening Grasshopper file: {e}")


# --- Mark the installation as complete for this session ---
scriptcontext.sticky["mNY_install_complete"] = True
print("mNY package: Install script finished.")