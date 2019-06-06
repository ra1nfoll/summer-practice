import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))



a = input('Введiть Буквенну оцінку: ')

if a == 'A+':
	print('>4.0')

elif a == 'A':
	print('4.0')

elif a == 'A-':
	print('3.7')

elif a == 'B+':
	print('3.3')

elif a == 'B':
	print('3.0')

elif a == 'B-':
	print('2.7')

elif a == 'C+':
	print('2.3')

elif a == 'C':
	print('2.0')

elif a == 'C-':
	print('1.7')

elif a == 'D+':
	print('1.3')

elif a == 'D':
	print('1.0')

elif a == 'F':
	print('0')

else:
	print('Не вірний ввод')		



printTimeStamp('\nОсередько Андрій, Ваня Жаботинський\n')


input('\n')					