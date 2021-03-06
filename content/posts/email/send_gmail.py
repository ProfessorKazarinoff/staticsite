# send_gmail.py

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "mythrowawayemail@gmail.com"  # your throw away gmail address
receiver_email = "mythrowawayemail@gmail.com"  # your throw away gamil address
password = input("Enter throw away gmail account password: ")
message = """\
Subject: Test Email from Python

This message was sent from Python.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
