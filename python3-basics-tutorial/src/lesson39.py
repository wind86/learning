'''
Created on Feb 5, 2017

@author: ubuntu
'''
from tkinter import *

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)

        mainMenu = Menu(self.master)
        self.master.config(menu=mainMenu)

        fileMenu = Menu(mainMenu)
        fileMenu.add_command(label="Exit", command=self.client_exit)
        mainMenu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(mainMenu)
        editMenu.add_command(label="Undo")
        mainMenu.add_cascade(label="Edit", menu=editMenu)

    def client_exit(self):
        exit()

root = Tk()
root.geometry("400x300")

app = Window(root)
root.mainloop()