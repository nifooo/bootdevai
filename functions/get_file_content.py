def get_file_content(working_directory, file_path):
	try:
		absolut_path = os.path.abspath(working_directory)
		target_dir = os.path.normpath(os.path.join(absolut_path, file_path))
		# Will be True or False
		is_valid_target_dir = os.path.commonpath([absolut_path, target_dir]) == absolut_path
		if is_valid_target_dir == False:
			return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
		elif os.path.isfile(target_dir) == False:
			return f'Error: File not found or is not a regular file: "{file_path}"'
        
        MAX_CHARS = 10000
        with open(file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
			
            # After reading the first MAX_CHARS...
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
	 
	except Exception as e:
	    return f"Error: Error while processing {e}"
