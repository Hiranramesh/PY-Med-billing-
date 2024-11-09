import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class HospitalBillingSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Billing System")

        self.patient_name = tk.StringVar()
        self.age = tk.StringVar()
        self.contact_no = tk.StringVar()
        self.service = tk.StringVar()
        self.amount = tk.StringVar()
        self.total_amount = tk.StringVar()
        self.date = tk.StringVar()
        self.date.set(datetime.now().strftime("%Y-%m-%d"))

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Patient Name:").grid(column=0, row=0)
        tk.Entry(self.root, textvariable=self.patient_name).grid(column=1, row=0)

        tk.Label(self.root, text="Age:").grid(column=0, row=1)
        tk.Entry(self.root, textvariable=self.age).grid(column=1, row=1)

        tk.Label(self.root, text="Contact No:").grid(column=0, row=2)
        tk.Entry(self.root, textvariable=self.contact_no).grid(column=1, row=2)

        tk.Label(self.root, text="Service:").grid(column=0, row=3)
        ttk.Combobox(self.root, textvariable=self.service, values=["Consultation", "Surgery", "Medicine"]).grid(column=1, row=3)

        tk.Label(self.root, text="Amount:").grid(column=0, row=4)
        tk.Entry(self.root, textvariable=self.amount).grid(column=1, row=4)

        self.bill_text = tk.Text(self.root)
        self.bill_text.grid(column=0, row=5, columnspan=2)

        tk.Button(self.root, text="Add to Bill", command=self.add_to_bill).grid(column=1, row=6)
        tk.Button(self.root, text="Calculate Total", command=self.calculate_total).grid(column=0, row=7)

        tk.Label(self.root, text="Total Amount:").grid(column=0, row=8)
        tk.Entry(self.root, textvariable=self.total_amount).grid(column=1, row=8)

        tk.Label(self.root, text="Date:").grid(column=0, row=9)
        tk.Entry(self.root, textvariable=self.date).grid(column=1, row=9)

        tk.Button(self.root, text="Generate Bill", command=self.generate_bill).grid(column=1, row=10)

    def add_to_bill(self):
        try:
            service = self.service.get()
            amount = float(self.amount.get())
            self.bill_text.insert(tk.END, f"{service}: {amount}\n")
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number")

    def calculate_total(self):
        try:
            total = 0
            for line in self.bill_text.get("1.0", tk.END).splitlines():
                total += float(line.split(":")[1].strip())
            self.total_amount.set(str(total))
        except ValueError:
            messagebox.showerror("Error", "Invalid bill items")

    def generate_bill(self):
        bill = f"Patient Name: {self.patient_name.get()}\nAge: {self.age.get()}\nContact No: {self.contact_no.get()}\nDate: {self.date.get()}\n\n{self.bill_text.get('1.0', tk.END)}\nTotal Amount: {self.total_amount.get()}"
        print(bill)
        messagebox.showinfo("Success", "Bill generated successfully")

root = tk.Tk()
hospital_billing_system = HospitalBillingSystem(root)
root.mainloop()
