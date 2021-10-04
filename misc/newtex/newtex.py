"""
Create basic TEX template for assignment
"""
import os, sys, shutil, glob
from pathlib import Path

SCRIPT_PATH = Path(os.path.realpath(__file__)).parent
TEMPLATE_PATH = SCRIPT_PATH / "template"

if __name__ == "__main__":
	CWD = Path(os.getcwd())
	NEW_TEX_PATH = CWD / "tex"

	if not NEW_TEX_PATH.exists():
		NEW_TEX_PATH.mkdir()

	# copy all files from template directory into tex dir
	for file in TEMPLATE_PATH.glob('*'):
		print(file)
		shutil.copy(file, NEW_TEX_PATH)


