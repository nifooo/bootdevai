import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    
    try:
        absolut_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolut_path, file_path))
		# Will be True or False
        is_valid_target_dir = os.path.commonpath([absolut_path, target_dir]) == absolut_path
        if is_valid_target_dir == False:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif os.path.isdir(target_dir) == False and os.path.isfile(target_dir) == False:
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif target_dir.endswith(".py") == False:
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_dir]
        if args is not None:
            command.extend(args)

        result = subprocess.run(command, capture_output=True, text=True, timeout=30)

        if result.returncode != 0:
            return f'Process exited with code "{result.returncode}"'
        elif result.stdout == None or result.stderr == None:
            return f'No output produced'
        else:
            return f'STDOUT: {result.stdout} and STDERR: 3{result.stderr}'
    except Exception as e:
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs certain python functions",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory python function from, relative to the working directory (default is the working directory itself)",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Argument to run the python function",
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Single Argument as string")
            ),
        },
    ),
)
