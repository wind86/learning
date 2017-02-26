'''
Created on Feb 5, 2017

@author: ubuntu
'''
from tkinter import *


from PIL import Image, ImageTk

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
        editMenu.add_command(label="Show Img", command=self.showImg)
        editMenu.add_command(label="Show Text", command=self.showText)

        #added "file" to our menu
        mainMenu.add_cascade(label="Edit", menu=editMenu)

    def showImg(self):
        load = Image.open("chat.png")
        render = ImageTk.PhotoImage(load)

        # labels can be text or images
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()
        

    def client_exit(self):
        exit()


root = Tk()
root.geometry("400x300")
app = Window(root)

root.mainloop()  