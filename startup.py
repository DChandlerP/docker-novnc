import secrets
import os

# x11vnc.conf only seems to accept a password stored in this directory
os.system("mkdir /root/.vnc")
#randomly generated hexadecimal password. 4 bytes = 8 characters
password = secrets.token_hex(4)
format = 'Your Password is: {}'.format(password)
print(format)

# saves password in the correct dir created above
str = 'echo {} >> /root/.vnc/passwd'.format(password)
os.system(str)

os.system("supervisord -c /app/supervisord.conf")






