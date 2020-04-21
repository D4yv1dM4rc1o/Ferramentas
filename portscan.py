import socket
import sys

class color:
	LIGREEN = '\033[1;92m'
	LIRED = '\033[1;91m'
	LIBLUE = '\033[1;94m'
	LIYELLOW ='\033[1;93m'


while True:
	per = int(input('''\033[1;32m____            _   ____                  
|  _ \ ___  _ __| |_/ ___|  ___ __ _ _ __  
| |_) / _ \| '__| __\___ \ / __/ _` | '_ \ 
|  __/ (_) | |  | |_ ___) | (_| (_| | | | |
|_|   \___/|_|   \__|____/ \___\__,_|_| |_|\033[m
					Developed by: Márcio Dayvid (Github: https://github.com/D4yv1dM4rc1o)
	\033[1;94mEscolha uma opção abaixo:\033[m
	\033[92m1 - Escanear principais portas\033[m [21, 22, 23, 25, 80, 135, 8080, 443, 3306, 3389, 156, 110]
	\033[92m2 - Escanear uma porta\033[m
	\033[92m3 - Escolher as portas para Escanear\033[m (Não pode ser mais de 50 portas!)

	\033[91m99 - Fechar o programa\033[m

	\033[92mDigite a opção: \033[m'''))
	if per == 1:
		ip = input(color.LIYELLOW + "Digite o IP ou Endereço: \033[m")
		ports = [21, 22, 23, 25, 80, 135, 8080, 443, 3306, 3389, 156, 110]

		print(color.LIBLUE + '=============SCANNER INICIADO=============\033[m')
		for port in ports:
			client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			client.settimeout(0.7)
			code = client.connect_ex((ip, port))
			if code == 0:
				print('Cód:',code, '-','Port:',port, color.LIGREEN + '-> OPEN\033[m')
			else:
				print('Cód:',code, '-','Port:', port, color.LIRED + '-> CLOSE\033[m')
		print(color.LIBLUE + '============SCANNER FINALIZADO============\033[m')

	elif per == 2:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.settimeout(0.4)

		ip = input(color.LIYELLOW + "Digite o IP ou Endereço: \033[m")
		ports = int(input(color.LIYELLOW + "Digite a porta: "))
		code = client.connect_ex((ip, ports))

		print(color.LIBLUE + '=============SCANNER INICIADO=============\033[m')
		if code == 0:
			print('Cód:',code, '-','Port:', ports, color.LIGREEN + '-> OPEN\033[m')
		else:
			print('Cód:',code, '-','Port:', ports, color.LIRED + '-> CLOSE\033[m')
		print(color.LIBLUE + '============SCANNER FINALIZADO============\033[m')

	elif per == 3:
		ports = []
		count = 0
		ip = input(color.LIYELLOW + "Digite o IP ou Endereço: \033[m")
		addport = int(input(color.LIYELLOW + 'Quer scanear quantas portas? \033[m'))
		if addport <=50 and addport > 0:
			while count < addport:
				ports.append(int(input(color.LIGREEN + 'Digite a porta: \033[m')))
				count += 1
			print(color.LIBLUE + '=============SCANNER INICIADO=============\033[m')
			for port in ports:
				client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				client.settimeout(0.2)
				code = client.connect_ex((ip, port))
				if code == 0:
					print('Cód:', code, '-', 'Port:', port, color.LIGREEN + '-> OPEN\033[m')
				else:
					print('Cód:', code, '-', 'Port:', port, color.LIRED + '-> CLOSE\033[m')
			print(color.LIBLUE + '=============SCANNER FINALIZADO=============')
		elif addport <=0:
			print('Não aceitamos números menores ou igual a 0!')
		elif addport >=50:
			print('Não aceitamos números maiores que 50!')
		else:
			print('Valor inválido! por favor tente novamente.')
	elif per == 99:
		print(color.LIRED + '============FECHANDO PROGRAMA============\033[m')
		sys.exit()
	else:
		print(color.LIRED + 'Opção inválida! Tente novamente')
