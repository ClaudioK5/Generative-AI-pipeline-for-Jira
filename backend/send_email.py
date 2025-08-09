from email.message import EmailMessage
import smtplib


def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'insert the email'
    msg['To'] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('insert the bot email','insert the APP password for the bot email')
        smtp.send_message(msg)