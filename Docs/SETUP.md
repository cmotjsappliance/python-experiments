# Setup Instructions

This guide provides detailed setup instructions for working with the Python Experiments repository.

## System Requirements

- **Python**: Version 3.6 or higher
- **Operating System**: Windows, macOS, or Linux
- **IDE**: VS Code (recommended) or any Python-compatible IDE
- **Git**: For cloning the repository (optional if downloading as ZIP)

## Installation Steps

### 1. Install Python

#### Windows
1. Download Python from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important**: Check "Add Python to PATH" during installation
4. Verify installation: Open Command Prompt and type `python --version`

#### macOS
1. Install using Homebrew: `brew install python3`
2. Or download from [python.org](https://www.python.org/downloads/)
3. Verify installation: Open Terminal and type `python3 --version`

#### Linux
1. Most Linux distributions come with Python pre-installed
2. If needed: `sudo apt-get install python3` (Ubuntu/Debian)
3. Verify installation: `python3 --version`

### 2. Install VS Code (Recommended)

1. Download VS Code from [code.visualstudio.com](https://code.visualstudio.com/)
2. Install the Python extension:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X or Cmd+Shift+X)
   - Search for "Python"
   - Install the Microsoft Python extension

### 3. Get the Repository

#### Option A: Clone with Git
```bash
git clone https://github.com/cmotjsappliance/python-experiments.git
cd python-experiments
```

#### Option B: Download as ZIP
1. Go to the repository on GitHub
2. Click the green "Code" button
3. Select "Download ZIP"
4. Extract the ZIP file to your desired location

### 4. Create a Working Folder

1. Create a folder on your device for the project
2. Give it a meaningful name (e.g., "python-experiments")
3. This helps VS Code manage files and save data properly

### 5. Open in VS Code

1. Open VS Code
2. File → Open Folder
3. Select your python-experiments folder
4. VS Code will load the project

## Running Your First Experiment

1. Open `calculator_up_to_1000.py` in VS Code
2. Open the Python REPL:
   - Windows/Linux: Press `Ctrl + Shift + \``
   - Mac: Press `Cmd + Shift + \``
3. Run the code in the REPL
4. Interact with the calculator by following the prompts

## Troubleshooting

### Python Not Found
- Ensure Python is added to your system PATH
- Restart your terminal/VS Code after installing Python

### REPL Not Opening
- Verify the Python extension is installed in VS Code
- Check that Python is properly detected by VS Code (bottom-left corner)

### File Permission Issues
- Ensure you have write permissions in the folder where you cloned/extracted the repository

## Next Steps

- Read [GETTING_STARTED.md](GETTING_STARTED.md) for usage instructions
- Explore the calculator experiment in [CALCULATOR.md](CALCULATOR.md)
- Start experimenting with the code!

## Additional Resources

- [Python Official Documentation](https://docs.python.org/)
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Python Beginners Guide](https://wiki.python.org/moin/BeginnersGuide)
