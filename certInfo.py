#!/usr/bin/python

import ssl,socket


hostname = 'google.com'
context = ssl.create_default_context()
conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)	
conn.connect((hostname, 443))
cert = conn.getpeercert()
print(cert)

