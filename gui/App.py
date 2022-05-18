import tkinter as tk
from tkinter import font  as tkfont
from gui.ui.views.PureNEPage import *
from gui.ui.views.MixedNEPage import *
from gui.ui.views.AiOPage import *
from gui.ui.views.WelcomePage import *
from gui.ui.views.Pure3x3NEPage import *
from algos.solver import *



class App(tk.Tk):

    def __init__(self, mx=None,*args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.mx = mx
        self.solve()
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
        for F in (WelcomePage,PureNEPage,MixedNEPage,AiOPage,Pure3x3NEPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("WelcomePage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
    
    def solve(self):
        
        M = np.array(self.mx)
        s = Solver(payoff=M)
        result=s.solve(0, 0)

        strategies=[]
        for r in result:
            if(r[0]==0 and r[1]==0):
                strategies.append("(A,C)")
            elif(r[0]==0 and r[1]==1):
                strategies.append("(A,D)")
            elif(r[0]==1 and r[1]==0):
                strategies.append("(B,C)")
            else:
                strategies.append("(B,D)")

        return