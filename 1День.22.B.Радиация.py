import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))



A = input('Введть частоту радiаiї: ')

a = int(A)

if  a >= 0 and a < 3 * 10**9:
	print('\nIt\'s radio waves \n')

elif a > 3 * 10**9 and a < 3 * 10**12:
	print('\nMicrowaves\n')

elif a > 3 * 10**12 and a < 4.3 * 10**4:
	print('\nInfrared light\n')

elif a > 4.3 * 10**14 and a < 7.5 * 10**14:
	print('\nVisible light\n')

elif a > 7.5 * 10**14 and a < 3 * 10**17:
	print('\nUltraviolet light\n')

elif a > 3 * 10**17 and a < 3 * 10**19:
	print('\nX-rays\n')

elif a > 3 * 10**19:
	print('\nGamma rays\n')

else:
	print('Не вiрний ввод')		


printTimeStamp('\nОсередько Андрій, Ваня Жаботинський\n')


input('\n')