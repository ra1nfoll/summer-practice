import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))


R = input('Звичайду сестему(1) чи Американську(2) ?')
r = int(R)
  


if r == 1:
	a = input('Введіть свою масу: ')
	b = input('Введіть свій зріст: ')

	d = float(b) * float(b)

	c = float(a) / float(d)

	print(c)

elif r == 2:
	a = input('Введіть свою масу: ')  # фуyn      
	b = input('Введіть свій зріст: ')     # дюйми

	F = float(a) * 2.2046
	D = float(b) * 39.370

	d = float(D) * float(D)

	c = float(F) / float(d) * 703

	print(c)

else:
	print('')


 

printTimeStamp('\nОсередько Андрій, Ваня Жаботинський\n')


input('\n')