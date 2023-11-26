import os
import subprocess
import requests

def execute_instruction(instruction):
    parts = instruction.split()

    # Check if there are enough elements in the list
    if len(parts) == 0:
        return

    command = parts[0].upper()

    if command == 'CREATE' and len(parts) >= 3:
        if parts[1] == 'FOLDER':
            folder_name = parts[2]
            os.makedirs(folder_name, exist_ok=True)
        elif parts[1] == 'FILE':
            file_name = parts[2]
            with open(file_name, 'w'):
                pass  # Create an empty file

    elif command == 'RUN' and len(parts) >= 4:
        program = parts[2]
        arguments = parts[3:]
        subprocess.run([program] + arguments)

    elif command == 'PRINT' and len(parts) >= 2:
        message = ' '.join(parts[1:])
        print(message)

    elif command == 'DOWNLOAD' and len(parts) == 4:
        url = parts[1]
        output_file = parts[3]

        try:
            response = requests.get(url)
            with open(output_file, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded {url} to {output_file} successfully.")
        except Exception as e:
            print(f"Error downloading {url}: {str(e)}")

# Read instructions from the script file
script_file = 'test.instruction'
with open(script_file, 'r') as file:
    instructions = file.readlines()

# Execute each instruction
for instruction in instructions:
    execute_instruction(instruction.strip())