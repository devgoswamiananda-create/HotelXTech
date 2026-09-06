from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from time import strftime

class HotelManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        img1 = Image.open(r"C:\Users\anand\OneDrive\Desktop\Hotel management system\hotel\images\hotel.jpg")
        img1 = img1.resize((1550, 140), Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        lbl_title = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="white", fg="black", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=70)

        # ================= Main Frame =================
        main_frame = Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=210, width=1550, height=590)

        lbl_menu = Label(main_frame, text="MENU", font=("times new roman", 20, "bold"), bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        # ================= Buttons Frame =================
        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=50, width=228, height=520)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.customer_details, width=22, font=("times new roman", 14, "bold"), bg="white", fg="black", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady=10)

        room_btn = Button(btn_frame, text="ROOM", command=self.room_details, width=22, font=("times new roman", 14, "bold"), bg="white", fg="black", bd=0, cursor="hand1")
        room_btn.grid(row=1, column=0, pady=10)

        details_btn = Button(btn_frame, text="DETAILS", command=self.details, width=22, font=("times new roman", 14, "bold"), bg="white", fg="black", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady=10)

        report_btn = Button(btn_frame, text="REPORT", command=self.report, width=22, font=("times new roman", 14, "bold"), bg="white", fg="black", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady=10)

        logout_btn = Button(btn_frame, text="LOG OUT", command=self.root.destroy, width=22, font=("times new roman", 14, "bold"), bg="white", fg="black", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady=10)

        # ================= Right Image =================
        img2 = Image.open(r"C:\Users\anand\OneDrive\Desktop\Hotel management system\hotel\images\hotel2.jpg")
        img2 = img2.resize((1300, 520), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(main_frame, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg2.place(x=230, y=50, width=1300, height=520)

    def customer_details(self):
        from customer import Customer_Window
        self.new_window = Toplevel(self.root)
        self.app = Customer_Window(self.new_window)

    def room_details(self):
        from room import RoomBooking
        self.new_window = Toplevel(self.root)
        self.app = RoomBooking(self.new_window)

    def details(self):
        from deatails import Details
        self.new_window = Toplevel(self.root)
        self.app = Details(self.new_window)

    def report(self):
        messagebox.showinfo("Report", "Report section is under development.", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = HotelManagementSystem(root)
    root.mainloop()
