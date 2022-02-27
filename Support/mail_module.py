import smtplib
import ssl
import credentials
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(mail_receiver, mail_text, mail_subject, mail_attachement=''):
   
    dic_config_data = credentials.read_credentials()
    mail_sender = dic_config_data['mail_sender']
    mail_server = dic_config_data['mail_server']
    mail_port = int(dic_config_data['mail_port'])
    mail_password = dic_config_data['mail_password']


    mail_message = MIMEMultipart()
    mail_message["From"] = mail_sender
    mail_message["To"] = mail_receiver
    mail_message["Subject"] = mail_subject
    mail_message.attach(MIMEText(mail_text, "plain"))

    filename = mail_attachement 

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

  
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    mail_message.attach(part)
    text = mail_message.as_string()
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(mail_server, mail_port, context=context) as server:
        server.login(mail_sender, mail_password)
        server.sendmail(mail_sender, mail_receiver, text)

