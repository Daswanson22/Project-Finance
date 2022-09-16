import tkinter as tk
from tkinter import *
from tkinter import ttk

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class AddTransactionView(Page):
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
        Page.__init__(self, *args, **kwargs)
        self.config(background="#1A1D1A")
        self.count = 0
        self.networth = 0
        self.base_font_size = 16
        self.header_font_size = 26
    #                  Gray    Darker Green   Dark Green   LGB      Grey-Blue     Red     Bright Green  Gray-Green   Tan      Black
        self.color = ["#1A1D1A", "#03120E", "#26413C", "#638092", "#8AB0AB", "#F27272", "#78FA58", "#629d62", "#c9a736", "#000000"]
        self.total_rows = 0
        self.total_cols = 4
        self.x = ((1300/2) - 183)
        # self.NAVBAR()
        self.display_entryBox()
        self.display_labels()

        # ------------------- Confirm Buttons --------------------
        self.button_confirm = tk.Button(self,
                                text="Confirm",
                                command=self.confirm_command,
                                font=("Cosmic Sans", 25),
                                fg=self.color[3],
                                bg=self.color[1],
                                padx=2,
                                pady=2,
                                width=19,
                                activeforeground=self.color[6],
                                activebackground="black",
                                state=tk.NORMAL)
        self.button_confirm.place(x=self.x, y=600, height=70, width=365)
    def NAVBAR(self):
        # --------------- Title label -----------------
        self.navFrame = tk.Frame(self,
                             bg="black",
                             bd=10,
                             relief=FLAT)
        self.navFrame.place(x=0, y=0, height=100, width=1300)
        self.nav_frame_bd = tk.Frame(self.navFrame,
                                  bg=self.color[7],
                                  bd=10,
                                  relief=FLAT)
        self.nav_frame_bd.place(x=-10, y=87, height=3, width=1300)
        self.label_title = tk.Label(self.navFrame,
                               text="Get Your Money Right",
                               font=("Bangers", 25, "bold"),
                               fg="#39FF14",
                               bg="black",
                               relief="raised",
                               padx=0,
                               pady=0,
                               bd=False,
                               )
        self.label_title.pack(side=LEFT)
        # SubFrame allows us to stack the Login and Settings button on top of each other
        self.subFrame = Frame(self.navFrame,
                              bg="black",
                              bd=False)
        self.subFrame.pack(side=RIGHT, padx=20)
        self.loginNAVbtn = tk.Button(self.subFrame,
                                     text="Login",
                                     font=("Bangers", self.base_font_size),
                                     fg="#39FF14",
                                     bg="black",
                                     bd=False,
                                     pady=5
                                     )
        self.loginNAVbtn.pack(side=TOP, fill=BOTH)
        self.settingsNAVbtn = tk.Button(self.subFrame,
                                     text="Settings",
                                     font=("Bangers", self.base_font_size),
                                     fg="#39FF14",
                                     bg="black",
                                     bd=False,
                                     pady=5
                                        )
        self.settingsNAVbtn.pack(side=TOP, fill=BOTH)

        self.delNAVbtn = tk.Button(self.navFrame,
                                   text="Del Transaction",
                                   font=("Bangers", self.base_font_size),
                                   fg="#39FF14",
                                   bg="black",
                                   bd=False,
                                   padx=20, pady=26)
        self.delNAVbtn.pack(side=RIGHT)
        self.addNAVbtn = tk.Button(self.navFrame,
                                   text="Add Transaction",
                                   font=("Bangers", self.base_font_size),
                                   fg="#39FF14",
                                   bg="black",
                                   bd=False,
                                   padx=20, pady=26)
        self.addNAVbtn.pack(side=RIGHT)
        self.dashNAVbtn = tk.Button(self.navFrame,
                                   text="Dashboard",
                                   font=("Bangers", self.base_font_size),
                                   fg="#39FF14",
                                   bg="black",
                                   bd=False,
                                   padx=20, pady=26)
        self.dashNAVbtn.pack(side=RIGHT)

        # menubar = Menu(root)

    def display_labels(self):
        # --------------- Add Trans label -----------------
        self.frame_addTransLbl = tk.Frame(self,
                                          bg=self.color[8],
                                          bd=3,
                                          relief=FLAT)
        self.frame_addTransLbl.place(x=self.x, y=110)
       # --------------- Deposit label -----------------
        self.label_AddTransaction = tk.Label(self.frame_addTransLbl,
                                             text="Add Transaction",
                                             font=("Arial", self.header_font_size),
                                             fg=self.color[3],
                                             bg="#1A1D1A",
                                             bd=3,
                                             justify=CENTER,
                                             padx=51,
                                             )
        self.label_AddTransaction.pack()
       # --------------- Deposit label -----------------
        self.label_deposit = tk.Label(self,
                                  text='Deposit amount:',
                                  font=('Arial', self.base_font_size),
                                  fg=self.color[6],
                                  bg="#1A1D1A",
                                  relief="raised",
                                  padx=0,
                                  pady=0,
                                  bd=False, )
        self.label_deposit.place(x=self.x, y=150)
        # Displays 'Correct' or 'Incorrect' to the right of deposit label
        self.answer_label_deposit = tk.Label(self,
                                          text='',
                                          font=('Arial', self.base_font_size),
                                          fg=self.color[6],
                                          bg="#1A1D1A",
                                          relief="raised",
                                          padx=0,
                                          pady=0,
                                          bd=False,
                                          )
        self.answer_label_deposit.place(x=self.x + 250, y=150)

        # --------------- Received From label -----------------
        self.label_from = tk.Label(self,
                                text=("Recieved From: "),
                                font=('Arial', self.base_font_size),
                                fg=self.color[6],
                                bg="#1A1D1A",
                                relief="raised",
                                padx=0,
                                pady=0,
                                bd=False)
        self.label_from.place(x=self.x, y=230)

        # --------------- Date label -----------------
        self.label_date = tk.Label(self,
                                text=("Date: "),
                                font=('Arial', self.base_font_size),
                                fg=self.color[6],
                                bg="#1A1D1A",
                                relief="raised",
                                padx=0,
                                pady=0,
                                bd=False)
        self.label_date.place(x=self.x, y=310)

        # --------------- Additional Info label -----------------
        self.label_additional = tk.Label(self,
                                      text=("Additional Information: "),
                                      font=('Arial', self.base_font_size),
                                      fg=self.color[6],
                                      bg="#1A1D1A",
                                      relief="raised",
                                      padx=0,
                                      pady=0,
                                      bd=False)
        self.label_additional.place(x=self.x, y=390)

    def display_entryBox(self):
       # ------------------- Deposit Entry --------------------
       self.entry_deposit = tk.Entry(self,
                                  font=("Cosmic Sans", self.base_font_size),
                                  fg=self.color[9],
                                  bg="#353b35",
                                  bd=3,
                                  cursor="spraycan",
                                  relief=FLAT
                                  )
       self.entry_deposit.place(x=self.x, y=180, height=40, width=365)
       # ------------------- Received From Entry --------------------
       self.entry_from = tk.Entry(self,
                                font=("Cosmic Sans", self.base_font_size),
                                fg=self.color[4],
                                bg="#353b35",
                                bd=3,
                                cursor="spraycan",
                                relief=FLAT
                                )
       self.entry_from.place(x=self.x, y=260, height=40, width=365)
       # ------------------- Date Entry --------------------
       self.entry_date = tk.Entry(self,
                                font=("Cosmic Sans", self.base_font_size),
                                fg=self.color[4],
                                bg="#353b35",
                                bd=3,
                                cursor="spraycan",
                                relief=FLAT
                                )
       self.entry_date.place(x=self.x, y=340, height=40, width=365)
       # ------------------- Additional Info Entry --------------------
       self.entry_additional = tk.Text(self,
                                    font=("Cosmic Sans", self.base_font_size),
                                    # command=click_entry,
                                    fg=self.color[4],
                                    bg="#353b35",
                                    padx=5,
                                    pady=5,
                                    bd=3,
                                    relief=FLAT,
                                    cursor="spraycan"
                                    )
       self.entry_additional.place(x=self.x, y=420, height=150, width=365)
       # --------------------- END of Entry --------------------


    # if not, prints incorrect value then deletes entry
    def validate_entry(self):
        """Function will check if input value is an integer,
        if not, prints incorrect value then deletes entry"""
        try:
            int(self.entry_deposit.get())
            self.answer_label_deposit.config(text='Correct Input', fg=self.color[6])
        except ValueError:
            self.messagebox.showwarning(title="Incorrect input",
                                        message="Please input numerical characters ONLY into the deposit entry line.")
            self.answer_label_deposit.config(text='', fg=self.color[6])

    def delete_entries(self):
        # delete the entries
        self.entry_deposit.delete(0, END)
        self.entry_from.delete(0, END)
        self.entry_date.delete(0, END)
        self.entry_additional.delete("1.0", END) #works

    def confirm_command(self):
        # global networth
        self.validate_entry()

        self.deposit = int(self.entry_deposit.get())
        self.sender = self.entry_from.get()
        self.date = self.entry_date.get()
        self.additionalInput = self.entry_additional.get("1.0", END)
        # --------------------------------
        # This goes into DashboardView at some point, need to hook up SQL first.
        self.count += 1
        # Inputs the new data into the treeview
        # self.tv.insert(parent='', index=self.count, iid=str(self.count), values=(self.count, self.entry_date.get(), self.entry_from.get(), self.entry_deposit.get(), self.entry_additional.get("1.0", END)))
        # --------------------------------
        # Allows deposit to become and integer value
        self.networth = self.networth + self.deposit
        print("Deposit = $" + str(
            self.deposit) + "\nSender = " + self.sender + "\nDate = " + self.date + "\nAdditional Input = " + self.additionalInput)
        self.delete_entries()
        return self.networth, self.sender


