import zipfile
import os

def unzip(path_to_zip_file, output_dir):
	zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
	zip_ref.extractall(output_dir)
	zip_ref.close()
	os.remove(path_to_zip_file)