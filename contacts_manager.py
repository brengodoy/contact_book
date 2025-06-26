from contact import Contact
import json
import os
import pandas as pd

def input_contact_data():
    print("Please enter the contact data:")
    name = input("Name: ")
    last_name = input("Last name: ")
    while True:
        phone_number = input("Phone number: ")
        if is_valid_phone(phone_number):
            if search_contact(phone_number) == []:
                break
            else:
                print("That phone number already exists.")
        else:
            print("The phone number must contain only numbers.")
    while True:
        email = input("Email: ")
        if is_valid_email(email):
            break
        else:
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
        contacts = load_contacts_list()
    else:
        contacts = []

    contacts.append(new_contact.__dict__)

    try:
        with open("contacts.json","w") as contacts_file:
            json.dump(contacts,contacts_file,indent=4)
        return {"status":"success","message":"Contact created succesfully!"}
    except Exception as e:
            return {"status": "error","message": f"There was a problem: {str(e)}"}
        
def search_contact(contact_data):
    try:
        contacts_list = load_contacts_list()
    except Exception as e:
        print(f"There was a problem while trying to access the JSON file: {str(e)}")
        return []
    
    return search_in_contacts_list(contacts_list,contact_data)

def search_in_contacts_list(contacts_list,contact_data):
    contact_match = []
    for contact in contacts_list:
        if (contact["first_name"].lower() == contact_data.lower() or 
            contact["last_name"].lower() == contact_data.lower() or 
            contact["phone_number"] == contact_data):
            contact_match.append(contact)
    return contact_match

def show_contacts_found(contact_match):
    if contact_match:
        print(f"Contacts that matched with the criteria: {str(len(contact_match))}")
        for index,contact in enumerate(contact_match):
            print(f"""{str(index+1)}) CONTACT INFO:
- First name: {contact["first_name"]}
- Last name: {contact["last_name"]}
- Phone number: {contact["phone_number"]}
- Email: {contact["email"]}""")
    else:
        print(f'There are no contacts that match with the criteria.')
        
def select_contact_to_delete(contact_match):
    show_contacts_found(contact_match)
    if len(contact_match) == 0:
        return None
    elif len(contact_match) == 1:
        return contact_match[0]
    elif len(contact_match) > 1:
        while True:
            try:
                index = int(input("Which contact do you want to delete? Please enter the numer assigned to the contact: "))
                if 1 <= index <= len(contact_match):
                    return contact_match[index - 1]
                else:
                    print("Please enter a valid option: ")
            except ValueError:
                print("Invalid input. Please enter a number.")

def ask_for_confirmation(contact):
    op = input("Are you sure you want to delete "+ contact["first_name"] + " " + contact["last_name"] + "'s contact? [Y/N] ")
    while op.lower() != 'y' and op.lower() != 'n':
        op = input("Please enter a valid option: Y/N ")
    return op
    
def delete_contact(contact_to_delete):
    try:
        contacts_list = load_contacts_list()
        if contact_to_delete in contacts_list:
            contacts_list.remove(contact_to_delete)
            with open("contacts.json",'w') as contacts_file:
                json.dump(contacts_list,contacts_file,indent=4)
            return {"status":"success","message":"Contact deleted succesfully!"}
        else:
            return {"status": "error","message": f"Contact not found."}    
    except Exception as e:
        return {"status": "error","message": f"There was a problem: {str(e)}"}
    
def load_contacts_list():
    try:
        with open('contacts.json','r') as contacts_file:
            return json.load(contacts_file)
    except Exception as e:
        return []
    
def show_all_contacts():
    try:
        contacts_list = load_contacts_list()
        for index,contact in enumerate(contacts_list):
            print(f"""{str(index+1)}) CONTACT INFO:
- First name: {contact["first_name"]}
- Last name: {contact["last_name"]}
- Phone number: {contact["phone_number"]}
- Email: {contact["email"]}""")
        return {"status": "success","message": f"Contacts showed successfully."}
    except Exception as e:
        return {"status": "error","message": f"There was a problem: {str(e)}"}
    
def export_contacts():
    try:
        contacts_list = load_contacts_list()
        df = pd.DataFrame(contacts_list)
        df.to_csv('datos.csv', index=False)
        return {"status": "success","message": f"Data exported successfully."}
    except Exception as e:
        return {"status": "error","message": f"There was a problem: {str(e)}"}