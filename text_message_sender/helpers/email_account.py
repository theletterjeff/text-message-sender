"""Class used in send_text--log into
GMail account that will send the text messages"""

import os
import smtplib

from dotenv import load_dotenv

load_dotenv()

class GMailAccount:
    """Log into a GMail account"""

    def __init__(self):
        """Set login credentials"""
        self.sender_email = os.getenv('sender_email')
        self.sender_email_password = os.getenv('sender_email_password')

        if not self.sender_email:
            self.sender_email = input("Please enter sender's email (for login): ")
        if not self.sender_email_password:
            self.sender_email_password = input("Please enter sender's email password: ")

        self.smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)

    def login(self):
        """Log into Gmail"""
        self.smtp_obj.ehlo()
        self.smtp_obj.starttls()
        self.smtp_obj.login(self.sender_email, self.sender_email_password)

    def logout(self):
        """Log out of Gmail"""
        self.smtp_obj.quit()
