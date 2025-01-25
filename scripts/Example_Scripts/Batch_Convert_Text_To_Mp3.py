"""
**********************************************
*            Script Information             *
**********************************************
Script Name: Batch_Convert_Text_To_mp3
Author: [Kyle May]
Date: [01-12-2025]
Description:
    Converts text files to speech (MP3 files) using Google Text-to-Speech (gTTS).
**********************************************
"""

# **********************************************
# *             Import Libraries               *
# **********************************************
import os
from gtts import gTTS

# **********************************************
# *           Function Definitions             *
# **********************************************
def text_to_speech(input_file, output_file):
    """
    Converts a text file to speech and saves it as an MP3 file.
    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to save the output MP3 file.
    """
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    # Read the text from the file
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            text = file.read()
            if not text.strip():
                print(f"Error: The input text file '{input_file}' is empty.")
                return
    except Exception as e:
        print(f"Error reading the file '{input_file}': {e}")
        return

    # Generate speech from text
    try:
        tts = gTTS(text)
        tts.save(output_file)
        print(f"MP3 file has been successfully saved at: {output_file}")
    except Exception as e:
        print(f"Error generating speech from file '{input_file}': {e}")


# **********************************************
# *              Main Function                 *
# **********************************************
def main():
    """
    Main function to execute the script logic.
    Handles user input for folders and processes all text files to generate speech.
    """
    # Input the directory that you want to convert (.txt files)
    input_folder = input("Enter the full path to the folder containing text files: ").strip()
    if not input_folder:
        print("Error: Input folder path cannot be empty.")
        exit(1)

    # Input the directory that you want to place the .mp3 files in
    output_folder = input("Enter the full path to the output folder for MP3 files: ").strip()
    if not output_folder:
        print("Error: Output folder path cannot be empty.")
        exit(1)

    # Check if input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: The input folder '{input_folder}' does not exist.")
        exit(1)

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get all .txt files from the input folder
    txt_files = [file for file in os.listdir(input_folder) if file.endswith(".txt")]
    if not txt_files:
        print("No .txt files found in the input folder.")
        exit(1)

    # Process all text files in the input folder
    for file_name in txt_files:
        input_file = os.path.join(input_folder, file_name)
        output_file = os.path.join(output_folder, file_name.replace(".txt", ".mp3"))

        # Convert text to speech
        print(f"Processing file: {file_name}")
        text_to_speech(input_file, output_file)

    print("All text files have been converted to MP3 files.")

# **********************************************
# *                Main Execution              *
# **********************************************
if __name__ == "__main__":
    main()
