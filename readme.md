# preInstall Instruction Language Documentation

## Introduction

Welcome to the README.MD for the preInstall Instruction Language or PIIL, a simple scripting language crafted to provide instructions to the preInstall Python script to install programs silently or passively.

## ONLY WINDOWS SUPPORT

## Table of Contents

1. [Syntax](#syntax)
2. [Commands](#commands)
    - [CREATE](#create)
    - [RUN](#run)
    - [PRINT](#print)
3. [Example Script](#example-script)
4. [Interpreter](#interpreter)
5. [Usage](#usage)
6. [Contributing](#contributing)
7. [License](#license)

## Syntax

The syntax of the preInstall Instruction Language is designed to be simple and human-readable. Each instruction is written on a new line and may include comments preceded by the `#` symbol.

example below:
```plaintext
# THIS IS A COMMENT

CREATE FOLDER folder_name
```

## Commands

### CREATE

The `CREATE` command is used to create folders or files.

- To create a folder: `CREATE FOLDER folder_name`
- To create a file: `CREATE FILE file_path`

### RUN

The `RUN` command is used to execute programs (often the installers).

- To run a program: `RUN PROGRAM program_name.exe arguments`

### PRINT

The `PRINT` command is used to display messages.

- To print a message: `PRINT "your message"`

## Example Script

```plaintext
# Sample instruction script

CREATE FOLDER output
CREATE FILE output/data.txt
RUN PROGRAM exeFile
PRINT "Instructions completed successfully!"
```

## Usage

1. Create a script using the syntax described in this documentation.
2. Save the script with a `.instruction` file extension (e.g., `example.instruction`).
3. Run the Python interpreter script: `python instruction_interpreter.py your_script.instruction`.
or use preInstall which contains the interpreter

## Contributing

If you have ideas for improvements or new features, feel free to contribute! Fork the repository, make your changes, and submit a pull request.

## License

This preInstall Instruction Language and its interpreter are open-source projects released under the [MIT](https://choosealicense.com/licenses/mit/)
>>>>>>> Stashed changes
