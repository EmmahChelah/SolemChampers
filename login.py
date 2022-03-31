from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox
import datetime
import time
from CampTripBookingApplication import CampTripBookingApp


def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.var_username = StringVar()
        self.var_password = StringVar()

        img = Image.open(r"CampersImages/c5.jpg")
        img = img.resize((1430, 800), Image.ANTIALIAS)
        self.bg = ImageTk.PhotoImage(img)

        lblimg = Label(image=self.bg, borderwidth=0)
        lblimg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=430)

        img2 = Image.open(r"CampersImages/lock6.png")
        img2 = img2.resize((90, 90), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img2)

        lblimg1 = Label(image=self.photoimg1, borderwidth=0)
        lblimg1.place(x=740, y=180, width=90, height=90)

        get_str = Label(frame, text="Get Started", font=("times new roman", 15, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=85)

        # label
        username = lbl = Label(frame, text="Username", font=("times new roman", 12, "bold"), fg="white", bg="black")
        username.place(x=70, y=125)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=150, width=270)

        password = lbl = Label(frame, text="Password", font=("times new roman", 12, "bold"), fg="white", bg="black")
        password.place(x=70, y=195)

        self.txtpass = ttk.Entry(frame, show='*', font=("times new roman", 15, "bold"))
        self.txtpass.place(x=40, y=220, width=270)

        # icon images
        img2 = Image.open(r"CampersImages/lock6.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg1 = Label(image=self.photoimg2, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=293, width=25, height=25)

        img3 = Image.open(r"CampersImages/lock6.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(image=self.photoimg3, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=363, width=25, height=25)

        # login button
        btn_login = Button(frame, text="Login", command=self.login, font=("times new roman", 12, "bold"),
                           bg="light green", borderwidth=3, relief=RIDGE)
        btn_login.place(x=110, y=270, width=120, height=35)

    def login(self):

        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "Fill all fields")
        elif self.txtuser.get() == "admin" and self.txtpass.get() == "admin":
            messagebox.showinfo("Success", "Welcome to Solent Campers Booking Application")

            if self.txtuser.get() == "admin" and self.txtpass.get() == "admin":
                self.new_window = Toplevel(self.root)
                self.app = CampTripBookingApp(self.new_window)
            else:
                if not self.txtuser.get() == "admin" and self.txtpass.get() == "admin":
                    return


if __name__ == "__main__":
    root = Tk()
    obj = Login_Window(root)
    root.mainloop()