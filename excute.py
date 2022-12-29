'''import sys
print("user version",sys.version)'''
import socket
hostname=socket.gethostname()
print(hostname)
ipad=socket.gethostbyname(hostname)
print(ipad)