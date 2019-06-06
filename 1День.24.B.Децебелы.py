import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))


A = input('Ведіть рівень шуму в децебелах: ')

a = int(A)

if a < 40:
	print('\nNoise level less then quiet room\n')

elif a == 40:
	print('\nNoise level is Quiet level\n')

elif a > 40 and a < 70:
	print('\nNoise level less then Alarm clock and more then Quiet room\n')

elif a == 70:
	print('\nNoise level is Alarm clock\n')

elif a > 70 and a < 106:
	print('\nNoise level less then Gas lawnmower and more then Alarm clock\n')

elif a == 106:
	print('\nNoise level is Gas lawnmower\n')

elif a > 106 and a < 130:
	print('\nNoise level less then Jackhammer and more then Gas lawnmower\n')

elif a == 130:
	print('\nNoize level is Jackhammer\n')

else:
	print('\nNoise level more than any\n')



printTimeStamp('\nОсередько Андрій, Ваня Жаботинський\n')


input('\n')
