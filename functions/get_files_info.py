import os
def get_files_info(working_directory, directory="."):
	try:
		absolut_path = os.path.abspath(working_directory)
		target_dir = os.path.normpath(os.path.join(absolut_path, directory))
		# Will be True or False
		is_valid_target_dir = os.path.commonpath([absolut_path, target_dir]) == absolut_path
		if is_valid_target_dir == False:
			return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
		elif os.path.isdir(target_dir) == False:
			return f'Error: "{directory}" is not a directory'
		liste = []

		for filename in os.listdir(target_dir):
			full_path = os.path.join(target_dir, filename)
			size = os.path.getsize(full_path)
			is_dir = os.path.isdir(full_path)
			entry = f"- {filename}: file_size={size} bytes, is_dir={is_dir}"
			liste.append(entry)
		return "\n".join(liste)
	 
	except Exception as e:
		return f"Error: Error while processing {e}"





