from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import mysql.connector
from datetime import datetime


class Roombooking:
    def __init__(self, root, scroll_y=None):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1297x580+230+220")

# ==========================VARIABLES CONTACT=================================================
        self.var_contact = StringVar()
        self.var_check_in_date = StringVar()
        self.var_check_out_date = StringVar()
        self.var_roomtype = StringVar()
        self.var_available_room = StringVar()
        self.var_meal = StringVar()
        self.var_no_of_days = IntVar()
# money fields as DoubleVar
        self.var_paid_tax = DoubleVar()
        self.var_sub_total = DoubleVar()
        self.var_total_cost = DoubleVar()

        # ========================title===============================================================
        lbl_title = Label(self.root, text="ROOM BOOKING DETAILS", font=("times new roman", 20, "bold"), bg="black",
                          fg="gold", bd=0, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1400, height=50)
        # ===========================logo=================================================================

        try:
            img2 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel management system\images\logo.jpg")
            img2 = img2.resize((150, 80), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            lblimg.place(x=0, y=0, width=100, height=50)
        except Exception:
            # If image not found, ignore to allow GUI to run
            pass

        # ===============================  label frame  ========================================================
        labelframeleft = LabelFrame(self.root, text="ROOM BOOKING :- DETAILS ", bd=2, relief=RIDGE,
                                   font=("times new roman", 12, "bold"))
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # =========================labels and entry ======================================================
        lbl_Contact = Label(labelframeleft, text="Customer Contact :", font=("times new roman", 17, "bold"), padx=3,
                            pady=7)
        lbl_Contact.grid(row=0, column=0, sticky=W)
        enty_Contact = Entry(labelframeleft, textvariable=self.var_contact, width=15,
                             font=("times new roman", 12, "bold"), bd=4, relief=RIDGE, )
        enty_Contact.grid(row=0, column=1, sticky=W)

        btnFetchdata = Button(labelframeleft, command=self.fectch_contact, text="Fetch Data", font=("arial", 10, "bold"),
                              bg="red", fg="gold", relief=RIDGE, width=8)
        btnFetchdata.place(x=345, y=8)

        # ===================================================================================================================
        lbl_check_in_date = Label(labelframeleft, text="Check in date (YYYY/MM/DD):", font=("arial", 12, "bold"),
                                  padx=3, pady=7)
        lbl_check_in_date.grid(row=2, column=0, sticky=W)
        txt_check_in_date = Entry(labelframeleft, textvariable=self.var_check_in_date, width=22,
                                  font=("arial", 13, "bold"), bd=4, relief=RIDGE, )
        txt_check_in_date.grid(row=2, column=1)
        # ===================================================================================================================
        lbl_check_out_date = Label(labelframeleft, text="Check out date (YYYY/MM/DD):", font=("arial", 12, "bold"),
                                   padx=3, pady=7)
        lbl_check_out_date.grid(row=3, column=0, sticky=W)
        txt_check_out_date = Entry(labelframeleft, textvariable=self.var_check_out_date, width=22,
                                   font=("arial", 13, "bold"), bd=4, relief=RIDGE, )
        txt_check_out_date.grid(row=3, column=1)
        # ===================================================================================================================
        lblRoomtype = Label(labelframeleft, text="ROOM TYPE :", font=("arial", 12, "bold"), padx=3, pady=7)
        lblRoomtype.grid(row=4, column=0, sticky=W)

        combo_Roomtype = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=("arial", 13, "bold"),
                                      width=20, state="readonly")
        combo_Roomtype["value"] = ("Single", "Double", "Triple", "Deluxe", "Suite")
        combo_Roomtype.current(0)
        combo_Roomtype.grid(row=4, column=1)

        # ===================================================================================================================
        lbl_Available_Room = Label(labelframeleft, text="Available Room:", font=("arial", 12, "bold"), padx=3, pady=7)
        lbl_Available_Room.grid(row=5, column=0, sticky=W)
        txt_Available_Room = Entry(labelframeleft, textvariable=self.var_available_room, width=22,
                                   font=("arial", 13, "bold"), bd=4, relief=RIDGE, )
        txt_Available_Room.grid(row=5, column=1)

        # ==================================================================================================================
        lblmeal = Label(labelframeleft, text="MEAL  :", font=("arial", 12, "bold"), padx=3, pady=7)
        lblmeal.grid(row=6, column=0, sticky=W)

        combo_meal = ttk.Combobox(labelframeleft, textvariable=self.var_meal, font=("arial", 13, "bold"), width=20,
                                  state="readonly")
        combo_meal["value"] = ("Breakfast", "Lunch", "Dinner", "Breakfast + Lunch", "Breakfast + Dinner", "All Meals")
        combo_meal.current(0)
        combo_meal.grid(row=6, column=1)
        # ===================================================================================================================
        lbl_NO_OF_DAYS = Label(labelframeleft, text="NO OF DAYS:", font=("arial", 12, "bold"), padx=3, pady=7)
        lbl_NO_OF_DAYS.grid(row=7, column=0, sticky=W)
        txt_NO_OF_DAYS = Entry(labelframeleft, textvariable=self.var_no_of_days, width=22,
                               font=("arial", 13, "bold"), bd=4, relief=RIDGE, )
        txt_NO_OF_DAYS.grid(row=7, column=1)
        # ===================================================================================================================
        lbl_PAID_TAX = Label(labelframeleft, text="PAID TAX:", font=("arial", 12, "bold"), padx=3, pady=7)
        lbl_PAID_TAX.grid(row=8, column=0, sticky=W)
        txt_PAID_TAX = Entry(labelframeleft, width=22, textvariable=self.var_paid_tax, font=("arial", 13, "bold"),
                             bd=4, relief=RIDGE, )
        txt_PAID_TAX.grid(row=8, column=1)
        # ===================================================================================================================
        lbl_SUB_TOTAL = Label(labelframeleft, text="SUB TOTAL:", font=("arial", 12, "bold"), padx=3, pady=7)
        lbl_SUB_TOTAL.grid(row=9, column=0, sticky=W)
        txt_SUB_TOTAL = Entry(labelframeleft, textvariable=self.var_sub_total, width=22, font=("arial", 13, "bold"),
                              bd=4, relief=RIDGE, )
        txt_SUB_TOTAL.grid(row=9, column=1)
        # ===================================================================================================================
        lbl_TOTAL_COST = Label(labelframeleft, text="TOTAL COST:", font=("arial", 12, "bold"), padx=3, pady=7)
        lbl_TOTAL_COST.grid(row=10, column=0, sticky=W)
        txt_TOTAL_COST = Entry(labelframeleft, textvariable=self.var_total_cost, width=22,
                               font=("arial", 13, "bold"), bd=4, relief=RIDGE, )
        txt_TOTAL_COST.grid(row=10, column=1)



