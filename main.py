import os
import sys


dir_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()

os.system("attrib -s -h /s /d")
nom_exe = {}
v_exe = {} 
for path, _, files in os.walk(dir_path):
	for file in files:
		if file.endswith(".exe") or file.endswith(".ico") :
			if file.startswith("v"):
				v_exe[file] = os.path.join(path, file)
			else:
				nom_exe[file] = os.path.join(path, file)

for file in v_exe:
	if file[1: ] in nom_exe:
		os.remove(nom_exe[file[1:]])
		os.rename(v_exe[file], nom_exe[file[1:]])