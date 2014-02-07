#!/bin/python
from ConfigParser import SafeConfigParser
import imaplib
import email
import re

parser = SafeConfigParser()
parser.read('.config.txt')

uname = parser.get('login', 'uname')
p_word = parser.get('login', 'pw')

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(uname, p_word)
mail.select()
typ, data = mail.search(None, 'ALL')
for num in data[0].split():
	typ, data = mail.fetch(num, '(RFC822)')
	raw_email = data[0][1]
	email_message = email.message_from_string(raw_email)
	print email_message['Subject']
