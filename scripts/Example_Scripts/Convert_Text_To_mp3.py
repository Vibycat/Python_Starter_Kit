"""
**********************************************
*            Script Information             *
**********************************************
Script Name:Convert_Text_To_mp3
Author: [Kyle]
Date: [01-12-2025]
Description:
    Converts text files to speech (MP3 files) using Google Text-to-Speech (gTTS).
**********************************************
"""

# **********************************************
# *                   Imports                  *
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
                print("Error: The input text file is empty.")
                return
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    # Generate speech from text
    try:
        tts = gTTS(text)
        tts.save(output_file)
        print(f"MP3 file has been successfully saved at: {output_file}")
    except Exception as e:
        print(f"Error generating speech: {e}")

# **********************************************
# *              Main Function                 *
# **********************************************
def main():
    
    # Specify the input text file and output MP3 file
    input_file = input(" Enter the full path to the text file:").strip() 
    output_file = input("Enter the full path for the output MP3 file: ").strip() 

    # Call the function to convert text to speech
    text_to_speech(input_file, output_file)


# **********************************************
# *                Main Execution              *
# **********************************************
if __name__ == "__main__":
    main()
