from tkinter import *
from PIL import Image, ImageTk
from customer import Cust_Win
from campingsite import CampSite_Win
from CamperVan import CamperVan_Win
from customerbookings import CustBooking_Win


class CampTripBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CAMPING TRIPS BOOKING APPLICATION")
        self.root.geometry("1550x800+0+0")

        # =================1st image=========
        img1 = Image.open("CampersImages/cool.png")
        img1 = img1.resize((1550, 140), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1500, height=140)

        # =================logo=========
        img2 = Image.open("CampersImages/logo.png")
        img2 = img2.resize((230, 140), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        # =================title=========
        lbl_title = Label(self.root, text="CAMPING TRIPS BOOKING APPLICATION", font=("times new roman", 40, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        # =================main frame=========
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        # =================menu=========
        lbl_menu = Label(main_frame, text="Menu", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4,
                         relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # =================btn frame=========
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details, width=22,
                          font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=1)

        csite_btn = Button(btn_frame, text="CAMPING SITES", command=self.CSite_details, width=22,
                          font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        csite_btn.grid(row=1, column=0, pady=1)

        cvan_btn = Button(btn_frame, text="CAMPERVAN", command=self.CVan_details, width=22,
                             font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        cvan_btn.grid(row=2, column=0, pady=1)

        custbook_btn = Button(btn_frame, text="CUSTOMER BOOKINGS", command=self.CustBookings_details, width=22, font=("times new roman", 14, "bold"), bg="black",
                            fg="gold", bd=0, cursor="hand2")
        custbook_btn.grid(row=3, column=0, pady=1)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout, width=22,
                            font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand2")
        logout_btn.grid(row=4, column=0, pady=1)

        # ============right side image=============
        img3 = Image.open("CampersImages/bg.jpg")
        img3 = img3.resize((1310, 590), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

        # ==================down images==================
        img4 = Image.open("CampersImages/c1.jpg")
        img4 = img4.resize((220, 190), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg2 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg2.place(x=0, y=225, width=230, height=210)

        img5 = Image.open("CampersImages/c2.jpg")
        img5 = img5.resize((220, 190), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg3 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg3.place(x=0, y=420, width=230, height=190)

    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)

    def CVan_details(self):
        self.new_window = Toplevel(self.root)
        self.app = CamperVan_Win(self.new_window)

    def CSite_details(self):
        self.new_window = Toplevel(self.root)
        self.app = CampSite_Win(self.new_window)

    def CustBookings_details(self):
        self.new_window = Toplevel(self.root)
        self.app = CustBooking_Win(self.new_window)

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = CampTripBookingApp(root)
    root.mainloop()



