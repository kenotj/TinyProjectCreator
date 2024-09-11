import json
import os
import tkinter as tk      # Import tkinter to create GUI
from tkinter import ttk   # Import ttk module to create themed widget
from tkinter import font  # Import font module to change font sizes
import sv_ttk             # Import sv_ttk to set theme
import darkdetect         # Import darkdetect to detect OS theme

# Function to create project
def CreateProject():
    project_name = entry_project_name.get()
    project_type = combo_project_type.get()

    # Check if project name is empty
    if project_name == "":
        label_project_name_error.config(text="Project name cannot be empty")
        return
    else:
        label_project_name_error.config(text="")

    # Check if project type is empty
    if project_type == "":
        label_project_type_error.config(text="Project type cannot be empty")
        return
    else:
        label_project_type_error.config(text="")

    # Get current working directory
    current_directory = os.getcwd()

    # Create project folder in the current directory
    project_folder = os.path.join(current_directory, project_name)
    os.makedirs(project_folder, exist_ok=True)

    # Create subfolders based on project type from settings.json
    with open('settings.json') as file_settings:
        settings = json.load(file_settings)

    # Check if project type exists in settings
    if project_type in settings:
        subfolders = settings[project_type]
    else:
        subfolders = []

    file_settings.close()

    # Create subfolders
    for folder in subfolders:
        if "\\" in folder:
            folders = folder.split("\\")
            folder_path = project_folder
            for subfolder in folders:
                folder_path = os.path.join(folder_path, subfolder)
                os.makedirs(folder_path, exist_ok=True)
        else:
            folder_path = os.path.join(project_folder, folder)
            os.makedirs(folder_path, exist_ok=True)

    # Success feedback
    label_success.config(text=f"Project '{project_name}' created successfully!", foreground="green")

# Function to check theme change
def check_theme_change():
    # Get the current OS theme
    current_theme = darkdetect.theme()

    # Check if the current theme is dark or light and set the sv_ttk theme accordingly
    if current_theme == "Dark":
        sv_ttk.set_theme("dark")
    else:
        sv_ttk.set_theme("light")

    # Check again after 1 second (1000 milliseconds)
    vRoot.after(1000, check_theme_change)


vRoot = tk.Tk()
vRoot.title("Bynd Socials - Project Creator")
vRoot.configure(padx=50, pady=50)

# Make responsive
vRoot.grid_rowconfigure(0, weight=1)
vRoot.grid_columnconfigure(0, weight=1)

# Properties
default_font = font.nametofont("TkDefaultFont")
default_size = default_font.cget("size")
large_font  = font.Font(size=default_size + 2)
normal_font = font.Font(size=default_size)
small_font  = font.Font(size=default_size - 2)

vPadY = 5
vPadY2 = vPadY * 2
vPadY4 = vPadY * 4

# MENU BAR
menuBar = tk.Menu(vRoot)
vRoot.config(menu = menuBar)
menuFileLabel = tk.Menu(menuBar, tearoff=0)
menuFileLabel.add_command(label="Exit", command=vRoot.quit)
menuBar.add_cascade(label="File", menu=menuFileLabel)

vRow = 1
# ENTRY - PROJECT NAME
label_project_name = ttk.Label(vRoot, text="Enter your Project Name", font=large_font)
label_project_name.grid(row=vRow, column=0, columnspan=2, pady=vPadY, sticky="nsew")
vRow += 1
label_project_name_error = ttk.Label(vRoot, text="", foreground="red", font=small_font)
label_project_name_error.grid(row=vRow, column=0, columnspan=2, pady=vPadY, sticky="nsew")
vRow += 1
entry_project_name = ttk.Entry(vRoot, font=normal_font)
entry_project_name.grid(row=vRow, column=0, columnspan=2, pady=vPadY2, sticky="nsew")
vRow += 3

# COMBO - PROJECT TYPE
label_project_type = ttk.Label(vRoot, text="Select your Project Type", font=large_font)
label_project_type.grid(row=vRow, column=0, columnspan=2, pady=vPadY, sticky="nsew")
vRow += 1
label_project_type_error = ttk.Label(vRoot, text="", foreground="red", font=small_font)
label_project_type_error.grid(row=vRow, column=0, columnspan=2, pady=vPadY, sticky="nsew")
vRow += 1

# Create combobox with values from settings.json
# Read values from settings.json
with open('settings.json') as file_settings:
    settings = json.load(file_settings)
    values = settings.keys()
file_settings.close()
combo_project_type = ttk.Combobox(vRoot, values=list(values), state="readonly", font=normal_font)
combo_project_type.grid(row=vRow, column=0, columnspan=2, pady=vPadY2, sticky="nsew")
vRow += 2

# BUTTON - CREATE PROJECT
button_create = ttk.Button(vRoot, text="Create project")
button_create.grid(row=vRow, column=0, pady=30, sticky="nsew")
button_create.config(command=CreateProject)
vRow += 1

# LABEL - SUCCESS
label_success = ttk.Label(vRoot, text="", font=small_font)
label_success.grid(row=vRow, column=0, columnspan=2, pady=vPadY, sticky="nsew")

# Resize to fit all widgets
vRoot.update_idletasks()

# Dynamically resize the window based on widgets
vRoot.geometry(f"{vRoot.winfo_reqwidth()}x{vRoot.winfo_reqheight()}")


# Set theme according to OS theme
check_theme_change()

# Run program
vRoot.mainloop()