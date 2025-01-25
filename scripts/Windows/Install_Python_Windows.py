import os
import subprocess
import sys
import urllib.request
import json

# =========================================
# Helper Functions
# =========================================

def is_python_installed():
    """
    Checks if Python is already installed.
    """
    try:
        subprocess.run(["python", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False

def get_latest_python_url():
    """
    Fetches the download URL for the latest Python installer from the official website.
    """
    try:
        url = "https://www.python.org/api/v2/downloads/release/?is_published=true"
        response = urllib.request.urlopen(url)
        data = json.load(response)
        for release in data["results"]:
            if "windows" in release["fields"]["version"] and "amd64" in release["fields"]["file"]:
                return release["fields"]["file"]
        raise Exception("Could not find the latest Python version.")
    except Exception as e:
        print(f"Error fetching the latest Python release: {e}")
        sys.exit(1)

def download_file(url, destination):
    """
    Downloads a file from the given URL to the specified destination.
    """
    try:
        urllib.request.urlretrieve(url, destination)
        print(f"Downloaded file from {url} to {destination}")
    except Exception as e:
        print(f"Error downloading file: {e}")
        sys.exit(1)

def install_python(installer_path):
    """
    Runs the Python installer with the required arguments.
    """
    try:
        print("Running the Python installer...")
        subprocess.run([installer_path, "/quiet", "InstallAllUsers=1", "PrependPath=1"], check=True)
        print("Python installation completed.")
    except subprocess.CalledProcessError as e:
        print(f"Error during Python installation: {e}")
        sys.exit(1)

def clean_up(installer_path):
    """
    Deletes the installer file to clean up.
    """
    try:
        os.remove(installer_path)
        print(f"Cleaned up installer: {installer_path}")
    except OSError as e:
        print(f"Error cleaning up installer: {e}")

# =========================================
# Main Function
# =========================================

def main():
    installer_path = "python_installer.exe"

    if is_python_installed():
        print("Python is already installed.")
        return

    print("Fetching the latest Python version...")
    python_url = get_latest_python_url()

    print("Downloading Python installer...")
    download_file(python_url, installer_path)

    print("Installing Python...")
    install_python(installer_path)

    print("Cleaning up files...")
    clean_up(installer_path)

    print("Python installed successfully.")
    subprocess.run(["python", "--version"])

if __name__ == "__main__":
    main()
