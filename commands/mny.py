# mny.py
import rhinoscriptsyntax as rs
import os
import sys

def run_grasshopper_player():
    """
    Finds and runs the Direct_Sunlight_Analysis.gh file using GrasshopperPlayer.
    """
    try:
        # This script will be installed in a versioned package folder.
        # We need to find the GH file relative to this script's location.
        # e.g., .../packages/mny/0.1.0/commands/mny.py
        # The GH file is at: .../packages/mny/0.1.0/Direct_Sunlight_Analysis.gh
        
        # Get the directory of the currently running script
        script_folder = os.path.dirname(__file__)
        
        # Go up one level to the package root directory
        package_root = os.path.dirname(script_folder)
        
        # Construct the full path to the Grasshopper file
        gh_file = "Direct_Sunlight_Analysis.gh"
        gh_file_path = os.path.join(package_root, gh_file)

        # Check if the file actually exists before trying to run it
        if not os.path.exists(gh_file_path):
            print("Error: Could not find {}.".format(gh_file))
            return

        # Use the -_GrasshopperPlayer command. The hyphen makes it run without dialogs,
        # and the underscore makes it work in any language version of Rhino.
        # The quotes are crucial for paths with spaces.
        command_string = '_-GrasshopperPlayer "{}"'.format(gh_file_path)
        
        rs.Command(command_string, echo=False)

    except Exception as e:
        # Print any errors to the command line for debugging
        print("mny command failed: {}".format(e))

# This is the standard entry point for a Rhino Python script command.
if __name__ == "__main__":
    run_grasshopper_player()