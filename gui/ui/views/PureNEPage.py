import numpy as np
import tkinter as tk
from tkinter.messagebox import showerror
from algos.Solver import *


class PureNEPage(tk.Frame):

    def resetColors(self):
        bg_col = "#000"
        fg_col = "#fff"
        p1_col = "#1efff3"
        p2_col = "#ff3d5e"
        # 0,0 Case !
        self.payoffFrame00.configure(background=bg_col)
        self.payoffLP00.configure(background=bg_col)
        self.payoffLP00.configure(foreground=fg_col)
        self.payoffRP00.configure(background=bg_col)
        self.payoffRP00.configure(foreground=fg_col)
        self.payoffV00.configure(background=bg_col)
        self.payoffV00.configure(foreground=fg_col)
        self.payoffEntryL00.configure(background=bg_col, relief="groove")
        self.payoffEntryR00.configure(background=bg_col, relief="groove")
        self.payoffEntryL00.configure(foreground=p1_col)
        self.payoffEntryR00.configure(foreground=p2_col)
        # 0,1 Case !
        self.payoffFrame01.configure(background=bg_col)
        self.payoffLP01.configure(background=bg_col)
        self.payoffLP01.configure(foreground=fg_col)
        self.payoffRP01.configure(background=bg_col)
        self.payoffRP01.configure(foreground=fg_col)
        self.payoffV01.configure(background=bg_col)
        self.payoffV01.configure(foreground=fg_col)
        self.payoffEntryL01.configure(background=bg_col, relief="groove")
        self.payoffEntryR01.configure(background=bg_col, relief="groove")
        self.payoffEntryL01.configure(foreground=p1_col)
        self.payoffEntryR01.configure(foreground=p2_col)

        # 1,0 Case !
        self.payoffFrame10.configure(background=bg_col)
        self.payoffLP10.configure(background=bg_col)
        self.payoffLP10.configure(foreground=fg_col)
        self.payoffRP10.configure(background=bg_col)
        self.payoffRP10.configure(foreground=fg_col)
        self.payoffV10.configure(background=bg_col)
        self.payoffV10.configure(foreground=fg_col)
        self.payoffEntryL10.configure(background=bg_col, relief="groove")
        self.payoffEntryR10.configure(background=bg_col, relief="groove")
        self.payoffEntryL10.configure(foreground=p1_col)
        self.payoffEntryR10.configure(foreground=p2_col)

        # 1,1 Case !
        self.payoffFrame11.configure(background=bg_col)
        self.payoffLP11.configure(background=bg_col)
        self.payoffLP11.configure(foreground=fg_col)
        self.payoffRP11.configure(background=bg_col)
        self.payoffRP11.configure(foreground=fg_col)
        self.payoffV11.configure(background=bg_col)
        self.payoffV11.configure(foreground=fg_col)
        self.payoffEntryL11.configure(background=bg_col, relief="groove")
        self.payoffEntryR11.configure(background=bg_col, relief="groove")
        self.payoffEntryL11.configure(foreground=p1_col)
        self.payoffEntryR11.configure(foreground=p2_col)

    def reset(self):
        valNull1=tk.StringVar()
        valNull1.set("")
        self.payoffEntryL00.configure(text=valNull1)

        valNull2 = tk.StringVar()
        valNull2.set("")
        self.payoffEntryL10.configure(textvariable=valNull2)

        valNull3 = tk.StringVar()
        valNull3.set("")
        self.payoffEntryL11.configure(textvariable=valNull3)

        valNull4 = tk.StringVar()
        valNull4.set("")
        self.payoffEntryR00.configure(textvariable=valNull4)

        valNull5 = tk.StringVar()
        valNull5.set("")
        self.payoffEntryR01.configure(textvariable=valNull5)

        valNull6 = tk.StringVar()
        valNull6.set("")
        self.payoffEntryR10.configure(textvariable=valNull6)

        valNull7 = tk.StringVar()
        valNull7.set("")
        self.payoffEntryR11.configure(textvariable=valNull7)

        valNull8 = tk.StringVar()
        valNull8.set("")
        self.payoffEntryL01.configure(textvariable=valNull8)
        self.resetColors()
        self.resultLabel.config(text='')

    def showNE(self,frame,lp,v,rp,lpo,rpo):
        bg_color="#28fa63"
        fg_color="black"
        frame.configure(background=bg_color)
        lp.configure(background=bg_color)
        v.configure(background=bg_color)
        rp.configure(background=bg_color)
        lpo.configure(background=bg_color)
        rpo.configure(background=bg_color)

        lp.configure(foreground=fg_color)
        rp.configure(foreground=fg_color)
        v.configure(foreground=fg_color)
        lpo.configure(foreground=fg_color,relief="flat")
        rpo.configure(foreground=fg_color,relief="flat")

    def solve(self):

        try:
            # We need to transofrm our GUI entries to variables  !
            po00 = (int(self.payoffEntryL00.get()), int(self.payoffEntryR00.get()))
            po01 = (int(self.payoffEntryL01.get()), int(self.payoffEntryR01.get()))
            po10 = (int(self.payoffEntryL10.get()), int(self.payoffEntryR10.get()))
            po11 = (int(self.payoffEntryL11.get()), int(self.payoffEntryR11.get()))
            payoff = [[po00, po01], [po10, po11]]

            M = np.array(payoff)
            s = Solver(payoff=M)
            result=s.solve(1, 0)

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

            ne=" , ".join(strategies)
            ne_msg=f'Pure Nash Equiliberia Strategies :\n{ne}\n'
            print(ne_msg)
            self.resultLabel.config(text=ne_msg)

            po00 = (self.payoffFrame00, self.payoffLP00, self.payoffV00,
                    self.payoffRP00, self.payoffEntryL00, self.payoffEntryR00)
            po01 = (self.payoffFrame01, self.payoffLP01, self.payoffV01,
                    self.payoffRP01, self.payoffEntryL01, self.payoffEntryR01)
            po10 = (self.payoffFrame10, self.payoffLP10, self.payoffV10,
                    self.payoffRP10, self.payoffEntryL10, self.payoffEntryR10)
            po11 = (self.payoffFrame11, self.payoffLP11, self.payoffV11,
                    self.payoffRP11, self.payoffEntryL11, self.payoffEntryR11)

            show_ne = [po00, po01, po10, po11]
            print(result)
            res2Show = []
            for r in result:
                bin_num = str(r[0]) + str(r[1])
                idx = int(bin_num, 2)
                res2Show.append(idx)

            for i in res2Show:
                self.showNE(show_ne[i][0], show_ne[i][1], show_ne[i][2],
                            show_ne[i][3], show_ne[i][4], show_ne[i][5])


        except ValueError as verr:
            showerror(title=" Invalid PayOff", message=" All entries need to be Integers!")
            return




    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#000")
        bg_col="#000"
        fg_col="#fff"
        p1_col="#1efff3"
        p2_col="#ff3d5e"

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'



        self.titleFrame = tk.Frame(self)

        self.titleFrame.place(relx=0.041, rely=0.028, relheight=0.124
                , relwidth=0.928)
        self.titleFrame.configure(relief='flat')
        self.titleFrame.configure(borderwidth="2")
        self.titleFrame.configure(background="#000000")

        self.titleLabel = tk.Label(self.titleFrame)
        self.titleLabel.place(relx=0.168, rely=0.241, height=34, width=600)
        self.titleLabel.configure(background="#000000")
        self.titleLabel.configure(disabledforeground="#a3a3a3")
        self.titleLabel.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.titleLabel.configure(foreground="#fff")
        self.titleLabel.configure(text='''Pure Nash Equilibria''')

        self.mainFrame = tk.Frame(self)
        self.mainFrame.place(relx=0.041, rely=0.176, relheight=0.728
                , relwidth=0.922)
        self.mainFrame.configure(relief='flat')
        self.mainFrame.configure(borderwidth="2")
        self.mainFrame.configure(background="#000")

        self.payoffMatrixFrame = tk.Frame(self.mainFrame)
        self.payoffMatrixFrame.place(relx=0.11, rely=0.343, relheight=0.573
                , relwidth=0.605)
        self.payoffMatrixFrame.configure(relief='flat')
        self.payoffMatrixFrame.configure(borderwidth="2")
        self.payoffMatrixFrame.configure(background="#000")

        self.payoffFrame00 = tk.Frame(self.payoffMatrixFrame)
        self.payoffFrame00.place(relx=0.056, rely=0.086, relheight=0.331
                , relwidth=0.417)
        self.payoffFrame00.configure(relief='groove')
        self.payoffFrame00.configure(borderwidth="2")
        self.payoffFrame00.configure(relief="groove")
        self.payoffFrame00.configure(background="#000")
        self.payoffFrame00.configure(highlightbackground="#d9d9d9")
        self.payoffFrame00.configure(highlightcolor="black")

        self.payoffEntryL00 = tk.Entry(self.payoffFrame00,justify="center")
        self.payoffEntryL00.place(relx=0.161, rely=0.25, height=42
                , relwidth=0.203)
        self.payoffEntryL00.configure(background=bg_col)
        self.payoffEntryL00.configure(disabledforeground="#a3a3a3")
        self.payoffEntryL00.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryL00.configure(foreground=p1_col)
        self.payoffEntryL00.configure(highlightbackground="#d9d9d9")
        self.payoffEntryL00.configure(highlightcolor="black")
        self.payoffEntryL00.configure(insertbackground=fg_col)
        self.payoffEntryL00.configure(selectbackground="blue")
        self.payoffEntryL00.configure(selectforeground="white")
        self.payoffEntryL00.configure(relief="groove")

        self.payoffEntryR00 = tk.Entry(self.payoffFrame00,justify="center")
        self.payoffEntryR00.place(relx=0.594, rely=0.25, height=42
                , relwidth=0.203)
        self.payoffEntryR00.configure(background=bg_col)
        self.payoffEntryR00.configure(disabledforeground="#a3a3a3")
        self.payoffEntryR00.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryR00.configure(foreground=p2_col)
        self.payoffEntryR00.configure(highlightbackground="#d9d9d9")
        self.payoffEntryR00.configure(highlightcolor="black")
        self.payoffEntryR00.configure(insertbackground=fg_col)
        self.payoffEntryR00.configure(selectbackground="blue")
        self.payoffEntryR00.configure(selectforeground="white")
        self.payoffEntryR00.configure(relief="groove")

        self.payoffLP00 = tk.Label(self.payoffFrame00)
        self.payoffLP00.place(relx=0.051, rely=0.216, height=40, width=16)
        self.payoffLP00.configure(activebackground="#f9f9f9")
        self.payoffLP00.configure(activeforeground="black")
        self.payoffLP00.configure(background="#000")
        self.payoffLP00.configure(disabledforeground="#a3a3a3")
        self.payoffLP00.configure(font="-family {Segoe UI Emoji} -size 22 -weight bold")
        self.payoffLP00.configure(foreground="#fff")
        self.payoffLP00.configure(highlightbackground="#d9d9d9")
        self.payoffLP00.configure(highlightcolor="black")
        self.payoffLP00.configure(text='''(''')

        self.payoffRP00 = tk.Label(self.payoffFrame00)
        self.payoffRP00.place(relx=0.871, rely=0.216, height=40, width=16)
        self.payoffRP00.configure(activebackground="#f9f9f9")
        self.payoffRP00.configure(activeforeground="black")
        self.payoffRP00.configure(background="#000")
        self.payoffRP00.configure(disabledforeground="#a3a3a3")
        self.payoffRP00.configure(font="-family {Segoe UI Emoji} -size 22 -weight bold")
        self.payoffRP00.configure(foreground="#fff")
        self.payoffRP00.configure(highlightbackground="#d9d9d9")
        self.payoffRP00.configure(highlightcolor="black")
        self.payoffRP00.configure(text=''')''')

        self.payoffV00 = tk.Label(self.payoffFrame00)
        self.payoffV00.place(relx=0.433, rely=0.102, height=52, width=28)
        self.payoffV00.configure(activebackground="#f9f9f9")
        self.payoffV00.configure(activeforeground="black")
        self.payoffV00.configure(background="#000")
        self.payoffV00.configure(disabledforeground="#a3a3a3")
        self.payoffV00.configure(font="-family {Segoe UI Emoji} -size 28 -weight bold")
        self.payoffV00.configure(foreground="#fff")
        self.payoffV00.configure(highlightbackground="#d9d9d9")
        self.payoffV00.configure(highlightcolor="black")
        self.payoffV00.configure(text=''',''')

        self.payoffFrame01 = tk.Frame(self.payoffMatrixFrame)
        self.payoffFrame01.place(relx=0.478, rely=0.086, relheight=0.331
                , relwidth=0.417)
        self.payoffFrame01.configure(relief='groove')
        self.payoffFrame01.configure(borderwidth="2")
        self.payoffFrame01.configure(relief="groove")
        self.payoffFrame01.configure(background="#000")
        self.payoffFrame01.configure(highlightbackground="#d9d9d9")
        self.payoffFrame01.configure(highlightcolor="black")

        self.payoffEntryL01 = tk.Entry(self.payoffFrame01,justify="center")
        self.payoffEntryL01.place(relx=0.161, rely=0.25, height=42
                , relwidth=0.203)
        self.payoffEntryL01.configure(background=bg_col)
        self.payoffEntryL01.configure(disabledforeground="#a3a3a3")
        self.payoffEntryL01.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryL01.configure(foreground=p1_col)
        self.payoffEntryL01.configure(highlightbackground="#d9d9d9")
        self.payoffEntryL01.configure(highlightcolor=fg_col)
        self.payoffEntryL01.configure(insertbackground=fg_col)
        self.payoffEntryL01.configure(selectbackground="blue")
        self.payoffEntryL01.configure(selectforeground="white")
        self.payoffEntryL01.configure(relief="groove")

        self.payoffEntryR01 = tk.Entry(self.payoffFrame01,justify="center")
        self.payoffEntryR01.place(relx=0.594, rely=0.25, height=42
                , relwidth=0.203)
        self.payoffEntryR01.configure(background=bg_col)
        self.payoffEntryR01.configure(disabledforeground="#a3a3a3")
        self.payoffEntryR01.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryR01.configure(foreground=p2_col)
        self.payoffEntryR01.configure(highlightbackground="#d9d9d9")
        self.payoffEntryR01.configure(highlightcolor="black")
        self.payoffEntryR01.configure(insertbackground=fg_col)
        self.payoffEntryR01.configure(selectbackground="blue")
        self.payoffEntryR01.configure(selectforeground="white")
        self.payoffEntryR01.configure(relief="groove")

        self.payoffLP01 = tk.Label(self.payoffFrame01)
        self.payoffLP01.place(relx=0.051, rely=0.216, height=40, width=16)
        self.payoffLP01.configure(activebackground="#f9f9f9")
        self.payoffLP01.configure(activeforeground="black")
        self.payoffLP01.configure(background="#000")
        self.payoffLP01.configure(disabledforeground="#a3a3a3")
        self.payoffLP01.configure(font="-family {Segoe UI Emoji} -size 22 -weight bold")
        self.payoffLP01.configure(foreground="#fff")
        self.payoffLP01.configure(highlightbackground="#d9d9d9")
        self.payoffLP01.configure(highlightcolor="black")
        self.payoffLP01.configure(text='''(''')

        self.payoffRP01 = tk.Label(self.payoffFrame01)
        self.payoffRP01.place(relx=0.871, rely=0.216, height=40, width=16)
        self.payoffRP01.configure(activebackground="#f9f9f9")
        self.payoffRP01.configure(activeforeground="black")
        self.payoffRP01.configure(background="#000")
        self.payoffRP01.configure(disabledforeground="#a3a3a3")
        self.payoffRP01.configure(font="-family {Segoe UI Emoji} -size 22 -weight bold")
        self.payoffRP01.configure(foreground="#fff")
        self.payoffRP01.configure(highlightbackground="#d9d9d9")
        self.payoffRP01.configure(highlightcolor="black")
        self.payoffRP01.configure(text=''')''')

        self.payoffV01 = tk.Label(self.payoffFrame01)
        self.payoffV01.place(relx=0.433, rely=0.102, height=52, width=28)
        self.payoffV01.configure(activebackground="#f9f9f9")
        self.payoffV01.configure(activeforeground="black")
        self.payoffV01.configure(background="#000")
        self.payoffV01.configure(disabledforeground="#a3a3a3")
        self.payoffV01.configure(font="-family {Segoe UI Emoji} -size 28 -weight bold")
        self.payoffV01.configure(foreground="#fff")
        self.payoffV01.configure(highlightbackground="#d9d9d9")
        self.payoffV01.configure(highlightcolor="black")
        self.payoffV01.configure(text=''',''')

        self.payoffFrame10 = tk.Frame(self.payoffMatrixFrame)
        self.payoffFrame10.place(relx=0.056, rely=0.436, relheight=0.327
                , relwidth=0.417)
        self.payoffFrame10.configure(relief='groove')
        self.payoffFrame10.configure(borderwidth="2")
        self.payoffFrame10.configure(relief="groove")
        self.payoffFrame10.configure(background="#000")
        self.payoffFrame10.configure(highlightbackground="#d9d9d9")
        self.payoffFrame10.configure(highlightcolor="black")

        self.payoffEntryL10 = tk.Entry(self.payoffFrame10,justify="center")
        self.payoffEntryL10.place(relx=0.161, rely=0.25, height=42
                , relwidth=0.203)
        self.payoffEntryL10.configure(background=bg_col)
        self.payoffEntryL10.configure(disabledforeground="#a3a3a3")
        self.payoffEntryL10.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryL10.configure(foreground=p1_col)
        self.payoffEntryL10.configure(highlightbackground="#d9d9d9")
        self.payoffEntryL10.configure(highlightcolor="black")
        self.payoffEntryL10.configure(insertbackground=fg_col)
        self.payoffEntryL10.configure(selectbackground="blue")
        self.payoffEntryL10.configure(selectforeground="white")
        self.payoffEntryL10.configure(relief="groove")

        self.payoffEntryR10 = tk.Entry(self.payoffFrame10,justify="center")
        self.payoffEntryR10.place(relx=0.594, rely=0.25, height=42
                , relwidth=0.203)
        self.payoffEntryR10.configure(background=bg_col)
        self.payoffEntryR10.configure(relief='flat')
        self.payoffEntryR10.configure(disabledforeground="#a3a3a3")
        self.payoffEntryR10.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryR10.configure(foreground=p2_col)
        self.payoffEntryR10.configure(highlightbackground="#d9d9d9")
        self.payoffEntryR10.configure(highlightcolor="black")
        self.payoffEntryR10.configure(insertbackground=fg_col)
        self.payoffEntryR10.configure(selectbackground="blue")
        self.payoffEntryR10.configure(selectforeground="white")
        self.payoffEntryR10.configure(relief="groove")

        self.payoffLP10 = tk.Label(self.payoffFrame10)
        self.payoffLP10.place(relx=0.051, rely=0.207, height=40, width=16)
        self.payoffLP10.configure(activebackground="#f9f9f9")
        self.payoffLP10.configure(activeforeground="black")
        self.payoffLP10.configure(background="#000")
        self.payoffLP10.configure(disabledforeground="#a3a3a3")
        self.payoffLP10.configure(font="-family {Segoe UI Emoji} -size 22 -weight bold")
        self.payoffLP10.configure(foreground="#fff")
        self.payoffLP10.configure(highlightbackground="#d9d9d9")
        self.payoffLP10.configure(highlightcolor="black")
        self.payoffLP10.configure(text='''(''')

        self.payoffRP10 = tk.Label(self.payoffFrame10)
        self.payoffRP10.place(relx=0.871, rely=0.207, height=40, width=16)
        self.payoffRP10.configure(activebackground="#f9f9f9")
        self.payoffRP10.configure(activeforeground="black")
        self.payoffRP10.configure(background="#000")
        self.payoffRP10.configure(disabledforeground="#a3a3a3")
        self.payoffRP10.configure(font="-family {Segoe UI Emoji} -size 22 -weight bold")
        self.payoffRP10.configure(foreground="#fff")
        self.payoffRP10.configure(highlightbackground="#d9d9d9")
        self.payoffRP10.configure(highlightcolor="black")
        self.payoffRP10.configure(text=''')''')

        self.payoffV10 = tk.Label(self.payoffFrame10)
        self.payoffV10.place(relx=0.433, rely=0.103, height=51, width=28)
        self.payoffV10.configure(activebackground="#f9f9f9")
        self.payoffV10.configure(activeforeground="black")
        self.payoffV10.configure(background="#000")
        self.payoffV10.configure(disabledforeground="#a3a3a3")
        self.payoffV10.configure(font="-family {Segoe UI Emoji} -size 28 -weight bold")
        self.payoffV10.configure(foreground="#fff")
        self.payoffV10.configure(highlightbackground="#d9d9d9")
        self.payoffV10.configure(highlightcolor="black")
        self.payoffV10.configure(text=''',''')


        self.payoffFrame11 = tk.Frame(self.payoffMatrixFrame)
        self.payoffFrame11.place(relx=0.478, rely=0.436, relheight=0.327
                , relwidth=0.417)
        self.payoffFrame11.configure(relief='groove')
        self.payoffFrame11.configure(borderwidth="2")
        self.payoffFrame11.configure(relief="groove")
        self.payoffFrame11.configure(background="#000")
        self.payoffFrame11.configure(highlightbackground="#d9d9d9")
        self.payoffFrame11.configure(highlightcolor="black")

        self.payoffEntryL11 = tk.Entry(self.payoffFrame11,justify="center")
        self.payoffEntryL11.place(relx=0.161, rely=0.25, height=42
                , relwidth=0.203)
        self.payoffEntryL11.configure(background=bg_col)
        self.payoffEntryL11.configure(disabledforeground="#a3a3a3")
        self.payoffEntryL11.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryL11.configure(foreground=p1_col)
        self.payoffEntryL11.configure(highlightbackground="#d9d9d9")
        self.payoffEntryL11.configure(highlightcolor="black")
        self.payoffEntryL11.configure(insertbackground=fg_col)
        self.payoffEntryL11.configure(selectbackground="blue")
        self.payoffEntryL11.configure(selectforeground="white")
        self.payoffEntryL11.configure(relief="groove")

        self.payoffEntryR11 = tk.Entry(self.payoffFrame11,justify="center")
        self.payoffEntryR11.place(relx=0.594, rely=0.25, height=42
                , relwidth=0.203)
        self.payoffEntryR11.configure(background=bg_col)
        self.payoffEntryR11.configure(disabledforeground="#a3a3a3")
        self.payoffEntryR11.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryR11.configure(foreground=p2_col)
        self.payoffEntryR11.configure(highlightbackground="#d9d9d9")
        self.payoffEntryR11.configure(highlightcolor="black")
        self.payoffEntryR11.configure(insertbackground=fg_col)
        self.payoffEntryR11.configure(selectbackground="blue")
        self.payoffEntryR11.configure(selectforeground="white")
        self.payoffEntryR11.configure(relief="groove")

        self.payoffLP11 = tk.Label(self.payoffFrame11)
        self.payoffLP11.place(relx=0.051, rely=0.207, height=40, width=16)
        self.payoffLP11.configure(activebackground="#f9f9f9")
        self.payoffLP11.configure(activeforeground="black")
        self.payoffLP11.configure(background="#000")
        self.payoffLP11.configure(disabledforeground="#a3a3a3")
        self.payoffLP11.configure(font="-family {Segoe UI Emoji} -size 22 -weight bold")
        self.payoffLP11.configure(foreground="#fff")
        self.payoffLP11.configure(highlightbackground="#d9d9d9")
        self.payoffLP11.configure(highlightcolor="black")
        self.payoffLP11.configure(text='''(''')

        self.payoffRP11 = tk.Label(self.payoffFrame11)
        self.payoffRP11.place(relx=0.871, rely=0.207, height=40, width=16)
        self.payoffRP11.configure(activebackground="#f9f9f9")
        self.payoffRP11.configure(activeforeground="black")
        self.payoffRP11.configure(background="#000")
        self.payoffRP11.configure(disabledforeground="#a3a3a3")
        self.payoffRP11.configure(font="-family {Segoe UI Emoji} -size 22 -weight bold")
        self.payoffRP11.configure(foreground="#fff")
        self.payoffRP11.configure(highlightbackground="#d9d9d9")
        self.payoffRP11.configure(highlightcolor="black")
        self.payoffRP11.configure(text=''')''')

        self.payoffV11 = tk.Label(self.payoffFrame11)
        self.payoffV11.place(relx=0.433, rely=0.103, height=51, width=28)
        self.payoffV11.configure(activebackground="#f9f9f9")
        self.payoffV11.configure(activeforeground="black")
        self.payoffV11.configure(background="#000")
        self.payoffV11.configure(disabledforeground="#a3a3a3")
        self.payoffV11.configure(font="-family {Segoe UI Emoji} -size 28 -weight bold")
        self.payoffV11.configure(foreground="#fff")
        self.payoffV11.configure(highlightbackground="#d9d9d9")
        self.payoffV11.configure(highlightcolor="black")
        self.payoffV11.configure(text=''',''')


        self.Label1_2 = tk.Label(self.mainFrame)
        self.Label1_2.place(relx=0.01, rely=0.422, height=43, width=78)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#000")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_2.configure(foreground="#1efff3")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''A''')

        self.Label1_2_2 = tk.Label(self.mainFrame)
        self.Label1_2_2.place(relx=0.01, rely=0.625, height=43, width=78)
        self.Label1_2_2.configure(activebackground="#f9f9f9")
        self.Label1_2_2.configure(activeforeground="black")
        self.Label1_2_2.configure(background="#000")
        self.Label1_2_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2_2.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_2_2.configure(foreground="#1efff3")
        self.Label1_2_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2_2.configure(highlightcolor="black")
        self.Label1_2_2.configure(text='''B''')

        self.Label1_2_3 = tk.Label(self.mainFrame)
        self.Label1_2_3.place(relx=0.22, rely=0.25, height=43, width=78)
        self.Label1_2_3.configure(activebackground="#f9f9f9")
        self.Label1_2_3.configure(activeforeground="black")
        self.Label1_2_3.configure(background="#000")
        self.Label1_2_3.configure(disabledforeground="#a3a3a3")
        self.Label1_2_3.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_2_3.configure(foreground="#ff3136")
        self.Label1_2_3.configure(highlightbackground="#d9d9d9")
        self.Label1_2_3.configure(highlightcolor="black")
        self.Label1_2_3.configure(text='''C''')

        self.Label1_2_4 = tk.Label(self.mainFrame)
        self.Label1_2_4.place(relx=0.473, rely=0.25, height=43, width=78)
        self.Label1_2_4.configure(activebackground="#f9f9f9")
        self.Label1_2_4.configure(activeforeground="black")
        self.Label1_2_4.configure(background="#000")
        self.Label1_2_4.configure(disabledforeground="#a3a3a3")
        self.Label1_2_4.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_2_4.configure(foreground="#ff3136")
        self.Label1_2_4.configure(highlightbackground="#d9d9d9")
        self.Label1_2_4.configure(highlightcolor="black")
        self.Label1_2_4.configure(text='''D''')



        self.btnReset = tk.Button(self.mainFrame,cursor="hand2")
        self.btnReset.place(relx=0.720, rely=0.42, height=63, width=136)
        self.btnReset.configure(activebackground="#ececec")
        self.btnReset.configure(activeforeground="#000000")
        self.btnReset.configure(background="#000")
        self.btnReset.configure(disabledforeground="#a3a3a3")
        self.btnReset.configure(font="-family {MV Boli} -size 24")
        self.btnReset.configure(foreground="#ff3d5e")
        self.btnReset.configure(highlightbackground="#d9d9d9")
        self.btnReset.configure(highlightcolor="black")
        self.btnReset.configure(pady="0")
        self.btnReset.configure(relief="groove")
        self.btnReset.configure(text='''Reset''')
        self.btnReset.configure(command= lambda : self.reset())

        self.btnSolve = tk.Button(self.mainFrame,cursor="hand2")
        self.btnSolve.place(relx=0.720, rely=0.62, height=63, width=136)
        self.btnSolve.configure(activebackground="#ececec")
        self.btnSolve.configure(activeforeground="#000000")
        self.btnSolve.configure(background="#000")
        self.btnSolve.configure(disabledforeground="#a3a3a3")
        self.btnSolve.configure(font="-family {MV Boli} -size 24")
        self.btnSolve.configure(foreground="#61ff33")
        self.btnSolve.configure(highlightbackground="#d9d9d9")
        self.btnSolve.configure(highlightcolor="black")
        self.btnSolve.configure(pady="0")
        self.btnSolve.configure(relief="groove")
        self.btnSolve.configure(text='''Solve''')
        self.btnSolve.configure(command= lambda : self.solve())



        self.btnRetour = tk.Button(self.mainFrame,cursor="hand2")
        self.btnRetour.place(relx=0.031, rely=0.916, height=40, width=145)
        self.btnRetour.configure(activebackground="#ff3d5e")
        self.btnRetour.configure(activeforeground="#000000")
        self.btnRetour.configure(background="#000")
        self.btnRetour.configure(disabledforeground="#a3a3a3")
        self.btnRetour.configure(font="-family {MV Boli} -size 20")
        self.btnRetour.configure(foreground="#ff3d5e")
        self.btnRetour.configure(highlightbackground="#d9d9d9")
        self.btnRetour.configure(highlightcolor="black")
        self.btnRetour.configure(pady="0")
        self.btnRetour.configure(relief="groove")
        self.btnRetour.configure(text='''Go Back''')
        self.btnRetour.configure(command=lambda: controller.show_frame("WelcomePage"))

        self.resultLabel = tk.Label(self.mainFrame,justify="center")
        self.resultLabel.place(relx=0.25, rely=0.06, height=80)
        self.resultLabel.configure(activebackground="#ff3d5e")
        self.resultLabel.configure(activeforeground="#000000")
        self.resultLabel.configure(background="#000")
        self.resultLabel.configure(disabledforeground="#a3a3a3")
        self.resultLabel.configure(font="-family {MV Boli} -size 18")
        self.resultLabel.configure(foreground="#0aff80")
        self.resultLabel.configure(highlightbackground="#d9d9d9")
        self.resultLabel.configure(highlightcolor="black")
        self.resultLabel.configure(pady="0")
        self.resultLabel.configure(relief="flat")
        self.resultLabel.configure(text='''''')