class DashboardView(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       # ------------------- Data Table --------------------
       #       When confirm button is pressed... create new transaction log line.
       #           - Call a new function to be created
       #           - parameters(date, received from, deposit amount, additional info,
       #           - type of transaction(deposit or withdraw), associated number,
       #           - Rows: infinite, Cols (5): #, date, from, deposit, additional info
       self.config(background="#1A1D1A")
       self.count = 0
       self.networth = 0
       self.base_font_size = 16
       self.header_font_size = 26
       #                  Gray    Darker Green   Dark Green   LGB      Grey-Blue     Red     Bright Green  Gray-Green   Tan      Black
       self.color = ["#1A1D1A", "#03120E", "#26413C", "#638092", "#8AB0AB", "#F27272", "#78FA58", "#629d62", "#c9a736",
                     "#000000"]
       self.total_rows = 0
       self.total_cols = 4
       self.x = ((1300 / 2) - 183)
       """trans_log_frame = Frame(self, bg='black', bd=5, relief=SUNKEN)
       trans_log_frame.place(x=550, y=160)
       self.tv = ttk.Treeview(
           trans_log_frame,
           columns=(1, 2, 3, 4, 5),
           show='headings',
           height=10,
           style="mystyle.Treeview"
       )
       self.tv.heading(1, text='#')
       self.tv.heading(2, text='Date')
       self.tv.heading(3, text='Received From')
       self.tv.heading(4, text='Amount')
       self.tv.heading(5, text='Info')

       self.tv.pack()
       style = ttk.Style()
       style.theme_use("default")
       style.map("Treeview")
       # Inputs the new data into the treeview
       self.tv.insert(parent='', index=self.count, iid=str(self.count), values=(
       self.count, self.entry_date.get(), self.entry_from.get(), self.entry_deposit.get(),
       self.entry_additional.get("1.0", END)))"""

       # This frame contains the labels for networth, p/Yr, p/Mo, p/Day
       frame = Frame(self, bg='black', bd=5, relief=SUNKEN)
       frame.place(x=550, y=20)

       # --------------- Networth label -----------------
       self.label_networth = Label(frame,
                                   text='Networth = $0.0',
                                   font=('Bangers', self.base_font_size - 2, 'bold'),
                                   fg=self.color[3],
                                   bg='BLACK',
                                   relief=RAISED,
                                   # padx=5,
                                   # pady=5,
                                   bd=FALSE)
       self.label_networth.pack(side=TOP, padx=10, pady=2)

       # --------------- Income p/Yr label -----------------
       self.label_perYr = Label(frame,
                                text='Income p/yr = $0.0',
                                font=('Bangers', self.base_font_size - 2, 'bold'),
                                fg=self.color[3],
                                bg='BLACK',
                                relief=RAISED,
                                # padx=5,
                                # pady=5,
                                bd=FALSE)
       self.label_perYr.pack(side=TOP, padx=10, pady=2)

       # --------------- Income p/Mo label -----------------
       self.label_perMonth = Label(frame,
                                   text='Income p/mo = $0.0',
                                   font=('Bangers', self.base_font_size - 2, 'bold'),
                                   fg=self.color[3],
                                   bg='BLACK',
                                   relief=RAISED,
                                   # padx=5,
                                   # pady=5,
                                   bd=FALSE)
       self.label_perMonth.pack(side=TOP, padx=10, pady=2)

       # --------------- Income p/Day label -----------------
       self.label_perDay = Label(frame,
                                 text='Income p/day = $0.0',
                                 font=('Bangers', self.base_font_size - 2, 'bold'),
                                 fg=self.color[3],
                                 bg='BLACK',
                                 relief=RAISED,
                                 # padx=5,
                                 # pady=5,
                                 bd=FALSE)
       self.label_perDay.pack(side=TOP, padx=10, pady=2)
       # ------------------- END of Labels --------------------
       # Updates the value of Label_networth
       self.label_networth.config(text=f'Networth = ${self.networth:,}')
       self.label_perYr.config(text=f'Income p/Yr = ${self.networth:,}')
       self.label_perMonth.config(text=f'Income p/Mo = ${(round((self.networth / 12), 2)):,}')
       self.label_perDay.config(text=f'Income p/Day = ${(round((self.networth / 365), 2)):,}')

class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        # Calls for the page
        av = AddTransactionView(self)
        db = DashboardView(self)
        # p2 = Page2(self)

        # buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        # buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)
        av.NAVBAR()

        av.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        db.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        # b1 = tk.Button(buttonframe, text="Page 1", command=av.lift)
        # b2 = tk.Button(buttonframe, text="Page 2", command=p2.lift)

        # b1.pack(side="left")
        # b2.pack(side="left")

        # How do I change from page to page?
        # If a button on the navbar is clicked then show
        # av.show()
        db.show()

if __name__ == "__main__":
    root = tk.Tk()
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("1300x700")
    root.resizable(0,0)
    icon = tk.PhotoImage(file="moneylogo.png")
    root.iconphoto(True, icon)
    root.title("Get Your Money Right")
    root.mainloop()

