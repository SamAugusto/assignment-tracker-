
import subprocess
import sys

# Function to install win10toast
def install_win10toast():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "win10toast"])
        print("win10toast installation successful!")
    except subprocess.CalledProcessError:
        print("Error installing win10toast. Please ensure pip is installed and try again.")

if __name__ == "__main__":
    install_win10toast()
