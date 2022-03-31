from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("CAMPING TRIPS BOOKING APPLICATION")
        self.root.geometry("1295x550+230+220")

        # =============variables==============
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_gender = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_id_number = StringVar()
        self.var_campervan_id = StringVar()
        self.var_camp_id = StringVar()

        # =================title=========
        lbl_title = Label(self.root, text="CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # =================logo=========
        # img2 = Image.open(r"images/logo.png")
        # img2 = img2.resize((100, 40), Image.ANTIALIAS)
        # self.photoimg2 = ImageTk.PhotoImage(img2)

        # lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        # lblimg.place(x=5, y=2, width=100, height=40)

        # ===========Labelframe+++++====
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                    font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=590)

        # ===========labels and entries++++++++++++
        # customer ref
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=29, font=("arial", 13, "bold"),
                              state="readonly")
        entry_ref.grid(row=0, column=1)

        # cust name
        cname = Label(labelframeleft, text="Customer Name:", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, width=29, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # gender combobox
        lbl_gender = Label(labelframeleft, text="Gender:", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_gender.grid(row=2, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=27,
                                    state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current(2)
        combo_gender.grid(row=2, column=1)

        # mobile no
        lblMobile = Label(labelframeleft, text="Mobile No:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=3, column=0, sticky=W)

        txtMobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"))
        txtMobile.grid(row=3, column=1)

        # email
        lblEmail = Label(labelframeleft, text="Email:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=4, column=0, sticky=W)

        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        txtEmail.grid(row=4, column=1)

        # nationality
        lblNationality = Label(labelframeleft, text="Nationality:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=5, column=0, sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality, font=("arial", 12, "bold"),
                                         width=27, state="readonly")
        combo_nationality["value"] = ("American", "Indian", "Jew", "African")
        combo_nationality.current(0)
        combo_nationality.grid(row=5, column=1)

        # id number
        lblIdNumber = Label(labelframeleft, text="Id Number:", font=("arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=6, column=0, sticky=W)

        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number, width=29, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=6, column=1)

        # campervan id
        campvid = Label(labelframeleft, text="CamperVan ID:", font=("arial", 12, "bold"), padx=2, pady=6)
        campvid.grid(row=7, column=0, sticky=W)

        txtcampvid = ttk.Entry(labelframeleft, textvariable=self.var_campervan_id, width=29, font=("arial", 13, "bold"))
        txtcampvid.grid(row=7, column=1)

        # campsite id
        csid = Label(labelframeleft, text="CampSite ID:", font=("arial", 12, "bold"), padx=2, pady=6)
        csid.grid(row=8, column=0, sticky=W)

        txtcsid = ttk.Entry(labelframeleft, textvariable=self.var_camp_id, width=29, font=("arial", 13, "bold"))
        txtcsid.grid(row=8, column=1)

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
        combo_combo_search["value"] = ("Mobile", "Ref")
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

        self.Cust_Details_Table = ttk.Treeview(details_table,
                                               column=("ref", "cust_name", "gender", "mobile", "email",
                                                       "nationality", "id_number", "campervan_id", "camp_id"),
                                               xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("cust_name", text="Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("id_number", text="Id Number")
        self.Cust_Details_Table.heading("campervan_id", text="CamperVan ID")
        self.Cust_Details_Table.heading("camp_id", text="CampSit ID")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("cust_name", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("id_number", width=100)
        self.Cust_Details_Table.column("campervan_id", width=100)
        self.Cust_Details_Table.column("camp_id", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_id_number.get() == "":
            messagebox.showerror("Error", "All fields are required to be filled", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="pierre",
                                               database="SolentCampers")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO customer VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_gender.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_number.get(),
                    self.var_campervan_id.get(),
                    self.var_camp_id.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added!", parent=self.root)

            except Exception as es:

                messagebox.showwarning("Warning", f"oops!Something went wrong!!!:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer ")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_mobile.set(row[3]),
        self.var_email.set(row[4]),
        self.var_nationality.set(row[5]),
        self.var_id_number.set(row[6]),
        self.var_campervan_id.set(row[7]),
        self.var_camp_id.set(row[8])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile no", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "Update customer set cust_name=%s,gender=%s,mobile=%s,email=%s,nationality=%s,id_number=%s,campervan_id=%s,camp_id=%s WHERE Ref=%s",
                (

                    self.var_cust_name.get(),
                    self.var_gender.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_number.get(),
                    self.var_ref.get(),
                    self.var_campervan_id.get(),
                    self.var_camp_id.get()
                ))

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("update", "Customer details have been updated in success", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Camping Trips Booking Application", "Do you want to delete this customer ",
                                      parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
            my_cursor = conn.cursor()
            query = "delete from customer where ref=%s"
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
        self.var_cust_name.set(""),
        self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set(""),
        self.var_id_number.set("")
        self.var_campervan_id.set("")
        self.var_camp_id.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="pierre", database="SolentCampers")
        my_cursor = conn.cursor()

        my_cursor.execute("SELECT * FROM customer WHERE " + str(self.search_var.get()) + " LIKE '%" + str(
            self.txt_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
                conn.commit()
            conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()

