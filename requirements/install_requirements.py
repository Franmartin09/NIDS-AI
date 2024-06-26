import subprocess
import sys

# Function to install a library using pip
def install_library(lib):
    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

# Read the requirements.txt file
with open('requirements.txt', 'r') as file:
    libraries = file.read().splitlines()

# Install each library
for lib in libraries:
    try:
        install_library(lib)
        print(f"Successfully installed {lib}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {lib}")

print("All libraries installed.")
