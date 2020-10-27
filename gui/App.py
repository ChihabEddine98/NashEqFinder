import tkinter as tk
from tkinter import font  as tkfont
from gui.ui.views.PureNEPage import *
from gui.ui.views.MixedNEPage import *
from gui.ui.views.AiOPage import *
from gui.ui.views.WelcomePage import *



class App(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.resizable(width=False, height=False)


        self.geometry("934x637+299+99")
        self.minsize(148, 1)
        self.maxsize(1924, 1055)
        self.resizable(0,  0)
        self.title("Nash Equilibria Finder")


        container = tk.Frame(self)
        container.configure(background="#000")
        # container.place(relx=0, rely=0, relheight=1 , relwidth=1)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)




        self.frames = {}
        for F in (WelcomePage,PureNEPage,MixedNEPage,AiOPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()