import subprocess
import sys

def install_plyer():
    try:
        # Use subprocess to run the pip install command
        subprocess.check_call([sys.executable, "-m", "pip", "install", "plyer"])
        print("plyer installation successful!")
    except subprocess.CalledProcessError:
        print("Error installing plyer. Make sure pip is installed and try again.")

if __name__ == '__main__':
    install_plyer()
