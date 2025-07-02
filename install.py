"""
Runs once, right after the package is first loaded.
Creates the Rhino alias  mny  →  opens your GH definition.
"""
import os
import Rhino
import scriptcontext as sc

# ── guard: only run once per Rhino session ───────────────────────────
if sc.sticky.get(__name__):
    raise SystemExit
sc.sticky[__name__] = True
# ---------------------------------------------------------------------

# Absolute path of the .gh file inside this package
package_dir = os.path.dirname(__file__)
gh_path      = os.path.join(package_dir, "Direct_Sunlight_Analysis.gh")

# Alias macro that Rhino will execute
macro = f'-_GrasshopperOpenDocument "{gh_path}" _Enter'

alias_name = "Mny"
aliases    = Rhino.ApplicationSettings.CommandAliasList

# Create the alias only if it does not yet exist
if not aliases.IsAlias(alias_name):          # ✔ proved by Rhino docs 
    aliases.AddAlias(alias_name, macro)      # AddAlias is part of CommandAliasList 