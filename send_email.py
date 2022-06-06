from email import message
import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
boddy = "This is a test email from Python"
sender_email = "normunds.barbans@gmail.com"
receiver_email = "normunds.barbans@me.com"
password = input("Type your password and press enter: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(boddy)

context = ssl.create_default_context()

print("Sending email...")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print("Email sent!")
