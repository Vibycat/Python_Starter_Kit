# Install Visual Studio Code

# Imports
import os
import subprocess
import urllib
import requests
import platform

# =========================================
# Helper Functions
# =========================================

# Install VS Code on Windows
def install_vscode_windows():
    """
    Installs Visual Studio Code on Windows, adds it to PATH,
    and enables the 'Open with Code' context menu option.
    """
    print("Installing Visual Studio Code for Windows...")
    url = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"
    installer_path = "VSCodeSetup.exe"

    try:
        # Download the installer
        print("Downloading Visual Studio Code installer...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(installer_path, "wb") as file:
                file.write(response.content)
            print(f"Downloaded installer to {installer_path}")
        else:
            raise Exception(f"Failed to download the installer. HTTP Status Code: {response.status_code}")

        # Run the installer silently with PATH addition and context menu option
        print("Running the Visual Studio Code installer...")
        subprocess.run(
            [
                installer_path,
                "/MERGETASKS=!runcode,addcontextmenufiles,addcontextmenufolders,addtopath",
                "/VERYSILENT",
                "/NORESTART"
            ],
            check=True
        )
        print("Visual Studio Code installed successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up installer file
        if os.path.exists(installer_path):
            os.remove(installer_path)
            print(f"Cleaned up installer file: {installer_path}")

# Install VS Code on Linux
def install_vscode_linux():
    """
    Installs Visual Studio Code on Linux and ensures it is added to the PATH.
    """
    print("Installing Visual Studio Code for Linux...")
    os.system("wget -q https://update.code.visualstudio.com/latest/linux-deb-x64/stable -O vscode.deb")
    os.system("sudo dpkg -i vscode.deb")
    os.system("sudo apt-get -f install -y")  # Fix missing dependencies if any
    os.remove("vscode.deb")
    print("VS Code installed successfully on Linux.")

# Install VS Code on MacOS
def install_vscode_mac():
    """
    Installs Visual Studio Code on MacOS using Homebrew.
    """
    print("Installing Visual Studio Code for Mac...")
    os.system("brew install --cask visual-studio-code")
    print("VS Code installed successfully on Mac.")

# Function to detect the operating system
def detect_os():
    """
    Detects the current operating system and returns a corresponding value.
    """
    current_os = platform.system().lower()
    if "windows" in current_os:
        return "windows"
    elif "linux" in current_os:
        return "linux"
    elif "darwin" in current_os:  # MacOS
        return "macos"
    else:
        return None

# =========================================
# Main Function
# =========================================

def install_code():
    """
    Installs Visual Studio Code based on the operating system.
    """
    detected_os = detect_os()
    if not detected_os:
        print("Unsupported operating system. Exiting...")
        return

    print(f"Detected operating system: {detected_os.capitalize()}")
    if detected_os == "windows":
        install_vscode_windows()
    elif detected_os == "linux":
        install_vscode_linux()
    elif detected_os == "macos":
        install_vscode_mac()
    else:
        print("Unable to determine operating system. Exiting...")

# =========================================
# Entry Point
# =========================================

if __name__ == "__main__":
    print("Setting up for Visual Studio Code installation...")
    install_code()
