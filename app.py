import sqlite3 as sql # Importing the library to use database

# Creating database and table for storage.
conn = sql.connect('Database.db')
curr = conn.cursor()
curr.execute('''
             CREATE TABLE IF NOT EXISTS
             expense(
             categories varchar(50),
             amount int(20),
             description varchar(50))
             ''')
conn.commit()
# Fucntion to add new category
def add_category():
    pass
# Function to add expense
def add_expense(category,amount,description):
    # Adding expense in Database
    curr.execute('''INSERT INTO expense(categories,amount,decription) VALUES (?,?,?)'''(category,amount,description))
    conn.commit()
    print('Expense Added Successfully')# Notice for successful transaction

# Fucntion to check categories wise expenses
def cat_expense():
    pass
# Function to check total expense
def total_expense():
    return

# Main function which will the start point of the app
def main():
    print('Welcome to Expense Manger')
    print('''
    How would you like to Proceed
        1. Check Total Expense
        2. Categories Wise Expense
        3. Add new Expense 
        4. Add new category
        5. Exit the Application
''')# Welcome Notice 
    
    command = int(input('Enter Your Transaction number')) # Input of the user

    # Task verification
    if command==1:
        total_expense()

    elif command==2:
        cat_expense()

    elif command==3:
        category = input('Enter in which category you want to enter')
        amount = int(input('Enter the amout you want to enter'))
        description = input('Give the description of the expense')
        add_expense(category,amount,description)

    elif command==4:
        add_category()

    elif command==5:
        print('Thanks For using us....')

    else:
        print('Invalid Input Please check the input and proceed')
        main()

if __name__ == '__main__':
    main()