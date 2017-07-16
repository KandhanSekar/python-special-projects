import poplib
import string, random
import io
import logging

SERVER = "pop.gmail.com"
USER  = "kandhan3694"
PASSWORD = "deiasgddpqthcgsu"

# connect to server
logging.debug('connecting to ' + SERVER)
server = poplib.POP3_SSL(SERVER)
#server = poplib.POP3(SERVER)

# log in
logging.debug('log in')
server.user(USER)
server.pass_(PASSWORD)
