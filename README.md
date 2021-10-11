# Text Message Sender
This program sends pre-programmed text messages that are entered into .txt or .csv files. It's most useful for reminder text messages (e.g., drink more water, pay bills on time).

It presumes that the .txt or .csv files contain multiple possible text messages, and it randomly selects one from the list. If there is only one message in the file, it chooses that one.

It can be used in one of two ways:

## Send one-off text messages
You may send a single text message using the send_single_text method in the send_text.py module's TextSender class.

This can be integrated into scripts for when you want to send a text upon the execution of an action--e.g., whenever a user does something on in a web app, send them a text message.

It can also be useful for ad hoc sends--e.g., you may remember that you want to remind your spouse to take out the trash, and you can quickly run your own pre-configured script rather than typing out a text message on your phone.

## Send recurring text messages
The other primary use case is to send recurring text messages.

Indeed, this was the original impetus for this program's creation--the author's mom wasn't drinking enough water, and he wanted to send her a text reminder a few times a day to hydrate.

You can schedule recurring texts using the send_recurring_texts method in the send_text.py module's TextSender class.

### Limitations on recurring text messages
Note that the program will only be able to send text messages while running--so, e.g., scheduling a text send for overnight when your local version of the program is not running will not result in correct exeuction.

The program keeps a log of the last time that it sent a message, and if it finds that more time has elapsed since the last send than the user specified in the method call, it will send a new text.

One option for circumventing these limitations is to host the program on a cloud server, where it will run continuously.

## Email platforms supported
At present, you must have a GMail account to use this program. (Texts are sent to cell phones through email.)