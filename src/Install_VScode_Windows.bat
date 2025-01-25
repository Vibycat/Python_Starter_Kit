@echo off
:: Set the URL for the Visual Studio Code installer
set "vscode_url=https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user"

:: Set the file name for the installer
set "installer_name=VSCodeSetup-x64.exe"

:: Download the installer
echo Downloading Visual Studio Code installer...
powershell -Command "Invoke-WebRequest -Uri '%vscode_url%' -OutFile '%installer_name%'"

:: Check if the download was successful
if not exist "%installer_name%" (
    echo Failed to download Visual Studio Code installer.
    pause
    exit /b 1
)

:: Run the installer silently
echo Installing Visual Studio Code...
start /wait "" "%installer_name%" /VERYSILENT /NORESTART

:: Clean up the installer
del "%installer_name%"
echo Installation completed.

:: Pause to show completion message
pause
