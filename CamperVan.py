from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class CamperVan_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("CAMPING TRIPS BOOKING APPLICATION")
        self.root.geometry("1295x550+230+220")

        # =============variables==============
        self.var_campervan_id = StringVar()
        self.var_campervan_type = StringVar()
        self.var_status = StringVar()

        # =================title=========
        lbl_title = Label(self.root, text="CAMPER VAN DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # ===========Labelframe+++++====
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Camper Van Details",
                                    font=("arial", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=590)

        # ===========labels and entries++++++++++++
        # camper van name
        cvname = Label(labelframeleft, text="Camper Van ID:", font=("arial", 12, "bold"), padx=2, pady=6)
        cvname.grid(row=1, column=0, sticky=W)

        txtcvname = ttk.Entry(labelframeleft, textvariable=self.var_campervan_id, width=25, font=("arial", 12, "bold"))
        txtcvname.grid(row=1, column=1)

        # camper van type
        cvtype = Label(labelframeleft, text="Camper Van Type:", font=("arial", 12, "bold"), padx=2, pady=6)
        cvtype.grid(row=2, column=0, sticky=W)

        combo_cvtype = ttk.Combobox(labelframeleft, textvariable=self.var_campervan_type, font=("arial", 12, "bold"), width=25, state="readonly")
        combo_cvtype["value"] = ("Small", "Medium",  "Large")
        combo_cvtype.current(0)
        combo_cvtype.grid(row=2, column=1)

        # status
        status = Label(labelframeleft, text="Status:", font=("arial", 12, "bold"), padx=2, pady=6)
        status.grid(row=3, column=0, sticky=W)

        combo_status = ttk.Combobox(labelframeleft, textvariable=self.var_status, width=25, font=("arial", 12, "bold"), state="readonly")
        combo_status["value"] = ("Booked", "NotBooked")
        combo_status.current(1)
        combo_status.grid(row=3, column=1)

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
        combo_combo_search["value"] = "campervan_type"
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

        self.CVan_Details_Table = ttk.Treeview(details_table,
                                               column=("campervan_id", "campervan_type", "status"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.CVan_Details_Table.xview)
        scroll_y.config(command=self.CVan_Details_Table.yview)

        self.CVan_Details_Table.heading("campervan_id", text="CamperVan ID")
        self.CVan_Details_Table.heading("campervan_type", text="CamperVan Type")
        self.CVan_Details_Table.heading("status", text="Status")

        self.CVan_Details_Table["show"] = "headings"

        self.CVan_Details_Table.column("campervan_id", width=100)
        self.CVan_Details_Table.column("campervan_type", width=100)
        self.CVan_Details_Table.column("status", width=100)

        self.CVan_Details_Table.pack(fill=BOTH, expand=1)
        self.CVan_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_campervan_type.get() == "":
            messagebox.showerror("Error", "All fields are required to be filled", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="pierre",
                                               database="SolemCampers")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO CamperVan VALUES(%s,%s,%s)", (
                    self.var_campervan_id.get(),
                    self.var_campervan_type.get(),
                    self.var_status.get()

                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "CamperVan has been added!", parent=self.root)

            except Exception as es:

                messagebox.showwarning("Warning", f"oops!Something went wrong!!!:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM CamperVan ")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.CVan_Details_Table.delete(*self.CVan_Details_Table.get_children())
            for i in rows:
                self.CVan_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.CVan_Details_Table.focus()
        content = self.CVan_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_campervan_id.set(row[0]),
        self.var_campervan_type.set(row[1]),
        self.var_status.set(row[2])

    def update(self):
        if self.var_campervan_type.get() == "":
            messagebox.showerror("Error", "Please enter the type of campervan ", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "Update campervan set campervan_id=%s,campervan_type=%s,status=%s WHERE Ref=%s",
                (

                    self.var_campervan_id.get(),
                    self.var_campervan_type.get(),
                    self.var_status.get(),

                ))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("update", "campervan  details have been updated in success", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Camping Trips Booking Application", "Do you want to delete this customer ",
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
            my_cursor = conn.cursor()
            query = "delete from campervan where Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_ref.set(""),
        self.var_campervan_id.set(""),
        self.var_campervan_type(""),
        self.var_status.set(""),

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM campervan WHERE " + str(self.search_var.get()) + " LIKE '%" + str(
            self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.CVan_Details_Table.get_children())
            for i in rows:
                self.CVan_Details_Table.insert("", END, values=i)
                conn.commit()
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = CamperVan_Win(root)
    root.mainloop()

