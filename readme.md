# Tiny Project Creator

This project is a **Project Creator** application built using Python and tkinter. It helps users quickly generate a structured folder setup for projects for consistency when working with others.

## Features
- Generates predefined folder structures for different project types (eg. Photos, Videos).
- Customizable folder structure through a `settings.json` file.
- Simple graphical user interface (GUI) built with `tkinter`.
- Supports light and dark themes using `sv_ttk` and `darkdetect`.

## Requirements
- Python 3.12+
- Required Python libraries:
  - tkinter
  - sv_ttk
  - darkdetect

## Installation

### Step 1: Clone the Repository
Clone this repository or download the project files.

### Step 2: Install Dependencies
Ensure that the following libraries are installed:
```bash
pip install sv_ttk darkdetect
```

### Step 3: Modify the `settings.json` File
The project folder structure is defined in the `settings.json` file. You can customize the folder structure by editing the file:
```json
{
  "Photos": ["1. INPUT", "2. WORKFILES", "3. EXPORT"],
  "Videos": [
    "1. INPUT",
    "2. ELEMENTS",
    "2. ELEMENTS\\TEMPLATES",
    "2. ELEMENTS\\TEMPLATES\\WOAH",
    "3. WORKFILES",
    "4. REFS",
    "5. SFX",
    "6. EXPORT"
  ],
  "Graphics": [
    "1. INPUT",
    "2. ELEMENTS",
    "2. ELEMENTS\\TEMPLATES",
    "2. ELEMENTS\\TEMPLATES\\WOAH",
    "3. WORKFILES",
    "4. REFS",
    "5. SFX",
    "6. EXPORT"
  ]
}
```
You can add, remove, or modify the folders as per your project needs.

### Step 4: Building the Executable
To build the application into an executable, use **PyInstaller**. Below is the command used to bundle the application into a standalone executable:
```bash
pyinstaller --onefile --windowed --icon="path_to_icon/project-creator-logo.ico" --hidden-import=tkinter --hidden-import=sv_ttk --hidden-import=darkdetect --add-data "path_to_sv_ttk/sv.tcl;sv_ttk" --add-data "path_to_sv_ttk/theme;sv_ttk/theme" --add-binary "path_to_python/python312.dll;." "path_to_script/ProjectCreator.py"
```
Refer to the provided `pyinstaller.txt` file for the exact command used to package this project.

### Step 5: Running the Application
After building, the application can be launched by running the executable file or directly running the `ProjectCreator.py` script:
```bash
python ProjectCreator.py
```

## Usage
1. Launch the application.
2. Select the project type (Photos, Videos, Graphics).
3. Click the "Create" button to generate the folder structure in the desired directory.

## Project Structure
- **settings.json**: Define the folder structure for various project types.
- **ProjectCreator.py**: The main Python script containing the GUI and folder creation logic.
- **project-creator-logo.ico**: The icon used for the application executable.
- **pyinstaller.txt**: Command used for bundling the application.

## License
This project is free for all to use.
