import time
import shutil
import os
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    link_Label = Label(root, text='Select the File to Copy: ', bg='lightgray')
    link_Label.grid(row=1, column=0, pady=5, padx=5)

    root.sourceText = Entry(root, width=50, textvariable = sourceLocation)
    root.sourceText.grid(row=1, column=1, pady=5, padx=5, columnspan=2)

    source_browseButton = Button(root, text='Browse', command = SourceBrowse, width=15)
    source_browseButton.grid(row=1, column=3, pady=5, padx=5)

    destinationLabel = Label(root, text='Select The Destination: ', bg='lightgray')
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=50, textvariable = destinationLocation)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5, columnspan=2)

    dest_browseButton = Button(root, text='Browse', command = DestinationBrowse, width = 15)
    dest_browseButton.grid(row=2, column=3, pady=5, padx=5)

    archiveButton = Button(root, text='Archive File', command = ArchiveFile, width=15)
    archiveButton.grid(row=3, column=1, pady=5, padx=5)

def SourceBrowse():

    # Opening the file-dialog directory prompting the user to select files to copy
    # using the filedialog.askopenfilenames() method. Setting the initialdir argument.
    # Converting the selection to list using list()
    root.files_list = filedialog.askdirectory(initialdir='/FolderA/')

    # Displaying the selected files in the root.sourceText Entry
    root.sourceText.insert('1', root.files_list)

def DestinationBrowse():

    # Opening the file-dialog directory prompting the user to select the destination folder.
    destinationdirectory = filedialog.askdirectory(initialdir='/FolderB/')

    # Displaying the selected directory in the root.destinationText Entry
    root.destinationText.insert('1', destinationdirectory)

SECONDS_IN_DAY = 24 * 60 * 60

now = time.time()
before = now - SECONDS_IN_DAY

def ArchiveFile(fname):
    return os.path.getmtime(fname)

    for fname in os.listdir(sourceLocation):
        sourceLocation_fname = os.path.join(sourceLoction, fname)
        if last_mod_time(sourLocation_fname) > before:
                destinationLocation_fname = os.path.join(destinationLocation, fname)
                shutil.move(sourceLocation_fname, destinationLocation_fname)

    messagebox.showinfo('SUCCESSFULL!')

    
# Creating object of tk class
root = tk.Tk()
root.geometry('830x120')
root.title('File-Transfer App')
root.config(background = 'lightgray')

# Creating tkinter variable
sourceLocation = StringVar()
destinationLocation = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop
root.mainloop()





