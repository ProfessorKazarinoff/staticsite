# local_email.py
"""
A Python script to send an email to localhost. Run the local server in a terminal with:
    $ python -m smtpd -c DebuggingServer -n localhost:1025
Then run this script from a seperate terminal
    $ python local_email.py
See the email text pop up in the first terminal
"""
import smtplib

port = 1025
sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']
message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost', port=port)
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except:
   print("Error: unable to send email")
