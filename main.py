from contact import Contact
import json
import sys,os

def add_contact():
    print("Please enter the name of the contact:")
    name = input()
    print("Please enter the last name of the contact:")
    last_name = input()
    print("Please enter the phone number of the contact:")
    phone_number = input()
    print("Please enter the email of the contact:")
    email = input()
    
    new_contact = Contact(name,last_name,phone_number,email)
    
    if os.path.exists("contacts.json") and os.path.getsize("contacts.json") > 0:
        with open("contacts.json","r") as contacts_file:
            contacts = json.load(contacts_file)
    else:
        contacts = []

    contacts.append(new_contact.__dict__)

    with open("contacts.json","w") as contacts_file:
        json.dump(contacts,contacts_file,indent=4)

def show_options():
    print("Please select an option:")
    print("1) Add contact")
    print("2) Search contact")
    print("3) Delete contact")
    print("4) Show all contacts")
    print("5) Exit")
    
def menu():
    print("Welcome to the contact book!")
    op = 0
    while True:
        show_options()
        op = int(input())
        match op:
            case 1: add_contact()
            case 2: search_contact()
            case 3: delete_contact()
            case 4: show_all_contacts()
            case 5: sys.exit()
        
menu()