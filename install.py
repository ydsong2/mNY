"""
install.py – executed once per Rhino session after the package is loaded.
Creates (or updates) the alias “Mny” that runs the packaged Grasshopper file.
"""
import os, traceback
import rhinoscriptsyntax as rs            # AddAlias lives here
import scriptcontext as sc

ALIAS_NAME  = "Mny"
GH_FILENAME = "Direct_Sunlight_Analysis.gh"

def main():
    try:
        print("🟢  mny | install.py starting…")

        # Run only once per Rhino session
        if sc.sticky.get("mny_init"):
            print("🔄  mny | already initialised – skipping")
            return
        sc.sticky["mny_init"] = True
        print("✅  mny | first run in this session")

        # Full path to the .gh inside the installed package
        pkg_dir = os.path.dirname(__file__)
        gh_path = os.path.join(pkg_dir, GH_FILENAME)
        if not os.path.exists(gh_path):
            print(f"❌  mny | {gh_path} not found – aborting")
            return
        print(f"📄  mny | GH file = {gh_path}")

        # Macro that GrasshopperPlayer understands
        macro = f'! _-GrasshopperPlayer "{gh_path}" _Enter'

        # Create / overwrite the alias
        print(f"⚙️   mny | rs.AddAlias('{ALIAS_NAME}', '{macro}')")
        rs.AddAlias(ALIAS_NAME, macro)    # overwrites if it exists  [oai_citation:0‡developer.rhino3d.com](https://developer.rhino3d.com/api/rhinoscript/application_methods/addalias.htm?utm_source=chatgpt.com)

        print("🏁  mny | install.py finished")
    except Exception:
        print("🔥  mny | install.py crashed:")
        traceback.print_exc()

main()