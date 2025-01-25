Project Workflow 


1. Launch the Intro Text file "Welcome.txt"
    - Read the "Welcome.txt" file using the "Welcome.py"
2. Launch the "Getting_Started.txt"
    - Read the "Getting_Started.txt" file using the "Getting_Started.py" 
3. Present the user with options: 
    a. Install Python (Latest version)
    b. Install Visual Studio Code (Latest version)
    C. Install Python and Visual Studio Code 
    D. Skip Install ( I already have python and an IDE)

    if == a: 
        Run "Install_Python.bat" 
    if == b:
        Run "Install_VSCode.exe" or "Install_VSCode.bat" 
    if == C: 
        Run "Install_Python.bat"
        Run "Install_VSCode.bat"
    if == D:
        break

4. Launch the Project builder text file "Using_Project_Builder.txt"
    -Read the "Using_Project_Builder.txt" file using the "Using_Project_Builder.py"
5. Present the user with options: 
    a. Use the project builder
    b. Skip the project builder 

    if == a: 
        Run "Setup_New_Project.exe" 
    else:
        break
6. Launch the "Open_Project_With_VS_Code.txt" 
    -Read the Open_Project_With_VS_Code.txt"  with Open_Project_With_VS_Code.py"

7. Present user with options: 
    a. Launch Visual Studio code
    b. Use your own IDE 

    if ==a: 
        Run "Launch_VSCode.py" or "Launch_VSCode.exe"
    else:
        break
8. Present User with options: 
    a. Learn to code 
    b. Maybe later

    if ==a: 
        Launch "Hello_World_Tutorial.txt"
            - Read "Hello_World_Tutorial.txt" file with "Hello_World_Tutorial.py"
    