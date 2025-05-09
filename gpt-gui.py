import sqlite3 as sql
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt

# Connect to database
conn = sql.connect('Database.db')
curr = conn.cursor()

# Create table
curr.execute('''
    CREATE TABLE IF NOT EXISTS expense (
        categories VARCHAR(50),
        amount INT,
        description VARCHAR(50)
    )
''')
conn.commit()

# --- Function Definitions ---
def add_expense():
    category = category_entry.get().strip()
    description = description_entry.get().strip()
    try:
        amount = int(amount_entry.get().strip())
    except ValueError:
        messagebox.showerror("Invalid Input", "Amount must be a number.")
        return
    if not category or not description:
        messagebox.showerror("Missing Info", "All fields are required.")
        return
    curr.execute("INSERT INTO expense (categories, amount, description) VALUES (?, ?, ?)",
                 (category, amount, description))
    conn.commit()
    messagebox.showinfo("Success", "Expense added successfully!")
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

def total_expense():
    curr.execute("SELECT SUM(amount) FROM expense")
    total = curr.fetchone()[0] or 0
    messagebox.showinfo("Total Expense", f"Total expense: ₹{total}")

def category_expense():
    curr.execute("SELECT categories, SUM(amount) FROM expense GROUP BY categories")
    records = curr.fetchall()
    if not records:
        messagebox.showinfo("No Data", "No expenses recorded yet.")
        return
    result = "\n".join([f"{cat}: ₹{amt}" for cat, amt in records])
    messagebox.showinfo("Category-wise Expense", result)

def list_categories():
    curr.execute("SELECT DISTINCT categories FROM expense")
    records = curr.fetchall()
    if not records:
        messagebox.showinfo("No Data", "No categories recorded yet.")
        return
    result = "\n".join([f"- {cat[0]}" for cat in records])
    messagebox.showinfo("Categories", result)

def show_bar_chart():
    curr.execute("SELECT categories, SUM(amount) FROM expense GROUP BY categories")
    data = curr.fetchall()
    if not data:
        messagebox.showinfo("No Data", "No expenses to visualize.")
        return

    categories = [item[0] for item in data]
    amounts = [item[1] for item in data]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color="#3498db")
    plt.title("Category-wise Expense Distribution", fontsize=14)
    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Total Expense (₹)", fontsize=12)
    plt.tight_layout()
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# --- GUI Setup ---
root = tk.Tk()
root.title("💸 Expense Manager")
root.geometry("440x530")
root.configure(bg="#f4f4f4")
root.resizable(False, False)

# --- Styling ---
style = ttk.Style()
style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=5)
style.configure('TLabel', font=('Segoe UI', 10))
style.configure('Header.TLabel', font=('Segoe UI', 16, 'bold'))

# --- Header ---
header = ttk.Label(root, text="Expense Manager", style='Header.TLabel', foreground="#2c3e50")
header.pack(pady=20)

# --- Input Frame ---
input_frame = tk.Frame(root, bg="#f4f4f4")
input_frame.pack(pady=10)

# Category
ttk.Label(input_frame, text="Category:").grid(row=0, column=0, sticky="w", padx=10, pady=5)
category_entry = ttk.Entry(input_frame, width=30)
category_entry.grid(row=0, column=1, pady=5)

# Amount
ttk.Label(input_frame, text="Amount:").grid(row=1, column=0, sticky="w", padx=10, pady=5)
amount_entry = ttk.Entry(input_frame, width=30)
amount_entry.grid(row=1, column=1, pady=5)

# Description
ttk.Label(input_frame, text="Description:").grid(row=2, column=0, sticky="w", padx=10, pady=5)
description_entry = ttk.Entry(input_frame, width=30)
description_entry.grid(row=2, column=1, pady=5)

# --- Buttons Frame ---
button_frame = tk.Frame(root, bg="#f4f4f4")
button_frame.pack(pady=20)

ttk.Button(button_frame, text="Add Expense", command=add_expense).grid(row=0, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="Total Expense", command=total_expense).grid(row=1, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="Category-wise Expense", command=category_expense).grid(row=2, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="List Categories", command=list_categories).grid(row=3, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="Show Bar Chart", command=show_bar_chart).grid(row=4, column=0, padx=10, pady=5)
ttk.Button(button_frame, text="Exit", command=root.destroy).grid(row=5, column=0, padx=10, pady=5)

# Run the application
root.mainloop()
