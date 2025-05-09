import sqlite3 as sql

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

# Function to list all categories
def list_category():
    curr.execute("SELECT DISTINCT categories FROM expense")
    categories = curr.fetchall()
    print("Categories:")
    for cat in categories:
        print(f"- {cat[0]}")

# Function to add an expense
def add_expense(category, amount, description):
    curr.execute('''INSERT INTO expense (categories, amount, description) VALUES (?, ?, ?)''',
                 (category, amount, description))
    conn.commit()
    print('Expense Added Successfully')

# Function to show category-wise expenses
def cat_expense():
    curr.execute('''SELECT categories, SUM(amount) FROM expense GROUP BY categories''')
    expense = curr.fetchall()
    print("Category-wise Expense:")
    for cat, total in expense:
        print(f"{cat}: ₹{total}")

# Function to check total expense
def total_expense():
    curr.execute('''SELECT SUM(amount) FROM expense''')
    amount = curr.fetchone()[0]
    print(f'Total expense: ₹{amount if amount else 0}')

# Main function
def main():
    while True:
        print('''
Welcome to Expense Manager

How would you like to proceed?
    1. Check Total Expense
    2. Category-wise Expense
    3. Add New Expense 
    4. List All Categories
    5. Exit the Application
''')
        try:
            command = int(input('Enter your option: '))
            if command == 1:
                total_expense()
            elif command == 2:
                cat_expense()
            elif command == 3:
                category = input('Enter the category: ')
                amount = int(input('Enter the amount: '))
                description = input('Enter the description: ')
                add_expense(category, amount, description)
            elif command == 4:
                list_category()
            elif command == 5:
                print('Thanks for using Expense Manager. Goodbye!')
                break
            else:
                print('Invalid input. Please try again.')
        except ValueError:
            print('Value error: Enter a valid number.')

if __name__ == '__main__':
    main()
