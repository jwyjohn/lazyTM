import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import time
from joinmeeting import *


class timerTM():
    def __init__(self):
        self.state = "Edit"
        self.cid = ""
        self.pwd = ""
        self.eta = ""

        self.root = tk.Tk()
        self.root.title("lazyTM")
        self.root.resizable(0, 0)

        self.label_cid = tk.Label(text="Course ID", font=('Fixedsys'))
        self.label_cid.grid(column=0, row=0)
        self.input_cid = tk.Entry(self.root, width=11, font=('Fixedsys'))
        self.input_cid.grid(column=5, row=0)

        self.label_pwd = tk.Label(text="Password ", font=('Fixedsys'))
        self.label_pwd.grid(column=0, row=1)
        self.input_pwd = tk.Entry(self.root, width=11, font=('Fixedsys'))
        self.input_pwd.grid(column=5, row=1)

        self.label_timeset = tk.Label(text="Enter at ", font=('Fixedsys'))
        self.label_timeset.grid(column=0, row=2)
        self.preset = ttk.Combobox(self.root, values=tuple(
            ["07:50:00", "09:50:00", "13:20:00", "15:20:00", "18:50:00"]), width=7, state='readonly')
        self.preset.current(0)
        self.preset.grid(column=5, row=2)

        self.commit_btn = tk.Button(
            self.root, text="Commit", font=('Fixedsys'), command=self.commit)
        self.commit_btn.grid(column=0, row=4)

        self.label_nowtime = tk.Label(text="", font=('Fixedsys'))
        self.label_nowtime.grid(column=0, row=5)

        # self.label_eta = tk.Label(text="[E 00:00:00]", font=('Fixedsys'))
        self.label_eta = tk.Label(text="[Not commit]", font=('Fixedsys'))
        self.label_eta.grid(column=5, row=5)

        self.update_clock()
        self.root.mainloop()

    def update_clock(self):
        now = time.strftime("%H:%M:%S")
        self.label_nowtime.configure(text="[N {}]".format(now))
        if self.state == "Committed":
            if now[:5] == self.eta[:5]:
                try:
                    enter_meeting(self.cid, self.pwd, "mewo~")
                except:
                    messagebox.showerror("Fatal", "Failed entering meeting..")
                self.root.destroy()
        self.root.after(500, self.update_clock)

    def commit(self):
        self.input_cid.configure(state='readonly')
        self.input_pwd.configure(state='readonly')
        self.commit_btn.configure(state='disabled')
        self.preset.configure(state='disabled')

        try:
            self.state = "Committed"
            self.cid = self.input_cid.get().strip(' ')
            self.pwd = self.input_pwd.get().strip(' ')
            self.eta = self.preset.get().strip(' ')
            self.label_eta.configure(text="[E {}]".format(self.eta))

            messagebox.showinfo("Info", "Timer set at {} enter cid={} with pwd={}".format(
                self.eta, self.cid, self.pwd))
        except:
            messagebox.showerror("Fatal", "Unknown Err, quitting..")
            self.root.destroy()


app = timerTM()
