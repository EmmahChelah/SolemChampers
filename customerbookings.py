from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class CustBooking_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("CAMPING TRIPS BOOKING APPLICATION")
        self.root.geometry("1295x550+230+220")

        # =============variables==============
        self.var_id_number = StringVar()
        self.var_campervan_type = StringVar()
        self.var_camp_id = StringVar()
        # =================title=========
        lbl_title = Label(self.root, text="CUSTOMER BOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # =================logo=========
        img1 = Image.open(r"CampersImages/c.jpg")
        img1 = img1.resize((430, 780), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=60, width=430, height=780)

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
        combo_combo_search["value"] = "id_number"
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
        details_table.place(x=0,y=50,width=860,height=780)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.CustBookings_Details_Table = ttk.Treeview(details_table,
                                                       column=("id_number", "campervan_type", "camp_id"),
                                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.CustBookings_Details_Table.xview)
        scroll_y.config(command=self.CustBookings_Details_Table.yview)

        self.CustBookings_Details_Table.heading("id_number", text="CIDNumber")
        self.CustBookings_Details_Table.heading("campervan_type", text="CVanType")
        self.CustBookings_Details_Table.heading("camp_id", text="CSiteID")

        self.CustBookings_Details_Table["show"] = "headings"

        self.CustBookings_Details_Table.column("id_number", width=20)
        self.CustBookings_Details_Table.column("campervan_type", width=20)
        self.CustBookings_Details_Table.column("camp_id", width=20)

        self.CustBookings_Details_Table.pack(fill=BOTH, expand=1)
        self.CustBookings_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT customer.id_number, campervan.campervan_type,campsite.camp_id "
                          "FROM customer INNER JOIN campervan ON customer.id_number = campervan.id_number"
                          " INNER JOIN campsite ON customer.id_number = campsite.id_number")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.CustBookings_Details_Table.delete(*self.CustBookings_Details_Table.get_children())
            for i in rows:
                self.CustBookings_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.CustBookings_Details_Table.focus()
        content = self.CustBookings_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_id_number.set(row[0]),
        self.var_campervan_type.set(row[1]),
        self.var_camp_id.set(row[2])

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT campervan.campervan_type,campsite.camp_id,customer.id_number",
                          " FROM customer JOIN campervan ON customer.id_number = campervan.id_number ",
                          "JOIN campsite ON campsite.camp_id = customer.id_number" + str(self.search_var.get() + " LIKE '%" + str(self.txt_search.get()) + "%'"))
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.CustBookings_Details_Table.delete(*self.CustBookings_Details_Table.get_children())
            for i in rows:
                self.CustBookings_Details_Table.insert("", END, values=i)
                conn.commit()
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = CustBooking_Win(root)
    root.mainloop()

