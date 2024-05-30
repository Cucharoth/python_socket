import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('port here', 9999)) # Reemplazar por la IP que corresponda

nombre = input('Ingrese su nombre: ')

while True:
    mensaje = ''
    while not mensaje:
        mensaje = input('<<< ')
    if mensaje == '\salir':
        break
    s.send(f'{nombre}: {mensaje}'.encode())
    print(f'>>> {s.recv(1024).decode()}')

print('Sesión terminada.')
s.close()