import subprocess
import sys

def install_schedule():
    try:
        # Use subprocess to run the pip install command
        subprocess.check_call([sys.executable, "-m", "pip", "install", "schedule"])
        print("schedule installation successful!")
    except subprocess.CalledProcessError:
        print("Error installing schedule. Make sure pip is installed and try again.")

if __name__ == '__main__':
    install_schedule()
