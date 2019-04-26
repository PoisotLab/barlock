import subprocess
import json

with open(".zenodo.json", 'r') as f:
    zenodo = json.load(f)

print(zenodo)

root = [
    "pandoc",
    "manuscript.md"
]

common_flags = [
    "--filter", "pandoc-fignos",
    "--filter", "pandoc-eqnos",
    "--filter", "pandoc-tablenos",
    "--filter", "pandoc-citeproc",
    "--bibliography", "references.json"
]

# Version for the website
subprocess.run(root + ["-o", "index.md", "--template", "templates/index.md"] + common_flags)
subprocess.run(["cat", "index.md"])
