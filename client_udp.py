import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('Client socket criado com sucesso!')

host = 'localhost'
porta = 5433
msg = 'Welcome to server!\n'

try:
    print('Client: ' + msg)
    s.sendto(msg.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Client: ' + dados)
finally:
    print('Client: Fechando conexão...')
    s.close()