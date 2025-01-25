#!/bin/bash

echo "Installing Python..."

# Check if Python is already installed
if command -v python3 &>/dev/null; then
    echo "Python is already installed."
    exit 0
fi

# Detect OS
OS=$(uname -s)
case $OS in
    Linux)
        # Check for Linux distribution
        if [ -f /etc/debian_version ]; then
            echo "Detected Debian/Ubuntu-based system. Installing Python..."
            sudo apt update && sudo apt install -y python3 python3-pip
        elif [ -f /etc/redhat-release ]; then
            echo "Detected Red Hat-based system. Installing Python..."
            sudo dnf install -y python3 python3-pip
        else
            echo "Unsupported Linux distribution."
            exit 1
        fi
        ;;
    Darwin)
        echo "Detected macOS. Installing Python..."
        brew install python
        ;;
    *)
        echo "Unsupported operating system."
        exit 1
        ;;
esac

echo "Python installed successfully."
