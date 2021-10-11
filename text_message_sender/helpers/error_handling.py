"""Functions for handling errors in text_message_sender"""

import sys

def handle_keyboard_interrupt(func):
    """Gracefully exit the program"""
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except KeyboardInterrupt:
            print('Program exited.')
            sys.exit()
    return wrapper
