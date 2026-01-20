import os
def write_file(working_directory, file_path, content):
	try:
		absolut_path = os.path.abspath(working_directory)
		target_dir = os.path.normpath(os.path.join(absolut_path, file_path))
		# Will be True or False
		is_valid_target_dir = os.path.commonpath([absolut_path, target_dir]) == absolut_path
		if is_valid_target_dir == False:
			return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
		elif os.path.isdir(target_dir) == True:
			return f'Error: Cannot write to "{file_path}" as it is a directory'
		dir_name = os.path.dirname(target_dir)
		if dir_name:
			os.makedirs(dir_name, exist_ok=True)
		with open(target_dir, "w") as f:
			f.write(content)
			return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
	 
	except Exception as e:
		return f"Error: Error while processing {e}"