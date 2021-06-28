from email import message
from email.mime.base import MIMEBase
from pathlib import Path
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# to create html template for the email content
from string import Template

def SendAutoMail(message:tuple,subject:str,recipients:list,**args)->None:
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    sender_mail="algolabdit@gmail.com"
    s.login(sender_mail, 'algolab2021')
    msg = MIMEMultipart()
    msg['From']=sender_mail
    msg['To']=','.join(recipients)
    msg['subject']=subject
    msg.attach(MIMEText(message[0],message[1]))
    if 'filename' in args:
        part=MIMEBase('application','octet-stream')
        with open(args['filename']) as F:
            part.set_payload(F.read())
        part.add_header('Content-Disposition','attachment; filename={}'.format(Path(args['filename']).name))
    msg.attach(part)
    s.send_message(msg)
    del msg
    s.quit()
    print('Email Sent:'+','.join(recipients),end='\n\n')
