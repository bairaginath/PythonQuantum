__author__ = 'veradocs-web'

import urllib2
for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print line



import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org', """To: jcaesar@example.org ... From: soothsayer@example.org
...
... Beware the Ides of March.
... """)
server.quit()

