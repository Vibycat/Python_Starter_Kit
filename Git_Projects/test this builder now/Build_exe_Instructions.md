# Instructions for Compiling the Python Script into an Executable

This guide walks you through the process of converting your Python script into a standalone executable file using PyInstaller. The instructions include the necessary steps to ensure your `templates` folder is bundled with the executable.

---

## Prerequisites

Before compiling the script, ensure the following are set up:

1. **Python Installed**:
   - Download and install Python from [python.org](https://www.python.org/downloads/).
   - Add Python to your system's PATH during installation.

2. **PyInstaller Installed**:
   - Install PyInstaller via pip:
     ```bash
     pip install pyinstaller
     ```

3. **Project Structure**:
   - Your project should have the following structure:
     ```
     root/
     ├── src/
     │   ├── Setup_New_Project.py  # The main Python script to compile
     │   └── templates/            # The templates folder
     └── ...
     ```

---

## Steps to Compile the Script

### 1. Open a Terminal or Command Prompt

Navigate to the directory containing your Python script. Replace `<project-path>` with the full path to your `src` directory:
```bash
cd <project-path>
```

For example:
```bash
cd C:\Projects\main_coding\Git_Projects\Setup_New_Git_Pro\src
```

---

### 2. Run the PyInstaller Command

Use the following PyInstaller command to compile the script into a standalone executable:
```bash
pyinstaller --add-data "templates;templates" --onefile Setup_New_Project.py
```

**Explanation**:
- `--add-data "templates;templates"`: Ensures the `templates` folder is bundled with the executable. The `;` separator works on Windows; for macOS/Linux, replace it with a `:` (`templates:templates`).
- `--onefile`: Packages everything into a single executable file.
- `Setup_New_Project.py`: Specifies the script to compile.

---

### 3. Locate the Compiled Executable

After running the command, PyInstaller will create several new folders in your `src` directory:

- **`build/`**: Temporary files created during the build process.
- **`dist/`**: Contains the compiled executable file.
- **`Setup_New_Project.spec`**: Configuration file for PyInstaller.

The compiled executable will be located in the `dist/` folder:
```
src/dist/Setup_New_Project.exe
```

---

### 4. Test the Executable

Run the executable to ensure it works as expected:
```bash
cd dist
Setup_New_Project.exe
```

---

### 5. (Optional) Clean Up Build Artifacts

You can delete the `build/` and `.spec` files to clean up your project:
```bash
rm -rf build
rm Setup_New_Project.spec
```

---

## Troubleshooting

1. **Error: Missing Templates Folder**:
   - Ensure the `templates` folder exists in the same directory as `Setup_New_Project.py`.
   - Verify the `--add-data` argument is correctly formatted based on your OS:
     - Windows: `templates;templates`
     - macOS/Linux: `templates:templates`

2. **Executable Doesn't Work**:
   - Run the script directly with Python to debug any errors:
     ```bash
     python Setup_New_Project.py
     ```

---

## Notes

- If additional files or folders need to be included in the build, add them using additional `--add-data` arguments.
- For cross-platform compatibility, test the executable on the target operating systems.

---


