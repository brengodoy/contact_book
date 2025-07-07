import smtplib
import os
from email.mime.text import MIMEText
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

receiver_email = sender_email = os.getenv('EMAIL_ADDRESS')
password = os.getenv('EMAIL_PASSWORD')
smtp_server = "smtp.gmail.com"
port = 587

def send_backup_email(backup_file : str) -> None:
    """
    Sends an email with a backup of the contacts to the user's email address.
    
    Parameters
    ----------
    backup_file : str
        The path to the backup file to be sent.
    
    Returns
    -------
    None
    """
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Automatic contacts backup"
    message.attach(MIMEText("This is an automated email with a backup of your contacts.", 'plain'))
    
    file_name = os.path.basename(backup_file)
    with open(backup_file, "rb") as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
    message.attach(part)
    
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        #print("Correo enviado con éxito.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
    finally:
        server.quit()