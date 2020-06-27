#!/usr/bin/env python3


import base64

ctf = '112f000c270171515165252919012d36010236250e0d26360d635303237e4f3f0e113e0b50580c3f3458096b'

#1st logic decode the string with hex- reverse order

strings=bytes.fromhex(ctf).decode('utf-8')

#ord is returns integer from unicode char
# 1st XOR with last word of the hex string  
# = base64 usually end with =

decvalue=chr(ord("=")^ord(strings[-1]))

#bitwise xor upto stringlenth-1

for n in range(len(strings)-1):
#incrementation operation
	decvalue+=chr(ord(strings[n])^ord(decvalue[n]))
	
print (decvalue) 


#echo VGhhdCB3b3VsZCBoYXZlIGJlZW4gdG9vIGVhc3kgXl4=| base64 --decode
