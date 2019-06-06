import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
a = input("Введіть букву:")
 if a == 'a' or 'e' or 'i' or 'u' or 'o':
 	print("Голосні")
elif a == 'y':
 	print("y голосна або приголосна")
elif a == 'q' or 'w' or 'r' or 't' or 'p' or 's' or 'd' or 'f' or 'g' or 'h' or ' j' or 'k' or 'l' or 'z' or 'x' or 'c' or 'v' or 'b' or 'n' or 'm':
	print("Приголосні")



 printTimeStamp('Жаботинський Іван,Осередько Андрій')
 input('\n')

