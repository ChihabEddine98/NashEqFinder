import tkinter as tk


class PureNEPage(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="#000")


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
        self.titleLabel.place(relx=0.284, rely=0.241, height=34, width=382)
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

        self.payoffFrame_1 = tk.Frame(self.payoffMatrixFrame)
        self.payoffFrame_1.place(relx=0.056, rely=0.086, relheight=0.331
                , relwidth=0.417)
        self.payoffFrame_1.configure(relief='groove')
        self.payoffFrame_1.configure(borderwidth="2")
        self.payoffFrame_1.configure(relief="groove")
        self.payoffFrame_1.configure(background="#000")
        self.payoffFrame_1.configure(highlightbackground="#d9d9d9")
        self.payoffFrame_1.configure(highlightcolor="black")

        self.payoffEntryL00 = tk.Entry(self.payoffFrame_1)
        self.payoffEntryL00.place(relx=0.161, rely=0.318, height=32
                , relwidth=0.203)
        self.payoffEntryL00.configure(background="white")
        self.payoffEntryL00.configure(disabledforeground="#a3a3a3")
        self.payoffEntryL00.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryL00.configure(foreground="#000000")
        self.payoffEntryL00.configure(highlightbackground="#d9d9d9")
        self.payoffEntryL00.configure(highlightcolor="black")
        self.payoffEntryL00.configure(insertbackground="black")
        self.payoffEntryL00.configure(selectbackground="blue")
        self.payoffEntryL00.configure(selectforeground="white")

        self.payoffEntryR00 = tk.Entry(self.payoffFrame_1)
        self.payoffEntryR00.place(relx=0.594, rely=0.318, height=32
                , relwidth=0.203)
        self.payoffEntryR00.configure(background="white")
        self.payoffEntryR00.configure(disabledforeground="#a3a3a3")
        self.payoffEntryR00.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryR00.configure(foreground="#000000")
        self.payoffEntryR00.configure(highlightbackground="#d9d9d9")
        self.payoffEntryR00.configure(highlightcolor="black")
        self.payoffEntryR00.configure(insertbackground="black")
        self.payoffEntryR00.configure(selectbackground="blue")
        self.payoffEntryR00.configure(selectforeground="white")

        self.Label1_3 = tk.Label(self.payoffFrame_1)
        self.Label1_3.place(relx=0.051, rely=0.216, height=33, width=16)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#000")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_3.configure(foreground="#fff")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''(''')

        self.Label1_1_1 = tk.Label(self.payoffFrame_1)
        self.Label1_1_1.place(relx=0.871, rely=0.216, height=33, width=16)
        self.Label1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1.configure(activeforeground="black")
        self.Label1_1_1.configure(background="#000")
        self.Label1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_1_1.configure(foreground="#fff")
        self.Label1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1.configure(highlightcolor="black")
        self.Label1_1_1.configure(text=''')''')

        self.Label1_2_1 = tk.Label(self.payoffFrame_1)
        self.Label1_2_1.place(relx=0.433, rely=0.102, height=52, width=28)
        self.Label1_2_1.configure(activebackground="#f9f9f9")
        self.Label1_2_1.configure(activeforeground="black")
        self.Label1_2_1.configure(background="#000")
        self.Label1_2_1.configure(disabledforeground="#a3a3a3")
        self.Label1_2_1.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_2_1.configure(foreground="#fff")
        self.Label1_2_1.configure(highlightbackground="#d9d9d9")
        self.Label1_2_1.configure(highlightcolor="black")
        self.Label1_2_1.configure(text=''',''')

        self.payoffFrame_1_1 = tk.Frame(self.payoffMatrixFrame)
        self.payoffFrame_1_1.place(relx=0.478, rely=0.086, relheight=0.331
                , relwidth=0.417)
        self.payoffFrame_1_1.configure(relief='groove')
        self.payoffFrame_1_1.configure(borderwidth="2")
        self.payoffFrame_1_1.configure(relief="groove")
        self.payoffFrame_1_1.configure(background="#000")
        self.payoffFrame_1_1.configure(highlightbackground="#d9d9d9")
        self.payoffFrame_1_1.configure(highlightcolor="black")

        self.payoffEntryL01 = tk.Entry(self.payoffFrame_1_1)
        self.payoffEntryL01.place(relx=0.161, rely=0.318, height=32
                , relwidth=0.203)
        self.payoffEntryL01.configure(background="white")
        self.payoffEntryL01.configure(disabledforeground="#a3a3a3")
        self.payoffEntryL01.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryL01.configure(foreground="#000000")
        self.payoffEntryL01.configure(highlightbackground="#d9d9d9")
        self.payoffEntryL01.configure(highlightcolor="black")
        self.payoffEntryL01.configure(insertbackground="black")
        self.payoffEntryL01.configure(selectbackground="blue")
        self.payoffEntryL01.configure(selectforeground="white")

        self.payoffEntryR01 = tk.Entry(self.payoffFrame_1_1)
        self.payoffEntryR01.place(relx=0.594, rely=0.318, height=32
                , relwidth=0.203)
        self.payoffEntryR01.configure(background="white")
        self.payoffEntryR01.configure(disabledforeground="#a3a3a3")
        self.payoffEntryR01.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.payoffEntryR01.configure(foreground="#000000")
        self.payoffEntryR01.configure(highlightbackground="#d9d9d9")
        self.payoffEntryR01.configure(highlightcolor="black")
        self.payoffEntryR01.configure(insertbackground="black")
        self.payoffEntryR01.configure(selectbackground="blue")
        self.payoffEntryR01.configure(selectforeground="white")

        self.Label1_3_1 = tk.Label(self.payoffFrame_1_1)
        self.Label1_3_1.place(relx=0.051, rely=0.216, height=33, width=16)
        self.Label1_3_1.configure(activebackground="#f9f9f9")
        self.Label1_3_1.configure(activeforeground="black")
        self.Label1_3_1.configure(background="#000")
        self.Label1_3_1.configure(disabledforeground="#a3a3a3")
        self.Label1_3_1.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_3_1.configure(foreground="#fff")
        self.Label1_3_1.configure(highlightbackground="#d9d9d9")
        self.Label1_3_1.configure(highlightcolor="black")
        self.Label1_3_1.configure(text='''(''')

        self.Label1_1_1_1 = tk.Label(self.payoffFrame_1_1)
        self.Label1_1_1_1.place(relx=0.871, rely=0.216, height=33, width=16)
        self.Label1_1_1_1.configure(activebackground="#f9f9f9")
        self.Label1_1_1_1.configure(activeforeground="black")
        self.Label1_1_1_1.configure(background="#000")
        self.Label1_1_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_1.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_1_1_1.configure(foreground="#fff")
        self.Label1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_1.configure(highlightcolor="black")
        self.Label1_1_1_1.configure(text=''')''')

        self.Label1_2_1_1 = tk.Label(self.payoffFrame_1_1)
        self.Label1_2_1_1.place(relx=0.433, rely=0.102, height=52, width=28)
        self.Label1_2_1_1.configure(activebackground="#f9f9f9")
        self.Label1_2_1_1.configure(activeforeground="black")
        self.Label1_2_1_1.configure(background="#000")
        self.Label1_2_1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_2_1_1.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_2_1_1.configure(foreground="#fff")
        self.Label1_2_1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_2_1_1.configure(highlightcolor="black")
        self.Label1_2_1_1.configure(text=''',''')

        self.payoffFrame_1_2 = tk.Frame(self.payoffFrame_1_1)
        self.payoffFrame_1_2.place(relx=0.493, rely=1.852, relheight=1.0
                , relwidth=1.0)
        self.payoffFrame_1_2.configure(relief='groove')
        self.payoffFrame_1_2.configure(borderwidth="2")
        self.payoffFrame_1_2.configure(relief="groove")
        self.payoffFrame_1_2.configure(background="#d9d9d9")
        self.payoffFrame_1_2.configure(highlightbackground="#d9d9d9")
        self.payoffFrame_1_2.configure(highlightcolor="black")

        self.payoffEntry00_1_2 = tk.Entry(self.payoffFrame_1_2)
        self.payoffEntry00_1_2.place(relx=0.161, rely=0.318, height=24
                , relwidth=0.203)
        self.payoffEntry00_1_2.configure(background="white")
        self.payoffEntry00_1_2.configure(disabledforeground="#a3a3a3")
        self.payoffEntry00_1_2.configure(font="TkFixedFont")
        self.payoffEntry00_1_2.configure(foreground="#000000")
        self.payoffEntry00_1_2.configure(highlightbackground="#d9d9d9")
        self.payoffEntry00_1_2.configure(highlightcolor="black")
        self.payoffEntry00_1_2.configure(insertbackground="black")
        self.payoffEntry00_1_2.configure(selectbackground="blue")
        self.payoffEntry00_1_2.configure(selectforeground="white")

        self.payoffEntry01_1_2 = tk.Entry(self.payoffFrame_1_2)
        self.payoffEntry01_1_2.place(relx=0.594, rely=0.318, height=24
                , relwidth=0.203)
        self.payoffEntry01_1_2.configure(background="white")
        self.payoffEntry01_1_2.configure(disabledforeground="#a3a3a3")
        self.payoffEntry01_1_2.configure(font="TkFixedFont")
        self.payoffEntry01_1_2.configure(foreground="#000000")
        self.payoffEntry01_1_2.configure(highlightbackground="#d9d9d9")
        self.payoffEntry01_1_2.configure(highlightcolor="black")
        self.payoffEntry01_1_2.configure(insertbackground="black")
        self.payoffEntry01_1_2.configure(selectbackground="blue")
        self.payoffEntry01_1_2.configure(selectforeground="white")

        self.Label1_3_2 = tk.Label(self.payoffFrame_1_2)
        self.Label1_3_2.place(relx=0.051, rely=0.216, height=33, width=16)
        self.Label1_3_2.configure(activebackground="#f9f9f9")
        self.Label1_3_2.configure(activeforeground="black")
        self.Label1_3_2.configure(background="#d9d9d9")
        self.Label1_3_2.configure(disabledforeground="#a3a3a3")
        self.Label1_3_2.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_3_2.configure(foreground="#000000")
        self.Label1_3_2.configure(highlightbackground="#d9d9d9")
        self.Label1_3_2.configure(highlightcolor="black")
        self.Label1_3_2.configure(text='''(''')

        self.Label1_1_1_2 = tk.Label(self.payoffFrame_1_2)
        self.Label1_1_1_2.place(relx=0.871, rely=0.216, height=33, width=16)
        self.Label1_1_1_2.configure(activebackground="#f9f9f9")
        self.Label1_1_1_2.configure(activeforeground="black")
        self.Label1_1_1_2.configure(background="#d9d9d9")
        self.Label1_1_1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_2.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_1_1_2.configure(foreground="#000000")
        self.Label1_1_1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_2.configure(highlightcolor="black")
        self.Label1_1_1_2.configure(text=''')''')

        self.Label1_2_1_2 = tk.Label(self.payoffFrame_1_2)
        self.Label1_2_1_2.place(relx=0.433, rely=0.102, height=52, width=28)
        self.Label1_2_1_2.configure(activebackground="#f9f9f9")
        self.Label1_2_1_2.configure(activeforeground="black")
        self.Label1_2_1_2.configure(background="#d9d9d9")
        self.Label1_2_1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2_1_2.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_2_1_2.configure(foreground="#000000")
        self.Label1_2_1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2_1_2.configure(highlightcolor="black")
        self.Label1_2_1_2.configure(text=''',''')

        self.payoffFrame_1_4 = tk.Frame(self.payoffMatrixFrame)
        self.payoffFrame_1_4.place(relx=0.478, rely=0.436, relheight=0.327
                , relwidth=0.417)
        self.payoffFrame_1_4.configure(relief='groove')
        self.payoffFrame_1_4.configure(borderwidth="2")
        self.payoffFrame_1_4.configure(relief="groove")
        self.payoffFrame_1_4.configure(background="#000")
        self.payoffFrame_1_4.configure(highlightbackground="#d9d9d9")
        self.payoffFrame_1_4.configure(highlightcolor="black")

        self.payoffEntryL11 = tk.Entry(self.payoffFrame_1_4)
        self.payoffEntryL11.place(relx=0.161, rely=0.31, height=24
                , relwidth=0.203)
        self.payoffEntryL11.configure(background="white")
        self.payoffEntryL11.configure(disabledforeground="#a3a3a3")
        self.payoffEntryL11.configure(font="TkFixedFont")
        self.payoffEntryL11.configure(foreground="#000000")
        self.payoffEntryL11.configure(highlightbackground="#d9d9d9")
        self.payoffEntryL11.configure(highlightcolor="black")
        self.payoffEntryL11.configure(insertbackground="black")
        self.payoffEntryL11.configure(selectbackground="blue")
        self.payoffEntryL11.configure(selectforeground="white")

        self.payoffEntryR11 = tk.Entry(self.payoffFrame_1_4)
        self.payoffEntryR11.place(relx=0.594, rely=0.31, height=24
                , relwidth=0.203)
        self.payoffEntryR11.configure(background="white")
        self.payoffEntryR11.configure(disabledforeground="#a3a3a3")
        self.payoffEntryR11.configure(font="TkFixedFont")
        self.payoffEntryR11.configure(foreground="#000000")
        self.payoffEntryR11.configure(highlightbackground="#d9d9d9")
        self.payoffEntryR11.configure(highlightcolor="black")
        self.payoffEntryR11.configure(insertbackground="black")
        self.payoffEntryR11.configure(selectbackground="blue")
        self.payoffEntryR11.configure(selectforeground="white")

        self.Label1_3_4 = tk.Label(self.payoffFrame_1_4)
        self.Label1_3_4.place(relx=0.051, rely=0.207, height=33, width=16)
        self.Label1_3_4.configure(activebackground="#f9f9f9")
        self.Label1_3_4.configure(activeforeground="black")
        self.Label1_3_4.configure(background="#000")
        self.Label1_3_4.configure(disabledforeground="#a3a3a3")
        self.Label1_3_4.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_3_4.configure(foreground="#fff")
        self.Label1_3_4.configure(highlightbackground="#d9d9d9")
        self.Label1_3_4.configure(highlightcolor="black")
        self.Label1_3_4.configure(text='''(''')

        self.Label1_1_1_4 = tk.Label(self.payoffFrame_1_4)
        self.Label1_1_1_4.place(relx=0.871, rely=0.207, height=33, width=16)
        self.Label1_1_1_4.configure(activebackground="#f9f9f9")
        self.Label1_1_1_4.configure(activeforeground="black")
        self.Label1_1_1_4.configure(background="#000")
        self.Label1_1_1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_4.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_1_1_4.configure(foreground="#fff")
        self.Label1_1_1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_4.configure(highlightcolor="black")
        self.Label1_1_1_4.configure(text=''')''')

        self.Label1_2_1_4 = tk.Label(self.payoffFrame_1_4)
        self.Label1_2_1_4.place(relx=0.433, rely=0.103, height=51, width=28)
        self.Label1_2_1_4.configure(activebackground="#f9f9f9")
        self.Label1_2_1_4.configure(activeforeground="black")
        self.Label1_2_1_4.configure(background="#000")
        self.Label1_2_1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_2_1_4.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_2_1_4.configure(foreground="#fff")
        self.Label1_2_1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_2_1_4.configure(highlightcolor="black")
        self.Label1_2_1_4.configure(text=''',''')

        self.payoffFrame_1_3 = tk.Frame(self.payoffMatrixFrame)
        self.payoffFrame_1_3.place(relx=0.056, rely=0.436, relheight=0.327
                , relwidth=0.417)
        self.payoffFrame_1_3.configure(relief='groove')
        self.payoffFrame_1_3.configure(borderwidth="2")
        self.payoffFrame_1_3.configure(relief="groove")
        self.payoffFrame_1_3.configure(background="#000")
        self.payoffFrame_1_3.configure(highlightbackground="#d9d9d9")
        self.payoffFrame_1_3.configure(highlightcolor="black")

        self.payoffEntryL10 = tk.Entry(self.payoffFrame_1_3)
        self.payoffEntryL10.place(relx=0.161, rely=0.31, height=24
                , relwidth=0.203)
        self.payoffEntryL10.configure(background="white")
        self.payoffEntryL10.configure(disabledforeground="#a3a3a3")
        self.payoffEntryL10.configure(font="TkFixedFont")
        self.payoffEntryL10.configure(foreground="#000000")
        self.payoffEntryL10.configure(highlightbackground="#d9d9d9")
        self.payoffEntryL10.configure(highlightcolor="black")
        self.payoffEntryL10.configure(insertbackground="black")
        self.payoffEntryL10.configure(selectbackground="blue")
        self.payoffEntryL10.configure(selectforeground="white")

        self.payoffEntryR10 = tk.Entry(self.payoffFrame_1_3)
        self.payoffEntryR10.place(relx=0.594, rely=0.31, height=24
                , relwidth=0.203)
        self.payoffEntryR10.configure(background="white")
        self.payoffEntryR10.configure(disabledforeground="#a3a3a3")
        self.payoffEntryR10.configure(font="TkFixedFont")
        self.payoffEntryR10.configure(foreground="#000000")
        self.payoffEntryR10.configure(highlightbackground="#d9d9d9")
        self.payoffEntryR10.configure(highlightcolor="black")
        self.payoffEntryR10.configure(insertbackground="black")
        self.payoffEntryR10.configure(selectbackground="blue")
        self.payoffEntryR10.configure(selectforeground="white")

        self.Label1_3_3 = tk.Label(self.payoffFrame_1_3)
        self.Label1_3_3.place(relx=0.051, rely=0.207, height=33, width=16)
        self.Label1_3_3.configure(activebackground="#f9f9f9")
        self.Label1_3_3.configure(activeforeground="black")
        self.Label1_3_3.configure(background="#000")
        self.Label1_3_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3_3.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_3_3.configure(foreground="#fff")
        self.Label1_3_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3_3.configure(highlightcolor="black")
        self.Label1_3_3.configure(text='''(''')

        self.Label1_1_1_3 = tk.Label(self.payoffFrame_1_3)
        self.Label1_1_1_3.place(relx=0.871, rely=0.207, height=33, width=16)
        self.Label1_1_1_3.configure(activebackground="#f9f9f9")
        self.Label1_1_1_3.configure(activeforeground="black")
        self.Label1_1_1_3.configure(background="#000")
        self.Label1_1_1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_1_1_3.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_1_1_3.configure(foreground="#fff")
        self.Label1_1_1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_1_1_3.configure(highlightcolor="black")
        self.Label1_1_1_3.configure(text=''')''')

        self.Label1_2_1_3 = tk.Label(self.payoffFrame_1_3)
        self.Label1_2_1_3.place(relx=0.433, rely=0.103, height=51, width=28)
        self.Label1_2_1_3.configure(activebackground="#f9f9f9")
        self.Label1_2_1_3.configure(activeforeground="black")
        self.Label1_2_1_3.configure(background="#000")
        self.Label1_2_1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_2_1_3.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_2_1_3.configure(foreground="#fff")
        self.Label1_2_1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_2_1_3.configure(highlightcolor="black")
        self.Label1_2_1_3.configure(text=''',''')

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
        self.Label1_2_3.place(relx=0.22, rely=0.222, height=43, width=78)
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
        self.Label1_2_4.place(relx=0.473, rely=0.222, height=43, width=78)
        self.Label1_2_4.configure(activebackground="#f9f9f9")
        self.Label1_2_4.configure(activeforeground="black")
        self.Label1_2_4.configure(background="#000")
        self.Label1_2_4.configure(disabledforeground="#a3a3a3")
        self.Label1_2_4.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1_2_4.configure(foreground="#ff3136")
        self.Label1_2_4.configure(highlightbackground="#d9d9d9")
        self.Label1_2_4.configure(highlightcolor="black")
        self.Label1_2_4.configure(text='''D''')

        self.Label1 = tk.Label(self.mainFrame)
        self.Label1.place(relx=0.297, rely=0.06, height=52, width=153)
        self.Label1.configure(background="#000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI Emoji} -size 20 -weight bold")
        self.Label1.configure(foreground="#ff3136")
        self.Label1.configure(text='''Player II''')

        self.Button1 = tk.Button(self.mainFrame)
        self.Button1.place(relx=0.738, rely=0.543, height=63, width=136)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#000")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {MV Boli} -size 22")
        self.Button1.configure(foreground="#61ff33")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(relief="groove")
        self.Button1.configure(text='''Solve''')