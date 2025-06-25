import sys,os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from contacts_manager import search_in_contacts_list

sample_contacts = [
    {"first_name": "Brenda", "last_name": "Godoy", "phone_number": "1234", "email": "brendagodoy@example.com"},
    {"first_name": "Federico", "last_name": "Godoy", "phone_number": "5678", "email": "federicogodoy@example.com"},
    {"first_name": "Maria", "last_name": "Lopez", "phone_number": "91011", "email": "marialopez@example.com"}
]

def test_search_1_matching_contact():
    assert len(search_in_contacts_list(sample_contacts,"brenda")) == 1
    
def test_search_2_matching_contacts():
    assert len(search_in_contacts_list(sample_contacts,"godoy")) == 2

def test_unmatching_contact():
    assert len(search_in_contacts_list(sample_contacts,"un nombre cualquiera")) == 0