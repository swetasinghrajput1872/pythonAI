import random
import smtplib

# User se email input
user_email = input("Enter your email: ")

# OTP generate (6 digit)
otp = random.randint(100000, 999999)

# Sender details
sender_email = "swetasinghrajput1872@gmail.com"
sender_password = "dehn qekf ldwx viqb"  # Gmail App Password

# Email message
message = f"Subject: OTP Verification\n\nYour OTP is: {otp}"

# Email send
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, sender_password)
server.sendmail(sender_email, user_email, message)
server.quit()

print("OTP sent successfully to your email!")

# OTP 
user_otp = int(input("Enter OTP: "))

if user_otp == otp:
    print("OTP Verified ✅")
else:
    print("Invalid OTP ❌")