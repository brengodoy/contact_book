from contact import Contact
import json
import os

def ask_information():
    print("Please enter the contact data:")
    name = input("Name: ")
    last_name = input("Last name: ")
    while True:
        try:
            phone_number = input("Phone number: ")
            int(phone_number)
            break
        except ValueError:
            print("The phone number must contain only numbers.")
    email = None
    while email is None:
        email = input("Email: ")
        if '@' not in email:
            email = None
            print("Please enter a valid email.")
    return name,last_name,phone_number,email

def add_contact():
    name,last_name,phone_number,email = ask_information()
    new_contact = Contact(name,last_name,phone_number,email)
    
    if os.path.exists("contacts.json") and os.path.getsize("contacts.json") > 0:
        with open("contacts.json","r") as contacts_file:
            contacts = json.load(contacts_file)
    else:
        contacts = []

    contacts.append(new_contact.__dict__)

    try:
        with open("contacts.json","w") as contacts_file:
            json.dump(contacts,contacts_file,indent=4)
        return {"status":"success","message":"Contact created succesfully!"}
    except Exception as e:
            return {"status": "error","message": f"There was a problem: {str(e)}"}