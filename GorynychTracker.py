#!/usr/bin/env python
# Coded by Vitali
import urllib
import sqlite3
import re

u = urllib.urlopen('http://www.cybercrime-tracker.net/index.php?search=gorynych')
data = u.read().split('/>')
rdate = re.findall(r'<tr><td>([0-9-]{10})</td>', str(data))
url = re.findall(r'<td>(.{8,40})</td>\\n\\t\\t\\t\\t', str(data))
for i in url:
	url = ' '.join(url).replace('Gorynych','').split()
ip = re.findall(r'/ip-address/([0-9\.]{4,20})/information/', str(data))
rtype = []
for i in range(len(ip)):
	i = 'Gorynych'
	rtype.append(i) 
zipped = zip(rdate, url, ip, rtype)

f = open('ips.txt', 'w+')
for i in ip:
	f.write(i+'\n')
f.close()

conn = sqlite3.connect('GorynychHostTracker.sqlite')
cur = conn.cursor()
conn.text_factory = str
# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Gorynych;
CREATE TABLE Gorynych (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    rdate 	TEXT,
    url    TEXT UNIQUE,
    ip		TEXT,
    rtype	TEXT
);
''')

for element in zipped:
	rdate = element[0]
	url = element[1]
	ip = element[2]
	rtype = element[3]

	cur.execute('''INSERT OR IGNORE INTO Gorynych (rdate, url, ip, rtype) VALUES ( ?, ?, ?, ? )''', ( rdate, url, ip, rtype ) )
    #cur.execute('SELECT id FROM Hosts WHERE name = ? ', ( name, ))

conn.commit()