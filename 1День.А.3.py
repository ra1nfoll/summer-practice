import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))


a = input('Введiть букви на англiйськiй мовi: ')

if a == 'a' or a == 'o' or a == 'u' or a == 'e' or a == 'i':
	print('Ця буква голосна\n')

elif a == 'y':
 	print('y – голосна, а iнколи -  приголосна\n')

elif a == 'q' or a == 'w' or a == 'r' or a == 't' or a == 'p' or a == 's' or a == 'd' or a == 'f' or a == 'g' or a == 'h' or a == 'j' or a == 'k' or a == 'l' or a == 'z' or a == 'x' or a == 'c' or a == 'v' or a == 'b' or a == 'n' or a == 'm':
	print('Ця буква приголосна\n')  
else:
	print('Не вiрний ввод\n')		



printTimeStamp('\nОсередько Андрій, Ваня Жаботинський\n')

input('\n')
