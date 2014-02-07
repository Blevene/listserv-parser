#!/bin/python
from ConfigParser import SafeConfigParser
import imaplib
import email
import re

#Global Variables n' Such
parser = SafeConfigParser()
parser.read('.config.txt')

uname = parser.get('login', 'uname')
p_word = parser.get('login', 'pw')

mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(uname, p_word)
mail.select('inbox')
typ, data = mail.search(None, 'ALL')
unread_count = len(mail.search(None, 'UnSeen')[1][0].split())
print "There are a total of %s unread messages." % unread_count
for num in data[0].split():
	typ, data = mail.fetch(num, '(RFC822)')
	raw_email = data[0][1]
	email_message = email.message_from_string(raw_email)
	print email_message['Subject']
