import System
import Rhino
import os # We need the 'os' module to handle file paths

def main():
    """
    This is the main function that runs when the 'Mny' command is executed.
    """
    
    # --- DEBUG: Stage 1 - Command Entry ---
    # This will print to the Rhino command history when the command starts.
    print("Mny command script started successfully.")
    
    try:
        # --- DEBUG: Stage 2 - Finding the Script's Own Path ---
        # __file__ is a special Python variable that holds the path to the current script.
        # This is the key to finding our resources reliably.
        script_path = os.path.dirname(os.path.abspath(__file__))
        print(f"DEBUG: This script is running from: {script_path}")
        
        # --- DEBUG: Stage 3 - Constructing the Grasshopper File Path ---
        # Now we build the path to our .gh file relative to this script.
        # The .gh file is in 'resources/', which is in the same directory as this script.
        # So the path is '../lib/resources/Direct_Sunlight_Analysis.gh' relative to the script
        # A more robust way is to go up one level from the script's dir and then down.
        # The script is in /lib. The resource is in /lib/resources.
        gh_file_name = "Direct_Sunlight_Analysis.gh"
        gh_file_path = os.path.join(script_path, "resources", gh_file_name)
        print(f"DEBUG: Attempting to find Grasshopper file at: {gh_file_path}")

        # --- DEBUG: Stage 4 - Verifying the File Exists ---
        # Always check if the file exists before trying to open it.
        if not os.path.exists(gh_file_path):
            print("ERROR: The Grasshopper file was NOT FOUND at the expected path.")
            Rhino.RhinoApp.WriteLine("Mny Error: Could not find the required Grasshopper definition file.")
            return # Stop the script if the file is missing.
            
        print("SUCCESS: Grasshopper file found!")

        # --- DEBUG: Stage 5 - Opening the File in Grasshopper ---
        # We will use Rhino's RunScript command to open the file.
        # The '-' prefix on _GrasshopperOpen suppresses the file dialog.
        # The quotes are crucial for paths that might contain spaces.
        # The _Enter at the end executes the command.
        command_string = f"-_GrasshopperOpen \"{gh_file_path}\" _Enter"
        print(f"DEBUG: Executing Rhino command: {command_string}")
        
        Rhino.RhinoApp.RunScript(command_string, False)
        
        print("Mny command finished.")

    except Exception as e:
        # --- DEBUG: Catch-All for Unexpected Errors ---
        # If anything else goes wrong, this will print the error.
        print(f"An unexpected error occurred: {e}")

# This is the standard entry point for a Rhino Python script.
if __name__ == "__main__":
    main()