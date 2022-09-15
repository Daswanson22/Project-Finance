import tkinter as tk

class Page(tk.Frame):
    '''
       Create 6 different pages.
           - Login, Sign Up -> Enter info page, Dashboard, Account Summary, Add Transaction, Del/Edit Transaction
       Create a container for each page frame.
       We have seven classes. First is the App class, where we have initialized the 6 frames and defined a function show_frame which is called every time the user clicks on a button.
       The StartPage is simple with two buttons to go to Page 1 and Page 2.
       Page 1 has two buttons, One for Page 2 and another to return to Start Page.
       Page 2 also has two buttons, one for Page 1 and others to return to StartPage.
       This is a simplistic application of navigating between Tkinter frames.
       This can be used as a boilerplate for more complex applications and several features can be added.
       '''
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class AccountView(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       # --------------- Title label -----------------
       self.config(background="#1A1D1A")
       label_title = tk.Label(self,
                           text="Get Your Money Right",
                           font=("Bangers", 25, "bold"),
                           fg="#39FF14",
                           bg="#1A1D1A",
                           relief="raised",
                           padx=0,
                           pady=0,
                           bd=False,
                           )
       label_title.place(x=15, y=20)
       # --------------- Deposit label -----------------
       self.label_deposit = Label(self
                                  ,
                                  text='Deposit amount:',
                                  font=('Arial', self.base_font_size, 'bold'),
                                  fg=self.color[3],
                                  bg="#1A1D1A",
                                  relief=RAISED,
                                  padx=0,
                                  pady=0,
                                  bd=False, )
       self.label_deposit.place(x=20, y=150)

class Page2(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 2")
       label.pack(side="top", fill="both", expand=True)

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        av = AccountView(self)
        # p2 = Page2(self)

        # buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        # buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        av.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        # p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # b1 = tk.Button(buttonframe, text="Page 1", command=av.lift)
        # b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)

        # b1.pack(side="left")
        # b2.pack(side="left")

        av.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1300x700")
    icon = tk.PhotoImage(file="moneylogo.png")
    root.iconphoto(True, icon)
    root.title("Get Your Money Right")
    root.mainloop()

