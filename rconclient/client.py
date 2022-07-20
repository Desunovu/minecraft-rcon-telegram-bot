# effect give AndTheSeal minecraft:weakness 1 2 true

import os
import socket
import mcrcon

from dotenv import load_dotenv

# .env
load_dotenv()

host = os.environ.get('HOST')
port = int(os.environ.get('PORT'))
password = os.environ.get('PASSWORD')
admins = os.environ.get('ADMINS').split('+')
print(admins, host, port, password)

client = mcrcon.MCRcon(host=host, password=password, port=port)