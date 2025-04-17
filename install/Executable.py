import subprocess
import sys
import os

# Function to install PyInstaller
def install_pyinstaller():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("PyInstaller installation successful!")
    except subprocess.CalledProcessError:
        print("Error installing PyInstaller. Please ensure pip is installed and try again.")
        sys.exit(1)

# Function to create the executable using PyInstaller
def create_executable(script_path):
    try:
        # Ensure that the script exists
        if not os.path.exists(script_path):
            print(f"Error: The script '{script_path}' does not exist.")
            sys.exit(1)

        print(f"Creating executable for {script_path}...")

        # Run pyinstaller to create the executable
        subprocess.check_call([sys.executable, "-m", "PyInstaller", "--onefile", script_path])
        print(f"Executable created successfully! Check the 'dist' folder.")
    except subprocess.CalledProcessError:
        print(f"Error creating executable for {script_path}.")
        sys.exit(1)

# Main function to run the script
def main():
    # Path to your specific Python script
    script_path = "C:\\Users\\Samuel\\Desktop\\Python Projects\\AssingmentTracker.py"

    # Step 1: Install PyInstaller if it's not installed
    install_pyinstaller()

    # Step 2: Create the executable
    create_executable(script_path)

if __name__ == "__main__":
    main()
