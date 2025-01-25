import os
import subprocess

# **********************************************
# *            Script Information              *
# **********************************************
"""
Script Name: Main Workflow Script  
Description:
    This script guides the user through the Python Starter Kit workflow,
    including reading text files and playing corresponding audio files.
"""

# **********************************************
# *             Filepath Definitions           *
# **********************************************
TEXT_PATH = r"C:\Projects\main_coding\Git_Projects\Python_Starter_Kit\assets\Text"
AUDIO_PATH = r"C:\Projects\main_coding\Git_Projects\Python_Starter_Kit\assets\Audio"
SRC_PATH = r"C:\Projects\main_coding\Git_Projects\Python_Starter_Kit\src"

# **********************************************
# *           Helper Functions                 *
# **********************************************
def open_text_file(file_name):
    """
    Opens a text file in the default text editor for reading.
    Args:
        file_name (str): Name of the text file to open.
    Returns:
        subprocess.Popen: Process handle for the opened text file.
    """
    file_path = os.path.join(TEXT_PATH, file_name)
    if not os.path.exists(file_path):
        print(f"Error: {file_name} does not exist in {TEXT_PATH}.")
        return None

    return subprocess.Popen(["notepad.exe", file_path])


def play_audio(file_name):
    """
    Plays an audio file using the default audio player.
    Args:
        file_name (str): Name of the audio file to play.
    Returns:
        subprocess.Popen: Process handle for the played audio file.
    """
    audio_file_path = os.path.join(AUDIO_PATH, file_name.replace(".txt", ".mp3"))

    if not os.path.exists(audio_file_path):
        print(f"Error: {file_name.replace('.txt', '.mp3')} does not exist in {AUDIO_PATH}.")
        return None

    try:
        return subprocess.Popen(["start", audio_file_path], shell=True)
    except Exception as e:
        print(f"Error playing audio: {e}")
        return None


def execute_file(file_name):
    """
    Executes a .bat or .exe file from the source directory.
    Args:
        file_name (str): Name of the file to execute.
    """
    file_path = os.path.join(SRC_PATH, file_name)
    if not os.path.exists(file_path):
        print(f"Error: {file_name} does not exist in {SRC_PATH}.")
        return

    os.system(f'"{file_path}"')


def get_user_choice(prompt, choices):
    """
    Gets validated user input from a list of choices.
    Args:
        prompt (str): The input prompt for the user.
        choices (list): List of valid choices.
    Returns:
        str: The validated user choice.
    """
    while True:
        choice = input(prompt).lower().strip()
        if choice in choices:
            return choice
        print(f"Invalid choice. Please select one of {choices}.")


# **********************************************
# *                Workflow Steps              *
# **********************************************
def welcome_step():
    text_process = open_text_file("Welcome.txt")
    audio_process = play_audio("Welcome.mp3")
    if audio_process:
        audio_process.wait()
    if text_process:
        text_process.terminate()

    # Ensure all resources are closed before proceeding
    print("Welcome message completed. Proceeding to the next step...")


def installation_step():
    print("Choose an installation option:")
    print("a. Install Python")
    print("b. Install Visual Studio Code")
    print("c. Install Both")
    print("d. Skip Installation")

    choice = get_user_choice("Enter your choice (a/b/c/d): ", ["a", "b", "c", "d"])

    if choice == "a":
        execute_file("Install_Python.bat")
    elif choice == "b":
        execute_file("Install_VSCode.bat")
    elif choice == "c":
        execute_file("Install_Python.bat")
        execute_file("Install_VSCode.bat")
    elif choice == "d":
        print("Skipping installation.")


def explain_project_builder():
    text_process = open_text_file("How_To_Use_Project_Builder.txt")
    audio_process = play_audio("How_To_Use_Project_Builder.mp3")
    if audio_process:
        audio_process.wait()
    if text_process:
        text_process.terminate()


def project_builder_step():
    text_process = open_text_file("Using_Project_Builder.txt")
    audio_process = play_audio("Using_Project_Builder.mp3")
    if audio_process:
        audio_process.wait()
    if text_process:
        text_process.terminate()

    print("Would you like to use the project builder?")
    print("a. Yes")
    print("b. No")
    
    project_choice = get_user_choice("Enter your choice (a/b): ", ["a", "b"])

    if project_choice == "a":
        execute_file("Setup_New_Project.exe")
    else:
        print("Skipping project builder.")


def open_project_step():
    text_process = open_text_file("Open_Project_With_VS_Code.txt")
    audio_process = play_audio("Open_Project_With_VS_Code.mp3")
    if audio_process:
        audio_process.wait()
    if text_process:
        text_process.terminate()

    print("Choose an option:")
    print("a. Launch Visual Studio Code")
    print("b. Use your own IDE")

    ide_choice = get_user_choice("Enter your choice (a/b): ", ["a", "b"])

    if ide_choice == "a":
        try:
            subprocess.Popen(["code"])
            print("Visual Studio Code launched successfully.")
        except FileNotFoundError:
            print("Error: Visual Studio Code executable not found. Ensure it is installed and added to the system PATH.")
    else:
        print("Skipping Visual Studio Code launch.")


def learn_python_step():
    print("Would you like to learn Python now?")
    print("a. Yes")
    print("b. Maybe later")

    learn_choice = get_user_choice("Enter your choice (a/b): ", ["a", "b"])

    if learn_choice == "a":
        text_process = open_text_file("Hello_World_Tutorial.txt")
        audio_process = play_audio("Hello_World_Tutorial.mp3")
        if audio_process:
            audio_process.wait()
        if text_process:
            text_process.terminate()
    else:
        print("Exiting Python Starter Kit. Have a great day!")


# **********************************************
# *                Main Logic                  *
# **********************************************
def main():
    print("Welcome to the Python Starter Kit!")

    # Step 1: Welcome
    #welcome_step()

    # Step 2: Installation Options
    #installation_step()

    # Step 3: Project Builder
    #explain_project_builder()
    #project_builder_step()

    # Step 4: Open Project in VS Code
    open_project_step()

    # Step 5: Learn Python
    learn_python_step()

    print("Thank you for using the Python Starter Kit. Happy Coding!")


if __name__ == "__main__":
    main()
