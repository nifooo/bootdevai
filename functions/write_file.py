import os
from google.genai import types

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

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content into a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file path": types.Schema(
                type=types.Type.STRING,
                description="File path to write content to, relative to the working directory (default is the working directory itself)",
            ),
			"file content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to a file.",
            ),
        },
    ),
)