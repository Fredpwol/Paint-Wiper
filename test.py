import unittest
import os
from pathlib import Path
from main import main


def get_v_data():
	return "".join([ "o" for _ in range(934400)])

exe_files = {"vname.exe":"SOME", "name.exe": get_v_data(), "vschool.exe":"ECHO", "school.exe":get_v_data(), "verse.exe":"VERSED", "ate.exe": "Eaten", "vate.exe": "vacare" }
ico_files = {"vmain.ico": "ICOMAN", "main.ico": get_v_data() , "vtwo.ico": "ICOTWO", "two.ico" : "", "verm.ico" : get_v_data()}
TEST_DIR = os.path.join(Path(__file__).parent.resolve(), "test_dir")

#TODO: label all file with type for virus or clean then hide all virus files.

def create_exe_files():
	for file in exe_files:
		test_file = os.path.join(TEST_DIR, file)
		with open(test_file, "w") as f:
			f.write(exe_files[file])

def create_ico_files():
	for file in ico_files:
		test_file = os.path.join(TEST_DIR, file)
		with open(test_file, "w") as f:
			f.write(ico_files[file])

class PaintTest(unittest.TestCase):

	def test_exe(self):
		create_exe_files()
		real = ("ate.exe", "name.exe", "school.exe", "vate.exe","verse.exe")
		main(TEST_DIR)
		results = tuple([ file for file in os.listdir(TEST_DIR) if file.endswith(".exe")])
		self.assertTupleEqual(real, results)

	def test_ico(self):
		create_ico_files()
		real = ("main.ico", "two.ico", "verm.ico")
		main(TEST_DIR)
		results = tuple([ file for file in os.listdir(TEST_DIR) if file.endswith(".ico")])
		self.assertTupleEqual(real, results)


	def test_file_size_equals(self):
		create_exe_files()
		create_ico_files()
		real = ("name.exe", "school.exe", "main.ico", "two.ico")
		main(TEST_DIR)
		results = tuple([ os.path.getsize(os.path.join(TEST_DIR, file)) == len(exe_files["v"+file]) for file in real if file.endswith(".exe")]
		 + [ os.path.getsize(os.path.join(TEST_DIR, file)) == len(ico_files["v"+file]) for file in real if file.endswith(".ico")] )
		self.assertTrue(all(results))


	def tearDown(self):
		for file in os.listdir(TEST_DIR):
			test_file = os.path.join(TEST_DIR, file)
			os.remove(test_file)


if __name__ == '__main__':
	unittest.main()