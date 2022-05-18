import tkinter as tk


class WelcomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        font13 = "-family {Tw Cen MT} -size 18"
        font14 = "-family {Tw Cen MT} -size 22"

        self.configure(background="#000")

        self.Frame1 = tk.Frame(self)
        self.Frame1.place(relx=0.034, rely=0.182, relheight=0.549
                          , relwidth=0.529)
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#000")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=-0.064, rely=0.275, height=74, width=368)
        self.Label1.configure(background="#000000")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font13)
        self.Label1.configure(foreground="#fff")
        self.Label1.configure(text='''2x2 Nash Equiliberia ''')

        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.278, rely=0.441, height=44, width=233)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#000")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font=font14)
        self.Label1_1.configure(foreground="#00ff00")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Solver''')

        self.Frame2 = tk.Frame(self)
        self.Frame2.place(relx=0.566, rely=0.242, relheight=0.514
                          , relwidth=0.292)
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#000")

        self.btnPureNE = tk.Button(self.Frame2)
        self.btnPureNE.place(relx=0.078, rely=0.059, height=53, width=206)
        self.btnPureNE.configure(activebackground="#80ff00")
        self.btnPureNE.configure(activeforeground="#000000")
        self.btnPureNE.configure(background="#000")
        self.btnPureNE.configure(borderwidth="3")
        self.btnPureNE.configure(cursor="hand2")
        self.btnPureNE.configure(disabledforeground="#a3a3a3")
        self.btnPureNE.configure(font=font13)
        self.btnPureNE.configure(foreground="#000")
        self.btnPureNE.configure(highlightbackground="#ffff00")
        self.btnPureNE.configure(highlightcolor="black")
        self.btnPureNE.configure(pady="0")
        self.btnPureNE.configure(relief="ridge")
        self.btnPureNE.configure(text='''Pure NE''')
        self.btnPureNE.configure(command=lambda: controller.show_frame("PureNEPage"))

        self.btnMixedNE = tk.Button(self.Frame2)
        self.btnMixedNE.place(relx=0.078, rely=0.265, height=53, width=206)
        self.btnMixedNE.configure(activebackground="#80ff00")
        self.btnMixedNE.configure(activeforeground="#000000")
        self.btnMixedNE.configure(background="#000000")
        self.btnMixedNE.configure(borderwidth="3")
        self.btnMixedNE.configure(disabledforeground="#a3a3a3")
        self.btnMixedNE.configure(font=font13)
        self.btnMixedNE.configure(foreground="#000")
        self.btnMixedNE.configure(highlightbackground="#d9d9d9")
        self.btnMixedNE.configure(highlightcolor="black")
        self.btnMixedNE.configure(pady="0")
        self.btnMixedNE.configure(relief="ridge")
        self.btnMixedNE.configure(text='''Mixed NE''')
        self.btnMixedNE.configure(command= lambda : controller.show_frame("MixedNEPage"))
        self.btnMixedNE.configure(cursor="hand2")



        self.btnAiONE = tk.Button(self.Frame2)
        self.btnAiONE.place(relx=0.078, rely=0.471, height=53, width=206)
        self.btnAiONE.configure(activebackground="#80ff00")
        self.btnAiONE.configure(activeforeground="#000000")
        self.btnAiONE.configure(background="#000")
        self.btnAiONE.configure(borderwidth="3")
        self.btnAiONE.configure(disabledforeground="#a3a3a3")
        self.btnAiONE.configure(font=font13)
        self.btnAiONE.configure(foreground="#000")
        self.btnAiONE.configure(highlightbackground="#d9d9d9")
        self.btnAiONE.configure(highlightcolor="black")
        self.btnAiONE.configure(pady="0")
        self.btnAiONE.configure(relief="ridge")
        self.btnAiONE.configure(text='''AiO''')
        self.btnAiONE.configure(command= lambda : controller.show_frame("AiOPage"))
        self.btnAiONE.configure(cursor="hand2")

        self.btnAiONE = tk.Button(self.Frame2)
        self.btnAiONE.place(relx=0.078, rely=0.672, height=53, width=206)
        self.btnAiONE.configure(activebackground="#80ff00")
        self.btnAiONE.configure(activeforeground="#000000")
        self.btnAiONE.configure(background="#000")
        self.btnAiONE.configure(borderwidth="3")
        self.btnAiONE.configure(disabledforeground="#a3a3a3")
        self.btnAiONE.configure(font=font13)
        self.btnAiONE.configure(foreground="#000")
        self.btnAiONE.configure(highlightbackground="#d9d9d9")
        self.btnAiONE.configure(highlightcolor="black")
        self.btnAiONE.configure(pady="0")
        self.btnAiONE.configure(relief="ridge")
        self.btnAiONE.configure(text='''Pure_3x3''')
        self.btnAiONE.configure(command= lambda : controller.show_frame("Pure3x3NEPage"))
        self.btnAiONE.configure(cursor="hand2")