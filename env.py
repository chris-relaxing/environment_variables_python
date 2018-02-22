#!/usr/bin/python

import os

print "Content-type: text/html\n\n";
print "<html><head>"
print "<font size=+2><B>Environment Variables</B></font><br><br>";
for param in os.environ.keys():
  print "\n\n<b>%20s</b>: %s<br>" % (param, os.environ[param])

print "<BR><BR><BR>"
print "</head><body>"
print ""
print "</body></html>"