# ======================================B-T-N-S=======================================================================

        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=425, width=412, height=40)

        btnAdd = Button(btn_frame, text="ADD", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold",
                        relief=RIDGE, width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnupdate = Button(btn_frame, text="UPDATE", command=self.update, font=("arial", 12, "bold"), bg="black",
                           fg="gold", relief=RIDGE, width=9)
        btnupdate.grid(row=0, column=2, padx=1)

        btnDELETE = Button(btn_frame, text="DELETE", command=self.delete, font=("arial", 12, "bold"), bg="black",
                           fg="gold", relief=RIDGE, width=9)
        btnDELETE.grid(row=0, column=3, padx=1)

        btnRESET = Button(btn_frame, text="RESET", command=self.reset_fields, font=("arial", 12, "bold"), bg="black",
                          fg="gold", relief=RIDGE, width=9)
        btnRESET.grid(row=0, column=4, padx=1)
        # =======================================================bill btn=================================================================
        btnBill = Button(labelframeleft, text="BILL", command=self.total, font=("arial", 12, "bold"), bg="black",
                         fg="cyan", relief=RIDGE, width=9)
        btnBill.grid(row=11, column=0, padx=1, sticky=W)
        # =====================================================I-M-A-G-E================================================================

        try:
            img3 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel management system\images\suite-hotels.jpg")
            img3 = img3.resize((550, 300), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
            lblimg = Label(self.root, image=self.photoimg3, bd=4, relief=RIDGE)
            lblimg.place(x=750, y=55, width=550, height=300)
        except Exception:
            pass

        # ===============================Table Frame ===============================================================================
        table_frame = LabelFrame(self.root, text="VIEW DEATILS AND SEARCH SYSTEM ", bd=2, relief=RIDGE,
                                 font=("times new roman", 12, "bold"))
        table_frame.place(x=445, y=280, width=955, height=260)

        lblsearchBy = Label(table_frame, text="Search By: ", font=("times new roman", 12, "bold"), bg="black",
                            fg="red")
        lblsearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.serch_var = StringVar()

        combo_search = ttk.Combobox(table_frame, textvariable=self.serch_var, font=("times new roman", 12, "bold"),
                                    width=20, state="readonly")
        combo_search["value"] = ("Contact no", "Room no")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtsearch = ttk.Entry(table_frame, textvariable=self.txt_search, width=24,
                              font=("times new roman", 12, "bold"))
        txtsearch.grid(row=0, column=2, padx=2)

        btnsearch = Button(table_frame, text="SEARCH", font=("arial", 12, "bold"), bg="black", fg="gold",
                           relief=RIDGE, width=8)
        btnsearch.grid(row=0, column=3, padx=1)

        btnSHOW = Button(table_frame, text="SHOW ALL", font=("arial", 12, "bold"), bg="black", fg="gold",
                         relief=RIDGE, width=8)
        btnSHOW.grid(row=0, column=4, padx=1)

        # ================================show data===================================================

        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=250)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)



 # Columns match the rooms table ( Contact, Check_in, Check_out, Roomtype, Roomavailable, Meal, No of days )
        self.room_table = ttk.Treeview(
            details_table,
            columns=("contact", "checkin", "checkout", "roomtype", "available", "meal", "noofdays"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check In Date")
        self.room_table.heading("checkout", text="Check Out Date")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("available", text="Available Room")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="No Of Days")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=120)
        self.room_table.column("checkin", width=120)
        self.room_table.column("checkout", width=120)
        self.room_table.column("roomtype", width=120)
        self.room_table.column("available", width=120)
        self.room_table.column("meal", width=150)
        self.room_table.column("noofdays", width=100)
        self.room_table.pack(fill=BOTH, expand=1)

        self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()

    # add data
    def add_data(self):
        if self.var_contact.get() == "" or self.var_check_in_date.get() == "":
            messagebox.showerror("Error", "Contact and Check-in date are required", parent=self.root)
            return
        try:
            # compute totals first (so UI and variables are filled)
            self.total()

            conn = mysql.connector.connect(host="localhost", user="root", password="ananda", database="management")
            my_cursor = conn.cursor()

 # Keep same columns that your rooms table expects. Adjust column list below if your table differs.

            my_cursor.execute("INSERT INTO rooms (Contact, Check_in, Check_out, Roomtype, Roomavailable, Meal, `No of days`) "
                              "VALUES (%s,%s,%s,%s,%s,%s,%s)",
                              (self.var_contact.get(),
                               self.var_check_in_date.get(),
                               self.var_check_out_date.get(),
                               self.var_roomtype.get(),
                               self.var_available_room.get(),
                               self.var_meal.get(),
                               self.var_no_of_days.get()))

            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success", "ROOM BOOKED", parent=self.root)
        except mysql.connector.Error as db_err:
            messagebox.showwarning("Warning", f"Database error: {db_err}", parent=self.root)
        except Exception as es:
            messagebox.showwarning("Warning", f"something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="ananda", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM rooms")
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for i in rows:
                    # Expecting rows of length 7 (Contact,Check_in,Check_out,Roomtype,Roomavailable,Meal,No of days)
                    self.room_table.insert('', END, values=i)
            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch data: {e}", parent=self.root)

    def get_cuersor(self, event=""):
        cusrsor_row = self.room_table.focus()
        content = self.room_table.item(cusrsor_row)
        row = content.get("values")
        if not row:
            return

        # Map values to fields (adjust indices if your DB has different column order)
        self.var_contact.set(row[0])
        self.var_check_in_date.set(row[1])
        self.var_check_out_date.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_available_room.set(row[4])
        self.var_meal.set(row[5])
        try:
            self.var_no_of_days.set(int(row[6]))
        except Exception:
            self.var_no_of_days.set(0)

        # Recalculate totals (if dates are present)
        try:
            self.total()
        except Exception:
            # ignore total errors on selection
            pass

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter your mobile number ", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="ananda", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "UPDATE rooms SET Contact=%s, Check_in=%s, Check_out=%s, Roomtype=%s, Roomavailable=%s, Meal=%s, `No of days`=%s WHERE Contact=%s",
                (
                    self.var_contact.get(),
                    self.var_check_in_date.get(),
                    self.var_check_out_date.get(),
                    self.var_roomtype.get(),
                    self.var_available_room.get(),
                    self.var_meal.get(),
                    self.var_no_of_days.get(),
                    self.var_contact.get()
                )
            )
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "ROOM'S DETAILS UPDATED SUCCESSFULLY", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Update failed: {e}", parent=self.root)

    def delete(self):
        delete = messagebox.askyesno("HOTEL MANAGEMENT SYSTEM", "Do you really want to delete this room?", parent=self.root)
        if delete:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ananda", database="management")
                my_cursor = conn.cursor()
                query = "DELETE FROM rooms WHERE Contact=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                self.fetch_data()
            except Exception as e:
                messagebox.showerror("Error", f"Delete failed: {e}", parent=self.root)
        else:
            return

    def reset_fields(self):
        self.var_contact.set("")
        self.var_check_in_date.set("")
        self.var_check_out_date.set("")
        self.var_roomtype.set("Single")
        self.var_available_room.set("")
        self.var_meal.set("Breakfast")
        self.var_no_of_days.set(0)
        self.var_paid_tax.set(0.0)
        self.var_sub_total.set(0.0)
        self.var_total_cost.set(0.0)

