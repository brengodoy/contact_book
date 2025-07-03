import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from contacts_manager import delete_contact,add_contact

def test_delete_existing_contact():
    contact = {
        "first_name": "Ida",
        "last_name": "Antinori",
        "phone_number": "75298554",
        "email": "idaantinori@example.com"
    }
    add_contact("Ida","Antinori","75298554","idaantinori@example.com")
    assert delete_contact(contact)["status"] == "success"
    
def test_delete_non_existing_contact():
    contact = {
        "first_name": "Julia",
        "last_name": "Gomez",
        "phone_number": "7625985",
        "email": "juliagomez@example.com"
    }
    assert delete_contact(contact)["status"] == "error"