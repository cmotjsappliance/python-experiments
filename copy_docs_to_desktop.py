#!/usr/bin/env python3
"""
Script to copy the Docs directory to the user's Desktop.

This utility helps users create a local copy of the documentation
on their Desktop for easy offline access.
"""

import os
import shutil
import platform
from pathlib import Path


def get_desktop_path():
    """
    Get the path to the user's Desktop folder based on the operating system.
    
    Returns:
        Path object pointing to the Desktop folder
    """
    home = Path.home()
    
    # Detect OS and return appropriate Desktop path
    system = platform.system()
    
    if system == "Windows":
        desktop = home / "Desktop"
    elif system == "Darwin":  # macOS
        desktop = home / "Desktop"
    elif system == "Linux":
        # Try common Linux desktop locations
        possible_desktops = [
            home / "Desktop",
            home / "Escritorio",  # Spanish
            home / "Bureau",       # French
        ]
        # Use the first one that exists, or default to Desktop
        desktop = next((d for d in possible_desktops if d.exists()), home / "Desktop")
    else:
        desktop = home / "Desktop"
    
    return desktop


def copy_docs_to_desktop():
    """
    Copy the Docs directory to the user's Desktop.
    
    Creates a copy of the documentation folder with all its contents
    on the Desktop for easy access.
    """
    print("Python Experiments - Documentation Copy Tool")
    print("=" * 50)
    
    # Get the current script location and find the Docs directory
    current_dir = Path(__file__).parent
    docs_source = current_dir / "Docs"
    
    # Check if Docs directory exists
    if not docs_source.exists() or not docs_source.is_dir():
        print("Error: Docs directory not found in the repository.")
        print(f"Expected location: {docs_source}")
        return False
    
    # Get Desktop path
    desktop = get_desktop_path()
    
    # Check if Desktop exists
    if not desktop.exists():
        print(f"Error: Desktop directory not found at {desktop}")
        print("Please specify a custom destination.")
        return False
    
    # Set destination path
    docs_destination = desktop / "python-experiments-Docs"
    
    # Check if destination already exists
    if docs_destination.exists():
        print(f"\nWarning: '{docs_destination.name}' already exists on your Desktop.")
        response = input("Do you want to replace it? (yes/no): ").lower()
        
        if response != "yes":
            print("Operation cancelled.")
            return False
        
        # Remove existing directory
        try:
            shutil.rmtree(docs_destination)
            print("Removed existing directory.")
        except Exception as e:
            print(f"Error removing existing directory: {e}")
            return False
    
    # Copy the Docs directory
    try:
        print(f"\nCopying documentation from:")
        print(f"  {docs_source}")
        print(f"To:")
        print(f"  {docs_destination}")
        
        shutil.copytree(docs_source, docs_destination)
        
        print("\n✓ Success! Documentation has been copied to your Desktop.")
        print(f"  Location: {docs_destination}")
        
        # List the copied files
        print("\nCopied files:")
        for file in sorted(docs_destination.glob("*")):
            if file.is_file():
                print(f"  - {file.name}")
        
        return True
        
    except Exception as e:
        print(f"\n✗ Error copying documentation: {e}")
        return False


def main():
    """Main function to run the documentation copy tool."""
    try:
        success = copy_docs_to_desktop()
        
        if success:
            print("\nYou can now access the documentation offline from your Desktop!")
            print("Markdown files (.md) can be viewed in any text editor or VS Code.")
        else:
            print("\nThe documentation copy operation was not completed.")
        
        input("\nPress Enter to exit...")
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
