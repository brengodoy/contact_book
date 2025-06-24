from contact import Contact
import json
import os

def input_contact_data():
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

def is_valid_phone(phone_number):
    return phone_number.isdigit()

def is_valid_email(email):
    return '@' in email and '.' in email.split('@')[-1]

def add_contact(name,last_name,phone_number,email):
    if not is_valid_phone(phone_number):
        return {"status": "error","message": f"Phone number is not valid."}
    
    if not is_valid_email(email):
        return {"status": "error","message": f"Email is not valid."}
    
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