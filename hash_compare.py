import hashlib

arquivo1 = str(input('Informe o primeiro arquivo a ser comparado: '))
arquivo2 = str(input('informe o segundo arquivo a ser comparado: '))

hash1 = hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}')
    print('O hash do primeiro arquivo é: ', hash1.hexdigest())
    print('O hash do segundo arquivo é: ', hash2.hexdigest())
else:
    print(f'O arquivo: {arquivo1} é igual o arquivo: {arquivo2}')
    print('O hash do primeiro arquivo é: ', hash1.hexdigest())
    print('O hash do segundo arquivo é: ', hash2.hexdigest())