import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Socket criado com sucesso!')

host = 'localhost'
port = 5432

s.bind((host, port))
msg = 'Server: Connected'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Send message...')
        s.sendto(dados + (msg.encode()), end)