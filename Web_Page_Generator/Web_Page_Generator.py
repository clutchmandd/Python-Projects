from tkinter import *
import tkinter as tk

import webbrowser

# tkinter GUI
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(600,400)
        self.master.maxsize(600,400)
        self.master.title("Web Page Automation Demo")
        self.master.configure(bg='#F0F0F0')
        self.master.protocol(lambda: submit_func(self))
        arg = self.master

    def submit_func(self):
        
    # write Basic HTML Web Page with Python

        f = open('BasicHTML.html','w')

        message = """<html>
        <body><h1><%('{}'.format(self.txt_wpText))%></h1></body>
        </html>"""

        f.write(message)
        f.close()


        filename = 'file:///Users/dixon/Documents/GitHub/Python-Projects/Web_Page_Generator/' + 'BasicHTML.html'
        webbrowser.open_new_tab(filename)
        
    def load_gui(self):

        self.lbl_wpText = tk.Label(self.master,text='Enter the text to dislpay on your web page:')
        self.lbl_wpText.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

        self.txt_wpText = tk.Entry(self.master,text='')
        self.txt_wpText.grid(row=1,column=0,rowspan=1,columnspan=4,padx=(30,40),pady=(0,0),sticky=N+E+W)

        self.btn_submit = tk.Button(self.master,width=12,height=2,text='Submit',command=lambda: submit_func(self))
        self.btn_submit.grid(row=2,column=0,padx=(25,0),pady=(45,10),sticky=W)

    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