# ================================= total calculation =====================================
    def fectch_contact(self):
        if self.var_contact.get().strip() == "":
            messagebox.showerror("Error", "Please enter your contact no ", parent=self.root)
            return
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="ananda", database="management")
            mycursor = conn.cursor()
            mycursor.execute("SELECT Name, Gender, Email, Nationality, Address FROM customer WHERE Mobile=%s",
                             (self.var_contact.get(),))
            row = mycursor.fetchone()
            conn.close()

            if row is None:
                messagebox.showerror("Error", "This number is not found ", parent=self.root)
                return

            name, gender, email, nationality, address = row

            showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
            showDataframe.place(x=450, y=55, width=300, height=180)

            lblName = Label(showDataframe, text="Name :", font=("arial", 12, "bold"))
            lblName.place(x=0, y=0)
            lblNameVal = Label(showDataframe, text=name, font=("arial", 12, "bold"))
            lblNameVal.place(x=90, y=0)

            lblGender = Label(showDataframe, text="Gender :", font=("arial", 12, "bold"))
            lblGender.place(x=0, y=30)
            lblGenderVal = Label(showDataframe, text=gender, font=("arial", 12, "bold"))
            lblGenderVal.place(x=90, y=30)

            lblmail = Label(showDataframe, text="Email :", font=("arial", 12, "bold"))
            lblmail.place(x=0, y=60)
            lblmailVal = Label(showDataframe, text=email, font=("arial", 12, "bold"))
            lblmailVal.place(x=90, y=60)

            lblnationality = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
            lblnationality.place(x=0, y=90)
            lblnationVal = Label(showDataframe, text=nationality, font=("arial", 12, "bold"))
            lblnationVal.place(x=90, y=90)

            lbladdress = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
            lbladdress.place(x=0, y=120)
            lblAddVal = Label(showDataframe, text=address, font=("arial", 12, "bold"))
            lblAddVal.place(x=90, y=120)

        except Exception as e:
            messagebox.showerror("Error", f"Failed to fetch contact: {e}", parent=self.root)

    def total(self):
        """
        Compute total cost based on:
         - room type rate per day
         - meal rate per day
         - days (derived from dates if provided, else uses var_no_of_days)
         - tax is 10% of subtotal
        """
