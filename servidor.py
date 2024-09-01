import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8888))

servidor.listen()
cliente, end = servidor.accept()

terminado = False

print('Chat iniciado')

while not terminado:
    msg = cliente.recv(1024).decode('utf-8')

    if msg == 'sair':
        terminado = True
    else:
        print(msg)
    cliente.send(input('Mensagem: ').encode('utf-8'))

cliente.close()
servidor.close()