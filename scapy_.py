'''ip=IP()
print(ip)
print(ip.show())
my_frame=Ether()/ICMP()
print(my_frame)
print(my_frame.show())
from scapy.all import *
s=IP(dst="google.com")/ICMP()
print(s.show())
a=IP(ttl=10)
a.dst="192.168.1.1"
var=a.src
print(var.show())
from scapy.all import *
del(a.ttl)
print(a.show())
b=IP()
print(b.show())'''
from scapy.all import *
'''c=IP()/TCP()
print(c.show())
d=Ether()/IP()/TCP()
print(d.show())
e=IP()/TCP()/"GET / HTTP/1.0\r\n\r\n"
print(e.show())
j=a=Ether()/IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"
print(hexdump(j))'''
k=IP(dst="www.google.com/20")
dst=Net('www.google.com/20')
print([p for p in k])