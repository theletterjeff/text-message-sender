"""Send one-off or recurring text messages.
Pulls a random text from a standalone .csv or .txt
file of text messages."""

import datetime
import random
import time

from dotenv import load_dotenv

from text_message_sender.helpers import email_account
from text_message_sender.helpers import error_handling
from text_message_sender.helpers import load_texts
from text_message_sender.helpers import logger
from text_message_sender.helpers.transform_cell_number import transform_cell_number

load_dotenv()

# Local classes
account = email_account.GMailAccount()
load_texts = load_texts.LoadTexts

class TextSender:
    """Class to send one-off and recurring text messages"""
    def __init__(
                self,
                recipient_number: int,
                recipient_carrier: str,
                texts_filepath: str, # A .csv or .txt file with text messages (one per line)
            ):
        self.recipient_number_email = transform_cell_number(recipient_number, recipient_carrier)
        self.texts = load_texts(texts_filepath).texts

    def send_single_text(self):
        """Send a single text message"""
        account.login()

        random_text_idx = random.randint(0,len(self.texts)-1)
        random_text = self.texts[random_text_idx]

        account.smtp_obj.sendmail(account.sender_email, self.recipient_number_email,
            f'Subject:\n{random_text}')

        logger.log_run(random_text)

        account.logout()

    @error_handling.handle_keyboard_interrupt
    def send_recurring_texts(self, **dt_kwargs):
        """
        Send text messages at the specified time intervals.
        dt_kwargs default to:
        days=0, seconds=0, microseconds=0,
        milliseconds=0, minutes=0, hours=0, weeks=0
        """
        last_run_date = logger.get_last_run()
        now = datetime.datetime.now()
        while True:
            if now - last_run_date >= datetime.timedelta(**dt_kwargs):
                self.send_single_text()
                last_run_date = now
            else:
                sleep_time = (datetime.timedelta(**dt_kwargs) -
                    (now - last_run_date)).total_seconds()
                time.sleep(sleep_time)
                self.send_single_text()

if __name__ == '__main__':
    text_message_obj = TextSender(7036186637, 'Verizon', 'text_message_files/drink_water.txt')
    text_message_obj.send_single_text()
    # text_message_obj.send_recurring_texts(seconds=10)
