import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from contacts_manager import edit_contact,add_contact,delete_contact,search_contact

contact = {
        "first_name": "Ida",
        "last_name": "Antinori",
        "phone_number": "75298554",
        "email": "idaantinori@example.com"
    }

contact_edited = {
        "first_name": "Ida",
        "last_name": "Antinorii",
        "phone_number": "75298554",
        "email": "idaantinori@example.com"
    }

def test_edit_contact_successfully():
    add_contact("Ida","Antinori","75298554","idaantinori@example.com")
    assert edit_contact(contact,"last_name","Antinorii")["status"] == "success"
    
    search_result = search_contact("75298554")
    assert search_result[0]["last_name"] == "Antinorii"
    
    delete_contact(contact_edited)

def test_edit_non_existing_contact():
    delete_contact(contact)
    assert edit_contact(contact,"first_name","Ida Antonia")["status"] == "error"
    
def test_edit_non_existing_data_field():
    add_contact("Ida","Antinori","75298554","idaantinori@example.com")
    assert edit_contact(contact,"address","montevideo 535")["status"] == "error"
    search_result = search_contact("75298554")
    assert "address" not in search_result[0]
    delete_contact(contact)