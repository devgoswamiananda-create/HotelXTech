from tkinter import *
from tkinter import ttk, messagebox
from PIL import ImageTk, Image
import mysql.connector
from datetime import datetime

class DeatailsRoom:
    def __init__(self, root, scroll_y=None):
        self.root = root
        self.root.title("ROOM DEATAILS")
        self.root.geometry("1297x580+230+220")

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


if __name__ == "__main__":
    root = Tk()
    app = DeatailsRoom(root)
    root.mainloop()