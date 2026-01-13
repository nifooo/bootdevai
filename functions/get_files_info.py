import os
def get_files_info(working_directory, directory="."):

	absolut_path = os.path.abspath(working_directory)
	target_dir = os.path.normpath(os.path.join(absolut_path, directory))
	# Will be True or False
	valid_target_dir = os.path.commonpath([absolut_path, target_dir]) == absolut_path
	if valid_target_dir == False:
		f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
	elif os.path.isdir(directory) == False:
		f'Error: "{directory}" is not a directory'

	for item in os.listdir(valid_target_dir):
		print(item.name)
		print (os.path.getsize(item))
		print(os.path.isdir(item))




