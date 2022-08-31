#Lib socket: fornece acesso de baixo nível à interface de rede
#Lib SYS: fornece acesso a algumas variaveis e algumas funções que tem interações com o interpretador

import socket
import sys

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou!')
        print('Erro: {}'.format(e))
        sys.exit()

    print('Socket criado com sucesso!')

    HostAlvo = input('Informe o host ou IP alvo: ')
    PortaAlvo = input('Informe a porta: ')

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print('Client TCP conectado com sucesso!')
        s.shutdown(2)
    except socket.error as e:
        print('A conexão falhou :(')
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == "__main__":
    main()
    