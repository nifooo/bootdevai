import os
import subprocess

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
        command.extend([args1, args2])

        result = subprocess.run(
            [command],  
            capture_output=True,          # stdout/stderr einfangen
            text=True                     # Ausgabe als String
            timeout=30
        )

        if result.returncode != 0:
            return f'Process exited with code "{result.returncode}"'
        elif result.stdout == None or result.stderr == None:
            return f'No output produced'
        else:
            return f'STDOUT{result.stdout} and STDERR:{result.stderr}'
    except Exception as e:
        return f"Error: executing Python file: {e}"
