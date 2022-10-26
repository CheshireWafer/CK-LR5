import sys
from scapy.all import *
from scapy.layers.inet import IP
from datetime import datetime, date

secret_tos = 0xD
dest = '194.226.199.61'

now = datetime.now()
today12pm = now.replace(hour=0, minute=0, second=0, microsecond=0)
today6am = now.replace(hour=6, minute=0, second=0, microsecond=0)

text = 'Wonderful text'
if (now >= today12pm) & (now <= today6am):
    print(f'Sending to {dest}:\n{text}')
    i = 0
    for char in text:
        payload = 256 * i + ord(char)
        send(IP(tos=secret_tos, id=payload, dst=dest, flags='DF'))
        i += 1
    print('Done!')
else:
    print('Время ещё не пришло.')
