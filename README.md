# Logger Script - Executable Version

This project contains a Python-based logger script that has been compiled into a standalone executable using **PyInstaller**. The executable allows the logger script to run on any Windows machine without the need for Python or external dependencies to be installed.

## Compilation Process

We used **PyInstaller** to compile the Python script into an `.exe` file. The following command was used:

```bash
pyinstaller --onefile --noconsole <file.py>
```

### Explanation of the PyInstaller Options:

- `--onefile`: This option bundles everything (the Python interpreter, libraries, and the script) into a **single executable**. This makes it easier to distribute the program, as you only need to provide the generated `.exe` file.
  
- `--noconsole`: This option ensures that no **console window** (command prompt) is opened when the executable is run. It's particularly useful for GUI applications or scripts that do not require any terminal interaction. If the logger script doesn't need to display anything in the console, this option helps make the application more user-friendly and clean and run in the **background**.

## Running the Executable

After compiling, the generated `.exe` file can be found in the `dist` folder. To run the logger script on any Windows machine, simply double-click the `.exe` file. No further setup (like installing Python or any libraries) is needed.
