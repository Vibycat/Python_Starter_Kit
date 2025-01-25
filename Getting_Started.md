
# **Getting Started with Python**

Welcome to your Python starter kit! Follow these steps to set up your environment and start coding in Python.

---

## **Step 1: Install Python**
Python is the programming language you'll be working with. Let’s get it installed:

### **Windows**
1. Run the any of the following files:
   - Navigate to the `scripts/Windows` folder in this project.
   - Option 1 Double click on the `Install_Python_Windows.bat`
   - Option 2 Double click on the `Install_Python_Windows.exe`
  
2. This will:
   - Download the Python installer.
   - Install Python on your system.
   - Add Python to your system's PATH.

3. Verify the installation:
   - Open a Command Prompt and type:
     ```cmd
     python --version
     ```
   - You should see the installed Python version.

### **Linux**
1. Open a terminal and run the `Install_Python_Linux.bash` script:
   ```bash
   ./scripts/Install_Python_Linux.bash
   ```
2. Follow the prompts to complete the installation.
3. Verify the installation:
   ```bash
   python3 --version
   ```

### **macOS**
1. Open a terminal and run the `Install_Python_Mac.sh` script:
   ```bash
   ./scripts/Install_Python_Mac.sh
   ```
2. Follow the instructions to complete the installation.
3. Verify the installation:
   ```bash
   python3 --version
   ```

---

## **Step 2: Install Visual Studio Code**
Visual Studio Code (VS Code) is a powerful code editor we'll use for writing Python code.

1. Run the `Install_VScode_Windows.bat` script:
   ```bash
   python scripts/Install_VisualStudioCode.py
   ```
2. This will:
   - Download and install VS Code.
   - Set it up for use with Python.

---

## **Step 3: Set Up a Python Virtual Environment (Optional)**
Using a virtual environment ensures your projects have isolated dependencies.

1. Open a terminal or command prompt.
2. Create a virtual environment:
   ```bash
   python -m venv myenv
   ```
3. Activate the virtual environment:
   - **Windows**:
     ```cmd
     myenv\Scripts\activate
     ```
   - **Linux/macOS**:
     ```bash
     source myenv/bin/activate
     ```
4. Your terminal prompt should now show `(myenv)`. This indicates the environment is active.

---

## **Step 4: Explore the Example Scripts**
1. Navigate to the `scripts` folder.
2. Open and review the example scripts:
   - `main_script.py`: A simple script to demonstrate Python basics.
   - `testing_script.py`: A script for practicing and testing your Python skills.

3. Run a script using Python:
   ```bash
   python scripts/main_script.py
   ```

---

## **Step 5: Learn Python Basics**
Here are a few beginner-friendly topics to explore:
1. **Variables and Data Types**:
   - Numbers, Strings, Lists, Dictionaries.
2. **Control Flow**:
   - `if`, `else`, `for`, and `while` loops.
3. **Functions**:
   - How to define and call functions.
4. **File I/O**:
   - Reading from and writing to files.

You can practice these concepts using the included `testing_script.py`.

---

## **Step 6: Write Your First Python Program**
1. Open VS Code.
2. Create a new file named `hello_world.py`.
3. Write the following code:
   ```python
   print("Hello, world!")
   ```
4. Save the file and run it:
   ```bash
   python hello_world.py
   ```

---

## **Step 7: Explore Additional Resources**
- [Python Official Documentation](https://docs.python.org/3/)
- [Visual Studio Code Documentation](https://code.visualstudio.com/docs)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)
- [Real Python](https://realpython.com/)

---

## **Step 8: What's Next?**
- Explore the `HOW_TO_PYTHON` folder for more tips and tricks.
- Start working on small projects like:
  - A calculator.
  - A to-do list app.
  - A number guessing game.

---

This starter kit is your stepping stone to becoming a Python developer. Have fun coding, and don’t hesitate to ask questions or explore new ideas!
