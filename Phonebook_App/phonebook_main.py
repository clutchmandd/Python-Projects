# Python Ver:      3.9.7
#
# Author:          David Dixon
#
# Purpose:         Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#                  using Tkinter Parent and Child relationships.
#
# Tested OS:       This code was written and tested to work with MacOS Catalina 10.15.7

from tkinter import *
import tkinter as tk
from tkinter import messagebox


# Be sure to import my other modules so we can have access to them
import phonebook_gui
import phonebook_func


# Frame is the Tkinter frame class that my own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define my master frame configuration
        self.master = master
        self.master.minsize(600,400) #(Height, Width)
        self.master.maxsize(600,400)
        # This CenterWindow method will counter my app on the user's screen
        phonebook_func.center_window(self,600,400)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        self.master.protocol(lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a seperate module,
        # keeping my code compartmentalized and clutter free
        phonebook_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
