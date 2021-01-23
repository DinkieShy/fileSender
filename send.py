import socket               # Import socket module

s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
port = 21                 # Reserve a port for your service.

s.connect((host, port))
s.send('Hello world!'.encode('utf-8'))
f = open('tosend.png','rb')
print('Sending...')
l = f.read(1024)
while (l):
    print('Sending...')
    s.send(l)
    l = f.read(1024)
f.close()
print("Done Sending")
s.close()                   # Close the socket when done