import time
import gevent
import gevent.monkey
gevent.monkey.patch_all()
import socket
import serial

s = serial.Serial("/dev/ttyACM0", 115200)
def client():
  client_socket = gevent.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_socket.connect(("127.0.0.1", 6000))
  t0 = time.time()
  while True:
    data = client_socket.recv(1024)
    try:
        value = int(data)
    except:
        print "failed to parse", data
    else:
        adj = value / 10
        print adj
        if (adj > 99): adj=99
        s.write("%d\r\n" % adj)
        s.flush()

client = gevent.spawn(client)

gevent.joinall([client])
