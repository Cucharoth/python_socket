import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('140.238.181.83', 9999))

nombre = input('<<< Ingrese su nombre: ')
estado = input('<<< Ingrese su estado: ')
s.send(f'{nombre}:{estado}'.encode())
print(f'>>> {s.recv(1024).decode()}')

while True:
	mensaje = ''
	while not mensaje:
		mensaje = input('<<< ')
	s.send(mensaje.encode())
	if mensaje == '\salir':
		break
	print(f'>>> {s.recv(1024).decode()}')

print('Sesión terminada.')
s.close()