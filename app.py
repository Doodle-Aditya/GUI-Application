
# Fucntion to add new category
def add_category():
    pass
# Function to add expense
def add_expense():
    pass
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
        add_expense()
    elif command==4:
        add_category()
    elif command==5:
        print('Thanks For using us....')
    else:
        print('Invalid Input Please check the input and proceed')
        main()

if __name__ == '__main__':
    main()