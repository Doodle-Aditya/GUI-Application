# 💸 Expense Manager - CLI Version

A simple yet powerful command-line Python application to help you **track daily expenses**, categorize them, and analyze your spending habits directly from your terminal.

---

## 📂 Project Structure

```
.
├── app.py          # CLI version of the Expense Manager
├── database.db     # SQLite database to store expenses
├── gpt-gui.py      # Experimental GUI version using Generative AI (tkinter + matplotlib)
└── README.md       # This file
```

---

## 🚀 Features

- ✅ Add new expenses with category and description  
- 📊 View **total expenses**
- 📂 See **category-wise expense summaries**
- 🧾 List all unique expense categories
- 💾 Data is persisted using SQLite for reliability and simplicity
- 🧪 Experimental GUI (`gpt-gui.py`) built with tkinter + matplotlib

---

## 🛠️ How to Run

### 🔧 Requirements
- Python 3.x  
- No additional libraries required for CLI version (`sqlite3` is part of the standard library)

### ▶️ Run the App

```bash
python app.py
```

You will be greeted with a menu like this:

```
Welcome to Expense Manager

How would you like to proceed?
    1. Check Total Expense
    2. Category-wise Expense
    3. Add New Expense 
    4. List All Categories
    5. Exit the Application
```

Simply enter the number corresponding to your task and follow the prompts!

---

## 💡 Notes

- Expenses are stored locally in `database.db`.
- The experimental GUI (`gpt-gui.py`) includes **data visualization** using matplotlib and is ideal for users who prefer a graphical interface.

---

## 🧪 GUI Version Preview

You can try the GUI with:

```bash
python gpt-gui.py
```

**Features:**
- Sleek Tkinter interface
- Bar chart visualizations of category-wise expenses
- Interactive input and feedback

> *Note: Make sure `matplotlib` is installed to use the GUI.*
```bash
pip install matplotlib
```

---

## 📬 Contact

Created by [Aditya Nishad](https://github.com/doodle-aditya)  
📧 Email: adityanishad98196@gmail.com

---
