@echo off

echo Installing Latest Python...

REM Check if Python is already installed
python --version >nul 2>&1
if %errorlevel%==0 (
    echo Python is already installed.
    exit /b
)

REM Download Python installer
set "python_url=https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
set "installer=python_installer.exe"

echo Downloading Python installer...
curl -o %installer% %python_url%

REM Run the installer silently (in background)
echo Running the installer...
%installer% /quiet InstallAllUsers=1 PrependPath=1

REM Cleanup files
echo Cleaning up files...
del %installer%
echo Python installed successfully.
python --version

pause
