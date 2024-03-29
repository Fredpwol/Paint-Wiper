import os
import sys
from tqdm import tqdm


def main(dir_path):
	os.chdir(dir_path)
	os.system("attrib -s -h /s /d")
	nom_exe = {} # holds normal exe and potential viruses
	v_exe = {} # holds files that starts with v and original files of corrupted files.
	for path, _, files in tqdm(list(os.walk(dir_path)), desc="Scanning"):
		for file in files:
			if file.endswith(".exe") or file.endswith(".ico") :
				if (file.startswith("v")):
					v_exe[file] = os.path.join(path, file)
				else:
					nom_exe[file] = os.path.join(path, file)
	count = 0
	for file in tqdm(list(v_exe), desc="Fixing"):
		if file[1: ] in nom_exe and (os.path.getsize(nom_exe[file[1:]]) in [0, 934400, 299008]):
			os.remove(nom_exe[file[1:]])
			os.rename(v_exe[file], nom_exe[file[1:]])
			count += 1
	print('Done Fixed (%d) files.'%count)


if __name__ == '__main__':
	dir_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
	main(dir_path)