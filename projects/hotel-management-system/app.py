import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import mysql.connector

APP_TITLE = "Hotel Management System"
ROOM_RATES = {"Single": 1000, "Double": 2000, "Triple": 3000, "Deluxe": 4000, "Suite": 8000}
MEAL_RATES = {"Breakfast": 200, "Lunch": 300, "Dinner": 300, "Breakfast + Lunch": 500, "Breakfast + Dinner": 500, "All Meals": 800}


def db():
    return mysql.connector.connect(
        host=os.getenv("HOTEL_DB_HOST", "localhost"),
        user=os.getenv("HOTEL_DB_USER", "root"),
        password=os.getenv("HOTEL_DB_PASSWORD", ""),
        database=os.getenv("HOTEL_DB_NAME", "management"),
    )


def calculate_bill(room, meal, days):
    subtotal = (ROOM_RATES.get(room, 0) + MEAL_RATES.get(meal, 0)) * max(1, days)
    tax = round(subtotal * 0.10, 2)
    return subtotal, tax, round(subtotal + tax, 2)


class HotelApp:
    def __init__(self, root):
        self.root = root
        root.title(APP_TITLE)
        root.geometry("1200x720")
        root.minsize(1000, 650)
        self.style = ttk.Style()
        self.style.configure("Title.TLabel", font=("Segoe UI", 24, "bold"))
        self.build()

    def build(self):
        header = ttk.Frame(self.root, padding=20)
        header.pack(fill="x")
        ttk.Label(header, text="🏨 Hotel Management System", style="Title.TLabel").pack(side="left")
        ttk.Button(header, text="Exit", command=self.root.destroy).pack(side="right")

        nav = ttk.Frame(self.root, padding=(20, 0, 20, 10))
        nav.pack(fill="x")
        for text, command in (("Customers", self.customers), ("Rooms", self.rooms), ("About", self.about)):
            ttk.Button(nav, text=text, command=command).pack(side="left", padx=(0, 8))

        self.status = tk.StringVar(value="Ready")
        ttk.Label(self.root, textvariable=self.status, relief="sunken", anchor="w").pack(side="bottom", fill="x")
        body = ttk.Frame(self.root, padding=40)
        body.pack(fill="both", expand=True)
        ttk.Label(body, text="Welcome", font=("Segoe UI", 28, "bold")).pack(pady=(80, 10))
        ttk.Label(body, text="Manage customers, reservations and billing from one place.", font=("Segoe UI", 13)).pack()

    def customers(self):
        win = tk.Toplevel(self.root); win.title("Customers"); win.geometry("1000x600")
        form = ttk.LabelFrame(win, text="Customer Details", padding=15); form.pack(fill="x", padx=15, pady=15)
        fields = ["Ref", "Name", "Mother", "Gender", "PostCode", "Mobile", "Email", "Address", "IDProof", "IDNumber", "Nationality"]
        vars_ = {f: tk.StringVar() for f in fields}; vars_["Ref"].set(datetime.now().strftime("%H%M%S"))
        for i, f in enumerate(fields):
            ttk.Label(form, text=f).grid(row=i//4*2, column=i%4, sticky="w", padx=5, pady=(3,0))
            ttk.Entry(form, textvariable=vars_[f], width=22).grid(row=i//4*2+1, column=i%4, padx=5, pady=(0,6))
        tree = ttk.Treeview(win, columns=fields, show="headings")
        for f in fields: tree.heading(f, text=f); tree.column(f, width=95)
        tree.pack(fill="both", expand=True, padx=15, pady=10)
        def load():
            try:
                c=db(); cur=c.cursor(); cur.execute("SELECT Ref,Name,Mother,Gender,PostCode,Mobile,Email,Address,IDProof,IDNumber,Nationality FROM customer"); rows=cur.fetchall(); cur.close(); c.close()
                tree.delete(*tree.get_children()); [tree.insert("", "end", values=r) for r in rows]
            except Exception as e: messagebox.showerror("Database Error", str(e), parent=win)
        def add():
            try:
                c=db(); cur=c.cursor(); cur.execute("INSERT INTO customer (Ref,Name,Mother,Gender,PostCode,Mobile,Email,Address,IDProof,IDNumber,Nationality) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", tuple(vars_[f].get() for f in fields)); c.commit(); cur.close(); c.close(); load(); self.status.set("Customer added")
            except Exception as e: messagebox.showerror("Database Error", str(e), parent=win)
        ttk.Button(form, text="Add Customer", command=add).grid(row=6, column=0, padx=5, pady=8); ttk.Button(form, text="Refresh", command=load).grid(row=6, column=1, padx=5)
        load()

    def rooms(self):
        win = tk.Toplevel(self.root); win.title("Room Booking"); win.geometry("1000x650")
        form = ttk.LabelFrame(win, text="Reservation", padding=15); form.pack(fill="x", padx=15, pady=15)
        fields = {k: tk.StringVar() for k in ("Contact", "CheckIn", "CheckOut", "Room", "Available", "Meal")}
        fields["Room"].set("Single"); fields["Meal"].set("Breakfast")
        labels = list(fields)
        for i, f in enumerate(labels):
            ttk.Label(form, text=f).grid(row=i//3*2, column=i%3, sticky="w", padx=6)
            if f in ("Room", "Meal"):
                values = list(ROOM_RATES) if f == "Room" else list(MEAL_RATES)
                widget = ttk.Combobox(form, textvariable=fields[f], values=values, width=24, state="readonly")
            else:
                widget = ttk.Entry(form, textvariable=fields[f], width=27)
            widget.grid(row=i//3*2+1, column=i%3, padx=6, pady=(0,8))
        result = {k: tk.StringVar(value="0") for k in ("Days", "Subtotal", "Tax", "Total")}
        summary = ttk.Frame(form); summary.grid(row=4, column=0, columnspan=3, pady=8)
        for i, k in enumerate(result): ttk.Label(summary, text=f"{k}: ").grid(row=0, column=i, padx=(8,0)); ttk.Label(summary, textvariable=result[k]).grid(row=0, column=i, padx=(45,8))
        def bill():
            try:
                d=(datetime.strptime(fields["CheckOut"].get(), "%Y/%m/%d")-datetime.strptime(fields["CheckIn"].get(), "%Y/%m/%d")).days
                if d <= 0: raise ValueError("Check-out must be after check-in")
                sub,tax,total=calculate_bill(fields["Room"].get(), fields["Meal"].get(), d)
                result["Days"].set(str(d)); result["Subtotal"].set(str(sub)); result["Tax"].set(str(tax)); result["Total"].set(str(total)); self.status.set(f"Bill calculated: {total}")
            except Exception as e: messagebox.showerror("Billing Error", str(e), parent=win)
        ttk.Button(form, text="Calculate Bill", command=bill).grid(row=5, column=0, pady=8)
        ttk.Label(win, text="Use the schema.sql file to create the MySQL tables.", padding=15).pack(anchor="w")

    def about(self):
        messagebox.showinfo(APP_TITLE, "Python + Tkinter + MySQL hotel management project.\n\nBuilt by Ananda Devgoswami.", parent=self.root)


if __name__ == "__main__":
    root = tk.Tk(); HotelApp(root); root.mainloop()