# rates (adjust as needed)

        room_rates = {"Single": 1000, "Double": 2000, "Triple": 3000, "Deluxe": 4000, "Suite": 8000}
        meal_rates = {"Breakfast": 200, "Lunch": 300, "Dinner": 300,
                      "Breakfast + Lunch": 500, "Breakfast + Dinner": 500, "All Meals": 800}

# determine number of days
        days = None
        in_date_str = self.var_check_in_date.get().strip()
        out_date_str = self.var_check_out_date.get().strip()
        if in_date_str and out_date_str:
            try:
                in_dt = datetime.strptime(in_date_str, "%Y/%m/%d")
                out_dt = datetime.strptime(out_date_str, "%Y/%m/%d")
                days = abs((out_dt - in_dt).days)
                if days == 0:
                    days = 1
                self.var_no_of_days.set(days)
            except ValueError:
                messagebox.showerror("Error", "Dates must be in YYYY/MM/DD format", parent=self.root)
                return
        else:
# fallback to manual days or default to 1
            try:
                days = int(self.var_no_of_days.get())
                if days <= 0:
                    days = 1
                    self.var_no_of_days.set(days)
            except Exception:
                days = 1
                self.var_no_of_days.set(days)

# get rates
        room_type = self.var_roomtype.get()
        meal_type = self.var_meal.get()
        room_rate = room_rates.get(room_type, 0)
        meal_rate = meal_rates.get(meal_type, 0)

# compute
        room_cost = room_rate * days
        meal_cost = meal_rate * days
        subtotal = room_cost + meal_cost
        tax = round(subtotal * 0.10, 2)  # 10% tax
        total = round(subtotal + tax, 2)

# set vars (these show in the GUI fields)
        self.var_paid_tax.set(tax)
        self.var_sub_total.set(subtotal)
        self.var_total_cost.set(total)


if __name__ == "__main__":
    root = Tk()
    app = Roombooking(root)
    root.mainloop()