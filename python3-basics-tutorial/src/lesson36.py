'''
Created on Jan 30, 2017

@author: ubuntu
'''
from tkinter import *

class Window(Frame):
    def init(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        
root = Tk()
app = Window(root)
root.mainloop()