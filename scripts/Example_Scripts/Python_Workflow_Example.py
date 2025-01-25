"""
**********************************************
*            Script Information             *
**********************************************
Script Name: Python Workflow Example
Author: [Your Name]
Date: [Current Date]
Description:
    Demonstrates the typical structure and workflow of a Python script, including
    imports, class declarations, functions, and a main execution block.
Version: [Current Version]
**********************************************
"""

# **********************************************
# *             Import Libraries              *
# **********************************************
# Standard library imports (e.g., os for file operations)
import os

# **********************************************
# *          Class Definitions               *
# **********************************************
class Greeting:
    """
    A simple class to demonstrate class structure in Python.
    """

    def __init__(self, name):
        """
        Initializes the Greeting class with a name.
        Args:
            name (str): The name to use in the greeting.
        """
        self.name = name

    def say_hello(self):
        """
        Returns a greeting message.
        Returns:
            str: A personalized greeting message.
        """
        return f"Hello, {self.name}! Welcome to the Python script example."

# **********************************************
# *           Function Definitions            *
# **********************************************
def display_working_directory():
    """
    Prints the current working directory.
    """
    print(f"Current Working Directory: {os.getcwd()}")

def print_greeting(name):
    """
    Prints a personalized greeting message.
    Args:
        name (str): Name to include in the greeting.
    """
    greeter = Greeting(name)
    print(greeter.say_hello())

# **********************************************
# *                Main Logic                 *
# **********************************************
if __name__ == "__main__":
    """
    Main execution block for the script. Demonstrates a simple workflow with examples.
    """
    # Step 1: Display the current working directory
    display_working_directory()

    # Step 2: Ask the user for their name
    user_name = input("Enter your name: ").strip()

    # Step 3: Print a personalized greeting
    print_greeting(user_name)

    # Step 4: Completion message
    print("This is the end of the example script. Have a great day!")
