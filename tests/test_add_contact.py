import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from contacts_manager import add_contact,delete_contact

contact = {
        "first_name": "Maria",
        "last_name": "Lopez",
        "phone_number": "778654123",
        "email": "marialopez@example.com"
    }

def test_add_valid_contact():
    assert add_contact("Maria","Lopez","778654123","marialopez@example.com")["status"] == "success"
    delete_contact(contact)
    
def test_invalid_phone_letters():
    assert add_contact("Juan","Gonzalez","numerodetelefono","juangonzalez@example.com")["status"] == "error"
    
def test_invalid_phone_format():
    assert add_contact("Juan","Gonzalez","+34-(123)45678","juangonzalez@example.com")["status"] == "error"
    
def test_invalid_email():
    assert add_contact("Juan","Gonzalez","12345678","juangonzalez")["status"] == "error"