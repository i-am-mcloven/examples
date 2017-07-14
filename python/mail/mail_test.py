#!/usr/bin/python

import smtplib

#
# SMTP: west.mail.splunk.com
# SMTP port: 587
# Connection sec: STARTTLS
#

sender = 'fe_kh@splunk.com'
receivers = ['kbaker@splunk.com', 'dflexer@splunk.com' ]

message = """From: Knowlege Harvesting <fe_kh@splunk.com>
To: All the squishy humans
Subject: Field Eng: Knowledge Harvesting test 

This is a test e-mail message, enjoy it :)
"""

try:
    s = smtplib.SMTP ('west.mail.splunk.com')
    s.set_debuglevel(True)
    s.starttls()
    s.ehlo()
    s.login ('email@domain.com', 'password')
    s.sendmail (sender, receivers, message)
    s.quit()

    print "Successfully sent email"


except smtplib.SMTPException as e :
    print "Error: unable to send email"
    print e

