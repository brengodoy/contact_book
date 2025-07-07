# 📒 Contact Book - Python Project

Hi there! I'm Brenda, and this is my **Contact Book**, a simple and friendly Python console application to manage your contacts in an easy and stylish way. ✨

---

## 🚀 Project Description

This project is a command-line contact book that allows you to:
- ➕ Add contacts
- 🔍 Search contacts
- ✏️ Edit contacts
- 🗑️ Delete contacts
- 📂 View all contacts
- 📤 Export contacts to Excel (.csv)
- 💾 Automatically backup your contacts every 5 minutes
- 📧 Send backups via email automatically
- 📝 Log every backup, email sent, and error in a detailed activity log

Everything is fully interactive and intuitive via a simple menu.

---

## 🛠️ Technologies Used
- Python 3.10.11
- Standard libraries: `csv`, `sys`, `json`, `os`, `pandas`, `smtplib`, `email`, `schedule`
- `pytest` for unit testing

---

## 📂 Project Structure
```
contact_book/
│
├── contact.py               # Contact class definition
├── contacts_manager.py      # Core logic for managing contacts
├── main.py                  # Interactive menu
├── auto_save.py             # Automatic backup and email scheduler
├── send_backup_email.py     # Handles sending backups via email
├── activity_log.py          # Logs activities and errors
├── contacts.csv             # Contacts storage file
├── backups/                 # Folder for JSON backups
├── activity_log.txt         # Activity log file
├── tests/                   # Unit tests folder
│ ├── test_add_contact.py
│ ├── test_delete_contact.py
│ ├── test_edit_contact.py
│ └── test_search_contact.py
└── README.md                # Project documentation (this file)
```

---

## 🎮 How to Run
1. **Clone the repository:**
```bash
git clone https://github.com/brengodoy/contact-book.git
cd contact-book
```
2. **Run the app:**
```bash
python main.py
```
3. **Enjoy!** Follow the menu options and start managing your contacts like a pro 📞✨.

---

## ✅ Testing
This project includes unit tests using `pytest`.

To run the tests:
```bash
pytest
```

---

## ✨ Cool Features
- Modular and clean code 💻
- User-friendly interactive flow 🪄
- Automated testing ✔️
- Excel export feature 📊
- Easy to scale 🚀
- Auto backup every 5 minutes ⏳
- Automatic email sending with latest backup 📧
- Activity logging for backups, emails, and errors 📝

---

## 💁‍♀️ About Me
I'm Brenda, a Systems Engineer passionate about creating software that solves real problems.  
I strive to build projects that combine clean code, innovation, and usability.  

---

## 📬 Contact
If you liked this project or want to connect:
- 💼 LinkedIn: [Brenda Godoy](https://www.linkedin.com/in/brendagodoy-/)
---

⭐️ **Thank you for stopping by! Don't forget to give this project a star if you find it useful!** ⭐️
