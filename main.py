from contacts_manager import add_contact,input_contact_data
import sys

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
        try:
            op = int(input())
        except ValueError:
            print("The option entered is not correct.")
        match op:
            case 1: 
                name,last_name,phone_number,email = input_contact_data()
                print(add_contact(name,last_name,phone_number,email)["message"])
            case 2: search_contact()
            case 3: delete_contact()
            case 4: show_all_contacts()
            case 5: 
                print("Goodbye! Thanks for using the contact book 📒✨")
                sys.exit()
        
if __name__ == "__main__":
    menu()