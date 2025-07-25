import schedule
import time
import os
import json
from datetime import datetime
from contacts_manager import load_contacts_list
from send_backup_email import send_backup_email
from activity_log import register_backup_created, register_email_sent, register_error, register_log_message

def get_current_time():
    return datetime.now()

def get_backup_directory() -> str:
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, 'backups')

BACKUP_DIR = get_backup_directory()

def save_contacts_backup():
    register_log_message('Backup process started')
    contacts_list = load_contacts_list()
    file_name = get_current_time().strftime('%Y-%m-%d_%H-%M-%S')
    clear_backups_folder()
    try:
        with open(os.path.join(BACKUP_DIR, f'contacts_backup_{file_name}.json'),'w') as backup_file:
            json.dump(contacts_list,backup_file,indent=4)
            #print(f'Backup {file_name} saved successfully.')
        register_backup_created(get_current_time())
        send_backup_email(os.path.join(BACKUP_DIR, f'contacts_backup_{file_name}.json'))
        register_email_sent()
    except Exception as e:
        print(f'Error saving backup: {e}')
        register_error(e)

def clear_backups_folder():
    for filename in os.listdir(BACKUP_DIR):
        file_path = os.path.join(BACKUP_DIR, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")  
    
def run_scheduler():
    schedule.every(5).minutes.do(save_contacts_backup)
    while True:
        schedule.run_pending()
        time.sleep(1)