from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class CampSite_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("CAMPING TRIPS BOOKING APPLICATION")
        self.root.geometry("1295x550+230+220")

        # =============variables==============
        self.var_camp_id = StringVar()
        self.var_camp_name = StringVar()
        self.var_location = StringVar()
        self.var_activity = StringVar()
        self.var_cost = StringVar()
        self.var_camping_period = StringVar()
        self.var_status = StringVar()
        self.var_id_number = StringVar()

        # =================title=========
        lbl_title = Label(self.root, text="CAMPING SITE DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # =================logo=========
        #img2 = Image.open(r"images/logo.png")
        #img2 = img2.resize((100, 40), Image.ANTIALIAS)
        #self.photoimg2 = ImageTk.PhotoImage(img2)

        #lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        #lblimg.place(x=5, y=2, width=100, height=40)

        # ===========Labelframe+++++====
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Camping Site Details",
                                    font=("arial", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=590)

        # ===========labels and entries++++++++++++
        # camp site id
        csid = Label(labelframeleft, text="CampSite ID:", font=("arial", 12, "bold"), padx=2, pady=6)
        csid.grid(row=1, column=0, sticky=W)

        txtcsid = ttk.Entry(labelframeleft, textvariable=self.var_camp_id, width=26, font=("arial", 12, "bold"))
        txtcsid.grid(row=1, column=1)

        # camp site name
        csname = Label(labelframeleft, text="CampSite Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        csname.grid(row=2, column=0, sticky=W)

        txtcsname = ttk.Entry(labelframeleft, textvariable=self.var_camp_name, width=26, font=("arial", 12, "bold"))
        txtcsname.grid(row=2, column=1)

        # camp site location
        cslocation = Label(labelframeleft, text="Location:", font=("arial", 12, "bold"), padx=2, pady=6)
        cslocation.grid(row=3, column=0, sticky=W)

        txtcslocation = ttk.Entry(labelframeleft, textvariable=self.var_location, width=26, font=("arial", 12, "bold"))
        txtcslocation.grid(row=3, column=1)

        # camp site activity
        csactivity = Label(labelframeleft, text="Activity:", font=("arial", 12, "bold"), padx=2, pady=6)
        csactivity.grid(row=4, column=0, sticky=W)

        txtcsactivity = ttk.Entry(labelframeleft, textvariable=self.var_activity, width=26, font=("arial", 12, "bold"))
        txtcsactivity.grid(row=4, column=1)

        # camp site Cost
        cscost = Label(labelframeleft, text="Cost:", font=("arial", 12, "bold"), padx=2, pady=6)
        cscost.grid(row=5, column=0, sticky=W)

        txtcscost = ttk.Entry(labelframeleft, textvariable=self.var_cost, width=26, font=("arial", 12, "bold"))
        txtcscost.grid(row=5, column=1)

        # camp site Camping period
        csperiod = Label(labelframeleft, text="Camping Period:", font=("arial", 12, "bold"), padx=2, pady=6)
        csperiod.grid(row=6, column=0, sticky=W)

        txtcsperiod = ttk.Entry(labelframeleft, textvariable=self.var_camping_period, width=26, font=("arial", 12, "bold"))
        txtcsperiod.grid(row=6, column=1)

        # Status
        status = Label(labelframeleft, text="Status:", font=("arial", 12, "bold"), padx=2, pady=6)
        status.grid(row=7, column=0, sticky=W)

        combo_status = ttk.Combobox(labelframeleft, textvariable=self.var_status, width=26, font=("arial", 12, "bold"),
                                          state="readonly")
        combo_status["value"] = ("Booked", "NotBooked")
        combo_status.current(1)
        combo_status.grid(row=7, column=1)

        # customer id number
        custID = Label(labelframeleft, text="CustomerID:", font=("arial", 12, "bold"), padx=2, pady=6)
        custID.grid(row=8, column=0, sticky=W)

        txtcustID = ttk.Entry(labelframeleft, textvariable=self.var_id_number, width=26, font=("arial", 12, "bold"))
        txtcustID.grid(row=8, column=1)

        # ==============btns=====================
        btn_Frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_Frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_Frame, text="Add", command=self.add_data, font=("arial", 11, "bold"), bg="black", fg="gold",
                        width=10)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_Frame, text="Update", command=self.update, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_Frame, text="Delete", command=self.mDelete, font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_Frame, text="Reset", command=self.reset, font=("arial", 11, "bold"), bg="black",
                          fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # ==============table frame of the search system=====================
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System",
                                 font=("arial", 11, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, text="Search By", font=("arial", 12, "bold"), bg="red", fg="white", padx=2,
                            pady=6)
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_combo_search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"),
                                          width=24, state="readonly")
        combo_combo_search["value"] = "location"
        combo_combo_search.current(0)
        combo_combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, command=self.search, text="Search", font=("arial", 11, "bold"), bg="black",
                           fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, command=self.fetch_data, text="Show All", font=("arial", 11, "bold"),
                            bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # ++++++++++++++++++Show data table================
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.CSite_Details_Table = ttk.Treeview(details_table,
                                                column=("camp_id", "camp_name", "location", "activity", "cost", "camping_period", "status", "id_number"),
                                                xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.CSite_Details_Table.xview)
        scroll_y.config(command=self.CSite_Details_Table.yview)

        self.CSite_Details_Table.heading("camp_id", text="Camp ID")
        self.CSite_Details_Table.heading("camp_name", text="Camp Name")
        self.CSite_Details_Table.heading("location", text="Location")
        self.CSite_Details_Table.heading("activity", text="Activity")
        self.CSite_Details_Table.heading("cost", text="Cost")
        self.CSite_Details_Table.heading("camping_period", text="Camping Period")
        self.CSite_Details_Table.heading("status", text="Status")
        self.CSite_Details_Table.heading("id_number", text="CustomerID")

        self.CSite_Details_Table["show"] = "headings"

        self.CSite_Details_Table.column("camp_id", width=100)
        self.CSite_Details_Table.column("camp_name", width=100)
        self.CSite_Details_Table.column("location", width=100)
        self.CSite_Details_Table.column("activity", width=100)
        self.CSite_Details_Table.column("cost", width=100)
        self.CSite_Details_Table.column("camping_period", width=100)
        self.CSite_Details_Table.column("status", width=100)
        self.CSite_Details_Table.column("id_number", width=100)

        self.CSite_Details_Table.pack(fill=BOTH, expand=1)
        self.CSite_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_location.get() == "":
            messagebox.showerror("Error", "All fields are required to be filled", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="pierre",
                                               database="SolentCampers")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO CampSite VALUES(%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_camp_id.get(),
                    self.var_camp_name.get(),
                    self.var_location.get(),
                    self.var_activity.get(),
                    self.var_cost.get(),
                    self.var_camping_period.get(),
                    self.var_status.get(),
                    self.var_id_number.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Camp Site has been added!", parent=self.root)

            except Exception as es:

                messagebox.showwarning("Warning", f"oops!Something went wrong!!!:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM CampSite ")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.CSite_Details_Table.delete(*self.CSite_Details_Table.get_children())
            for i in rows:
                self.CSite_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.CSite_Details_Table.focus()
        content = self.CSite_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_camp_id.set(row[0]),
        self.var_camp_name.set(row[1]),
        self.var_location.get(row[2]),
        self.var_activity.get(row[3]),
        self.var_cost.get(row[4]),
        self.var_camping_period.get(row[5]),
        self.var_status.get(row[6]),
        self.var_id_number.get(row[7])

    def update(self):
        global conn
        if self.var_location.get() == "":
            messagebox.showerror("Error", "Please enter the location of camp site ", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "Update CampSite set camp_id=%s,camp_name=%s,location=%s,activity=%s,cost=%s,camping_period=%s,status=%s WHERE Ref=%s",
                (

                    self.var_camp_id.get(),
                    self.var_camp_name.get(),
                    self.var_location.get(),
                    self.var_activity.get(),
                    self.var_cost.get(),
                    self.var_camping_period.get(),
                    self.var_status.get(),
                    self.var_id_number.get()

                ))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("update", "Camp Site  details have been updated in success", parent=self.root)

    def mDelete(self):
        global conn
        mDelete = messagebox.askyesno("Camping Trips Booking Application", "Do you want to delete this camp site ",
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
            my_cursor = conn.cursor()
            query = "delete from CampSite where camp_id=%s"
            value = (self.var_camp_id.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set(""),
        self.var_camp_id.set(""),
        self.var_camp_name.set(""),
        self.var_location.set(""),
        self.var_activity.set(""),
        self.var_cost.set(""),
        self.var_camping_period.set(""),
        self.var_status.set("")
        self.var_id_number.set("")

    def search(self):
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM CampSite WHERE " + str(self.search_var.get()) + " LIKE '%" + str(
            self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.CSite_Details_Table.delete(*self.CSite_Details_Table.get_children())
            for i in rows:
                self.CSite_Details_Table.insert("", END, values=i)
                conn.commit()
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = CampSite_Win(root)
    root.mainloop()

