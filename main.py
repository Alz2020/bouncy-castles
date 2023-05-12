import sqlite3 as db

# Create the connection and cursor for the first database
connection1 = db.connect("bouncy castles.db")
# I used a cursor to update records in a database table
cursor1 = connection1.cursor()

# Create the table in the first database
myQuery = """CREATE TABLE IF NOT EXISTS customer (
    id INTEGER PRIMARY KEY,
    first_name  TEXT,
    surname TEXT,
    postcode TEXT,
    house_number INTEGER,
    phone_number INTEGER
)"""
cursor1.execute(myQuery)

# Create the table in the second database
myQuery = """CREATE TABLE IF NOT EXISTS Bouncy_information  (
    id INTEGER PRIMARY KEY,
    Dimensions TEXT,
    Main colour TEXT,
    Name  TEXT,
    Maximum_occupants INTEGER,
    Hire_price INTEGER,
    Customer_id integer,
    FOREIGN KEY (Customer_id) REFERENCES customer(id)
)"""
cursor1.execute(myQuery)


# Create the table in the second database
myQuery = """CREATE TABLE IF NOT EXISTS Booking  (
    id INTEGER PRIMARY KEY,
    Customer_id integer,
    Bouncy_castle_id integer,
    Booking_date  DATE,
    Additional_notes TEXT,
    FOREIGN KEY (Customer_id) REFERENCES customer(id),
    FOREIGN KEY (Bouncy_castle_id) REFERENCES Bouncy_information (id)
)"""
cursor1.execute(myQuery)


# dispaly the data:
def view_data():

    # Prompt the user for input:
    user_input= input("Which table do you want to view data from? (customer or bouncy information, booking): ")
    
    # checking for conditions:
    if user_input == 'customer':

        # Define the SQL query:
        myQuery = "SELECT * FROM customer"

        # Execute the query
        cursor1.execute(myQuery)
        
        # get all the data
        rows = cursor1.fetchall()
        
        # to display all the records:
        for row in rows:
            print(row)

    elif user_input == 'bouncy information':

        # Define the SQL query
        myQuery = "SELECT * FROM Bouncy_information"
        
        cursor1.execute(myQuery)
        
        rows = cursor1.fetchall()
        
        for row in rows:
            print(row)
        
    elif user_input == 'booking':
        
        # Define the SQL query
        myQuery = "SELECT * FROM  Booking"  
        cursor1.execute(myQuery)
        
        rows = cursor1.fetchall()
        
        for row in rows:
            print(row)
            
    # if the user input does not meet any of the conditions: 
    else:
        print("Invalid table name.")
        return
    
    # Commit the changes
    connection1.commit()
# i didnt use cconnection1.close() because it well stop the process




def insert_data():
        
    # Prompt the user to choose which table to insert data into
    user_input= input("Which table do you want to insert data into? (customer or bouncy information, booking): ")
   
    # check for conditions
    if user_input == 'customer':
        Id = input("Enter the Id: ")
        First_Name = input("Enter the First Name : ")
        Surname = input("Enter the Surname: ")
        Postcode = input("Enter the Postcode: ")
        Phone_number = input("Enter the phone number: ")
        House_number = input("Enter the house number: ")

        # Define the SQL query
        myQuery = "INSERT INTO customer VALUES (?,?,?,?,?,?)"
        values = (Id,First_Name, Surname, Postcode, Phone_number, House_number)

    elif user_input == 'bouncy information':
        Id = input("Enter the Id: ")
        dimensions = input("Enter the dimensions: ")
        main_colour = input("Enter the main colour: ")
        name = input("Enter the name: ")
        maximum_occupants = input("Enter the maximum occupants: ")
        hire_price= input("Enter the hire price: ")
        customer_id= input("Enter the customer id: ")

        # Define the SQL query
        myQuery = "INSERT INTO Bouncy_information VALUES (?, ?, ?, ?,?,?,?)"
        values = (Id, dimensions , main_colour, name, maximum_occupants, hire_price, customer_id)
        
    elif user_input == 'booking':
        Id = input("Enter the Id: ")
        customer_id = input("Enter the customer id: ")
        bouncy_id= input("Enter the bouncy Castle id: ")
        date= input("Enter the booking date: ")
        note = input("Enter the additional note: ")
       
        # Define the SQL query
        myQuery = "INSERT INTO Booking VALUES (?, ?, ?, ?,?)"
        values = (Id, customer_id , bouncy_id, date, note )

    else:
        print("Invalid table name.")
        return
    cursor1.execute(myQuery, values)
    connection1.commit()


def search_data():

    # Prompt the user for input
    user_input= input("Search for a booking by ? (customer_id, castle_id, or date):")
    # Prompt the user for input
    if user_input == 'customer_id':
        cust_id = input("Enter the Customer id or castle id to search for a booking: ")
        
        cursor1.execute("SELECT * FROM Booking WHERE Customer_id =?",(cust_id,))
        
        rows = cursor1.fetchall()
        
        for row in rows:
            print(row)

    
    elif user_input == 'castle_id':
        bounc_id = input("Enter the Customer id or castle id to search for a booking: ")
        
        cursor1.execute("SELECT * FROM Booking WHERE Bouncy_castle_id =?",(bounc_id,))
        
        rows = cursor1.fetchall()
        
        for row in rows:
            print(row)
            
    elif user_input == 'date':

        book_date = input("Enter the date to search for a booking: ")
        
        cursor1.execute("SELECT * FROM Booking WHERE Booking_date =?",(book_date,))
        
        rows = cursor1.fetchall()
        
        for row in rows:
            print(row)
       
        
    else:
        print("Invalid table name.")
        return
    
    # Commit the changes
    connection1.commit()


    
    
def delete_data():

    # Prompt the user for input
    user_input= input("Which table do you want to delete data from? (customer or bouncy information, booking): ")
    # Prompt the user for input
    if user_input == 'customer':
        customer_id = input("Enter the Customer ID to delete: ")

        # Define the SQL query
        myQuery = "DELETE FROM customer WHERE id = ?"

        # Execute the query
        cursor1.execute(myQuery, (customer_id,))

    elif user_input == 'bouncy information':
        bouncy_id = input("Enter the bouncy ID to delete: ")

        # Define the SQL query
        myQuery = "DELETE FROM Bouncy_information WHERE id = ?"
        
        cursor1.execute(myQuery, (bouncy_id,))
        
    elif user_input == 'booking':
        booking_id = input("Enter the booking ID to delete: ")

        # Define the SQL query
        myQuery = "DELETE FROM Booking WHERE id = ?"  
        cursor1.execute(myQuery, (booking_id,))
    else:
        print("Invalid table name.")
        return
    
    # Commit the changes
    connection1.commit()

    # Close the connection
    # connection1.close()

    
while True:
    menu = """
    What do you want to do? 
    1. View data
    2. Add data
    3. Search
    4. Delete 
    5. Exit
    """
    choose = input(menu)
                
    if choose == '1':
        view_data()
    elif choose == '2':
        insert_data()
    elif choose == '3':
        search_data()
    elif choose == '4':
        delete_data()
    elif choose == '5':
     break    
 
    else:
     print("Invalid input, please choose again.")