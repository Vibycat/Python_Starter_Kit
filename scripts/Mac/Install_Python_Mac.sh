#!/bin/bash

echo "Installing the latest Python version on macOS..."

# Check if Python is already installed
if command -v python3 &>/dev/null; then
    echo "Python is already installed."
    python3 --version
    exit 0
fi

# Check if Homebrew is installed
if ! command -v brew &>/dev/null; then
    echo "Homebrew is not installed. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    echo "Homebrew installed successfully."
else
    echo "Homebrew is already installed."
fi

# Install Python using Homebrew
echo "Installing Python with Homebrew..."
brew install python

# Verify installation
echo "Python installed successfully."
python3 --version
