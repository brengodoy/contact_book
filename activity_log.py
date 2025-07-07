from datetime import datetime

def register_backup_created(time : datetime):
    with open('activity_log.txt','a') as log_file:
        log_file.write(f"Backup created at: {time.strftime('%Y/%m/%d %H:%M:%S')}.\n")
        
def register_email_sent():
    with open('activity_log.txt','a') as log_file:
        log_file.write(f"Email sent at: {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}.\n")
        
def register_error(e : Exception):
    with open('activity_log.txt','a') as log_file:
        log_file.write(f"Error ocurred at: {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}. Message: {e}\n")
        
def register_log_message(msg : str):
    with open('activity_log.txt','a') as log_file:
        log_file.write(f"{msg} at: {datetime.now().strftime('%Y/%m/%d %H:%M:%S')}.\n")