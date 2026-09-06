from optparse import Values
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector
import random
from tkinter import messagebox

class cust_Win:
    def __init__(self, root, scroll_y=None):
        self.root=root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1297x580+230+220")
#========================================variable=======================================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_crust_name=StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_nationality = StringVar()



 #========================titel===============================================================
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 20, "bold"), bg="black",
                      fg="gold", bd=0, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1400, height=50)
#===========================logo=================================================================


        img2 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel management system\images\logo.jpg")
        img2 = img2.resize((150,80),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=0, y=0, width=100, height=50)

#===============================label frame========================================================
        labelframeleft = LabelFrame(self.root,text="customer details",bd=2,relief=RIDGE,font=("times new roman",12,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

#=========================labels and entry ======================================================
        lbl_cust_ref=Label(labelframeleft,text="Customer Reference",font=("times new roman",17,"bold"))
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        enty_ref = Entry(labelframeleft,textvariable=self.var_ref, width=22, font=("times new roman", 12, "bold"))
        enty_ref.grid(row=0, column=1)
#==================================================================================================================
        c_name = Label(labelframeleft, text="Customer name", font=("times new roman", 17, "bold"))
        c_name.grid(row=1, column=0, sticky=W)
        txtname = Entry(labelframeleft,textvariable=self.var_crust_name, width=22, font=("times new roman", 12, "bold"))
        txtname.grid(row=1, column=1)
#===================================================================================================================
        lblname= Label(labelframeleft, text="Mother name ", font=("times new roman", 17, "bold"))
        lblname.grid(row=2, column=0, sticky=W)
        txtcname = Entry(labelframeleft,textvariable=self.var_mother, width=22, font=("times new roman", 12, "bold"))
        txtcname.grid(row=2, column=1)
#===================================================================================================================
        lblgender = Label(labelframeleft, text="Gender :", font=("times new roman", 17, "bold"))
        lblgender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft,textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=20,state=
                                    "readonly")
        combo_gender["value"] = ("male", "female", "other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

#=============================================================================================================
        lblpostcode = Label(labelframeleft, text="PostCode :", font=("times new roman", 17, "bold"))
        lblpostcode.grid(row=4, column=0, sticky=W)
        txtp = Entry(labelframeleft,textvariable=self.var_post, width=22, font=("times new roman", 12, "bold"))
        txtp.grid(row=4, column=1)
#=========================================================================================================
        lblmobile = Label(labelframeleft, text="Mobile :", font=("times new roman", 17, "bold"))
        lblmobile.grid(row=5, column=0, sticky=W)
        txtmobile = Entry(labelframeleft,textvariable=self.var_mobile, width=22, font=("times new roman", 12, "bold"))
        txtmobile.grid(row=5, column=1)
#===================================================================================================
        lblEmail= Label(labelframeleft, text="Email :", font=("times new roman", 17, "bold"))
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = Entry(labelframeleft,textvariable=self.var_email, width=22, font=("times new roman", 12, "bold"))
        txtEmail.grid(row=6, column=1)
#=============================================================================================================
        lblNationality = Label(labelframeleft, text="Nationality :", font=("times new roman", 17, "bold"))
        lblNationality.grid(row=8, column=0, sticky=W)

        combo_nationality = ttk.Combobox(labelframeleft,textvariable=self.var_nationality, font=("times new roman", 12, "bold"), width=20, state=
        "readonly")
        combo_nationality["value"] = ("INDIAN", "AMERICAN", "BRITISH", "CANADIAN", "AUSTRALIAN", "CHINESE", "JAPANESE", "KOREAN", "GERMAN", "FRENCH", "ITALIAN", "SPANISH", "RUSSIAN", "BRAZILIAN", "MEXICAN", "NEPALESE", "BANGLADESHI", "PAKISTANI", "SRI LANKAN", "SOUTH AFRICAN")
        combo_nationality.current(0)
        combo_nationality.grid(row=8, column=1)



#===============================================================================================================
        lblID = Label(labelframeleft, text="ID_PROOF Type :", font=("times new roman", 12, "bold"))
        lblID.grid(row=9, column=0, sticky=W)

        combo_ID = ttk.Combobox(labelframeleft,textvariable=self.var_idproof , font=("times new roman", 12,), width=20, state=
        "readonly")
        combo_ID["value"] = ("AADHAR CARD", "PAN CARD", "PASSPORT", "VOTER ID CARD", "DRIVING LICENSE", "RATION CARD", "BIRTH CERTIFICATE", "EMPLOYEE ID CARD", "STUDENT ID CARD", "NREGA JOB CARD", "PENSION CARD", "HEALTH CARD", "DISABILITY ID CARD", "SENIOR CITIZEN CARD", "RESIDENCE PERMIT", "OCI CARD", "PIO CARD", "ARMY CANTEEN CARD", "GOVERNMENT ID CARD", "TAX ID CARD")
        combo_ID.current(0)
        combo_ID.grid(row=9, column=1)



#==========================================================================================================
        lblidN = Label(labelframeleft, text="Id Number :", font=("times new roman", 12, "bold"))
        lblidN.grid(row=10, column=0, sticky=W)
        txtidN = Entry(labelframeleft,textvariable=self.var_idnumber, width=22, font=("times new roman", 12, "bold"))
        txtidN.grid(row=10, column=1)

#============================================================================================================
        lblAddress = Label(labelframeleft, text="Address :", font=("times new roman", 12, "bold"))
        lblAddress.grid(row=11, column=0, sticky=W)
        txtAddress= Entry(labelframeleft,textvariable=self.var_address, width=22, font=("times new roman", 12, "bold"))
        txtAddress.grid(row=11, column=1)

#==================================================BTNS====================================================
        btn_frame = Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",relief=RIDGE,width=9)
        btnAdd.grid(row=0,column=0,padx=1)

        btnupdate = Button(btn_frame, text="UPDATE",command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", relief=RIDGE, width=9)
        btnupdate.grid(row=0, column=2, padx=1)

        btnDELETE = Button(btn_frame, text="DELETE",command=self.delete, font=("arial", 12, "bold"), bg="black", fg="gold", relief=RIDGE, width=9)
        btnDELETE.grid(row=0, column=3, padx=1)

        btnRESET = Button(btn_frame, text="RESET",command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", relief=RIDGE, width=9)
        btnRESET.grid(row=0, column=4, padx=1)



#===============================Table Frame ===============================================================================
        table_frame = LabelFrame(self.root, text="VIEW DEATILS AND SEARCH SYSTEM ", bd=2, relief=RIDGE,
                                    font=("times new roman", 12, "bold"))
        table_frame.place(x=445, y=50, width=955, height=490)

        lblsearchBy = Label( table_frame, text="Search By: ", font=("times new roman", 12, "bold"),bg="red",fg="white")
        lblsearchBy.grid(row=0, column=0, sticky=W,padx=2)

        self.serch_var = StringVar()

        combo_search = ttk.Combobox(table_frame,textvariable=self.serch_var, font=("times new roman", 12, "bold"), width=20, state=
        "readonly")
        combo_search["value"] = ("Mobile","Ref_no")
        combo_search.current(0)
        combo_search.grid(row=0, column=1,padx=2)



        self.txt_search=StringVar()
        txtsearch=ttk.Entry(table_frame,textvariable=self.txt_search, width=24, font=("times new roman", 12, "bold"))
        txtsearch.grid(row=0, column=2,padx=2)



        btnsearch = Button(table_frame, text="SEARCH",command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", relief=RIDGE,
                           width=8)
        btnsearch.grid(row=0, column=3, padx=1)

        btnSHOW = Button(table_frame, text="SHOW ALL",command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", relief=RIDGE,
                          width=8)
        btnSHOW.grid(row=0, column=4, padx=1)


        #================================show data===================================================

        details_table = Frame(table_frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=350)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_details_table = ttk.Treeview(
            details_table,
            columns=("ref", "name", "mother", "gender", "post", "mobile", "email", "address", "idproof", "idnumber",
                     "nationality"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set
        )

        scroll_x.pack(side= BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_details_table.xview)
        scroll_y.config(command=self.Cust_details_table.yview)

        self.Cust_details_table.heading("ref",text="Refer No")
        self.Cust_details_table.heading("name", text="Name")
        self.Cust_details_table.heading("mother", text="Mother Name")
        self.Cust_details_table.heading("gender", text="Gender")
        self.Cust_details_table.heading("post", text="Post Code")
        self.Cust_details_table.heading("mobile", text="Mobile No")
        self.Cust_details_table.heading("email", text="Email")
        self.Cust_details_table.heading("address", text="Address")
        self.Cust_details_table.heading("idproof", text="ID Proof")
        self.Cust_details_table.heading("idnumber", text="ID Number")
        self.Cust_details_table.heading("nationality", text="Nationality")

        self.Cust_details_table["show"]="headings"

        self.Cust_details_table.column("ref", width=100)
        self.Cust_details_table.column("name", width=100)
        self.Cust_details_table.column("mother", width=100)
        self.Cust_details_table.column("gender", width=100)
        self.Cust_details_table.column("post", width=100)
        self.Cust_details_table.column("mobile", width=100)
        self.Cust_details_table.column("email", width=100)
        self.Cust_details_table.column("address", width=100)
        self.Cust_details_table.column("idproof", width=100)
        self.Cust_details_table.column("idnumber", width=100)
        self.Cust_details_table.column("nationality", width=100)

        self.Cust_details_table.pack(fill=BOTH, expand=1)
        self.Cust_details_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get()=="" or self.var_mother.get()=="":
            messagebox.showerror("Error", "All fields are required",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="ananda", database="management")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_crust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_idproof.get(),
                    self.var_idnumber.get(),
                    self.var_nationality.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "CUSTOM ADDED SUCCESSFULLY",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"something went wrong:{str(es)}",parent=self.root)
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost", user="root", passwd="ananda", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cuersor(self,event=""):
        cusrsor_row=self.Cust_details_table.focus()
        content=self.Cust_details_table.item(cusrsor_row)
        row=content.get("values")

        self.var_ref.set(row[0]),
        self.var_crust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_idnumber.set(row[9]),
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error", "Please enter your mobile number ",parent=self.root)
        else:

            conn=mysql.connector.connect(host="localhost", user="root", password="ananda", database="management")
            my_cursor = conn.cursor()
            my_cursor.execute(
                "UPDATE customer SET Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Address=%s, IDProof=%s, IDNumber=%s, Nationality=%s WHERE Ref=%s",
                (self.var_crust_name.get(), self.var_mother.get(), self.var_gender.get(), self.var_post.get(),
                 self.var_mobile.get(), self.var_email.get(), self.var_address.get(), self.var_idproof.get(),
                 self.var_idnumber.get(), self.var_nationality.get(), self.var_ref.get()))


            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "CUSTOM UPDATE SUCCESSFULLY",parent=self.root)

    def delete(self):
        delete=messagebox.askyesno("HOTEL MANAGEMENT SYSTEM","Do you really want to delete this customer?",parent=self.root)
        if delete>0:
            conn = mysql.connector.connect(host="localhost", user="root", password="ananda", database="management")
            my_cursor = conn.cursor()
            query = f"DELETE FROM customer WHERE Ref=%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        #self.var_ref.set(""),
        self.var_crust_name.set(""),
        self.var_mother.set(""),
        #self.var_gender.set(""),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        #self.var_nationality.set(""),
        #self.var_idproof.set(""),
        self.var_idnumber.set(""),
        self.var_address.set("")


        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="ananda", database="management")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer WHERE " + str(self.serch_var.get()) + " LIKE %s",
                          ("%" + str(self.txt_search.get()) + "%",))
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for i in rows:
                self.Cust_details_table.insert("",END,values=i)

            conn.commit()
        conn.close()



if __name__=="__main__":
    root=Tk()
    obj=cust_Win(root)
    root.mainloop()