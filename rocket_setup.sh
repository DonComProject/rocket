#!/bin/bash

# Check if Python 3 is installed
if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Installing..."
    sudo apt install python3 -y
    echo "Python 3 installed successfully."
fi

# Check if Rocket execution line is added to .bashrc file
if ! grep -q 'python3 $(pwd)/main.py' ~/.bashrc; then
    echo "Adding Rocket execution line to .bashrc file..."
    echo 'python3 $(pwd)/main.py' >> ~/.bashrc
    echo "Rocket execution line added successfully."
fi

# Update the .bashrc file
echo "Updating the .bashrc file..."
source ~/.bashrc
echo ".bashrc file updated successfully."
