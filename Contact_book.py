def display():
    print("\n Contact Booko Manager")
    print("1.-- Add New Contact")
    print("2.--Search for Contact")
    print("3.--Delete Contact")
    print("4.--View Contacts")
    print("5.--Exit")

def add_contact(c_book):
    name=input("Enter Contact name:- ")
    phone=input("Enter phone number:- ")
    email=input("enter email:- ")

    c_book[name]={'phone':phone,'email':email}
    print("Contact Added Successfully!")

def search_contact(c_book):
    name=input("Enter contact name to search: ")

    if name in c_book:
        print(f"\n contact Details for {name}:- ")
        print(f"Phone: {c_book[name]['phone']}")
        print(f"email: {c_book[name]['email']}")
    else:
        print(f"Contact '{name}' not found")

def delete_contact(c_book):
    name=input("enter contact name to delete:-  ")

    if name in c_book:
        del c_book[name]
        print(f" Contact '{name}' deleted sucessfully!")
    else:
        print(f"Contact 'name' not found")

def display_contacts(c_book):
    print("\n Contact List: ")
    for name, details in c_book.items():
        print(f"{name}---phone: {details['phone']}, Email:---{details['email']}")


c_book={}

while True:
    display()
    choice=input("Enter your Choice:--")

    if(choice=='1'):
        add_contact(c_book)
    elif(choice=='2'):
        search_contact(c_book)
    elif(choice=='3'):
        delete_contact(c_book)
    elif(choice=='4'):
        display_contacts(c_book)
    elif(choice=='5'):
        print("exiting")
        break
    else:
        print("Invalid choice")