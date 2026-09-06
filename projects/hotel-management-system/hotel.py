from tkinter import *
from PIL import Image,ImageTk
from customer import cust_Win
from room import Roombooking



class HotelManagementSystem:                           #   mera hi class hai
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #=================ist upper img============================


        img1 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel management system\images\Screenshot 2026-08-02 002119.png")
        img1=img1.resize((1500,150),Image.LANCZOS)                    #ek high-quality resampling method hai.
        self.photoimg1 = ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image = self.photoimg1,bd=4,relief=RIDGE)    #level :- image and picture
        lblimg.place(x=0,y=0,width=1550,height=140)


       #===================logo==============================

        img2 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel management system\images\74f0d9_6879870255a84441bca61de944616a01~mv2.png")
        img2 = img2.resize((250, 200),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)
       #======================titel=========================
        lbl_title =Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1700, height=50)

       #======================main frame=========================

        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1550,height=620)
       #========= menu ===========================================
        lbl_title = Label(main_frame, text=" MENU", font=("times new roman", 20, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=230, height=50)
        # ======================between frame=========================

        btn_frame = Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=50, width=228, height=230)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman", 14, "bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        cust_btn.grid(row=0,column=0)

        room_btn = Button(btn_frame, text="ROOM",command=self.roomboooking, width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        room_btn.grid(row=1, column=0,pady=1)

        details_btn = Button(btn_frame, text="DETAILS", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        details_btn.grid(row=2, column=0,pady=1)

        report_btn= Button(btn_frame, text="REPORT", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        report_btn.grid(row=3, column=0,pady=1)

        logout_btn = Button(btn_frame, text="LOG OUT ", width=22, font=("times new roman", 14, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        logout_btn.grid(row=4, column=0,pady=1)

  #======================= right side image ===================================================
        img3 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel management system\images\stylish-marble-reception-table-803225145-qupeux2b.avif")
        img3 = img3.resize((1500,620), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=620)
   #=======================down 2 image ========================================================
        img4 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel management system\images\171860869215--B-VOC-in-Hotel-Management.webp")
        img4 = img4.resize((300,200), Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=200)
 #=================================================================================================
        img5 = Image.open(r"C:\Users\ASUS\OneDrive\Desktop\Hotel management system\images\images (3).jpg")
        img5 = img5.resize((300,200), Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=200)

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app= cust_Win(self.new_window)

    def roomboooking(self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)




if __name__=="__main__":
    root=Tk()                                 # main window create karoo, yaha pe tk window banata hai and rootisko reference deta hai
    obj=HotelManagementSystem(root)
    root.mainloop()
