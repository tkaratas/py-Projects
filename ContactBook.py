""" Contact Book Project. At least im going to try to develop a contact book with python and SQLite. I tried to use classes to practice OOP. """
import sqlite3

try:
    connection = sqlite3.connect('ContactBook.db', uri=True)
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE ContactBook(ID integer primary key, Name string, Surname string, PhoneNumber integer)""")
except sqlite3.OperationalError as err:
    pass


class Person:
    def __init__(self, name, surname, phonenumber):
        self.name = name
        self.surname = surname
        self.phonenumber = phonenumber

    def addToDB(self):
        cursor.execute("INSERT INTO ContactBook VALUES(null,?,?,?)",
                       (self.name, self.surname, self.phonenumber))
        connection.commit()

    def deleteFromDB(self, id):
        cursor.execute("DELETE FROM ContactBook WHERE ID=?", (id,))
        connection.commit()

    def updatePhoneNumber(self, id, newPhoneNumber):
        cursor.execute(
            "UPDATE ContactBook SET PhoneNumber = ? WHERE ID = ?", (newPhoneNumber, id))
        connection.commit()


while True:
    print("Enter 'q' to exit.\nEnter 'add' to add a new person.\nEnter 'delete' to delete a person.\nEnter 'update' to update the phonenumber.")
    action = input("Action: ").lower()
    if action == "q":
        connection.close()
        exit()
    elif action == "delete":
        id = int(input("Id: "))
        name = cursor.execute("SELECT Name From ContactBook WHERE ID=?", (id,))
        surname = cursor.execute(
            "SELECT Surname From ContactBook WHERE ID=?", (id,))
        phonenumber = cursor.execute(
            "SELECT PhoneNumber From ContactBook WHERE ID=?", (id,))
        person = Person(name, surname, phonenumber)
        person.deleteFromDB(id)

    elif action == "add":
        name = input("Name: ")
        surname = input("Surname: ")
        phonenumber = int(input("(Old) Phone Number: "))
        person = Person(name, surname, phonenumber)
        person.addToDB()

    elif action == 'update':
        id = int(input("Id: "))
        newPhoneNumber = int(input("New Phone Number: "))
        name = cursor.execute("SELECT Name From ContactBook WHERE ID=?", (id,))
        surname = cursor.execute(
            "SELECT Surname From ContactBook WHERE ID=?", (id,))
        phonenumber = cursor.execute(
            "SELECT PhoneNumber From ContactBook WHERE ID=?", (id,))
        person = Person(name, surname, phonenumber)
        person.updatePhoneNumber(id, newPhoneNumber)

    else:
        print("Unknown Action. Please Enter a valid action.")
