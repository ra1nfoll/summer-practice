import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
year = int(input())
if year % 4 != 0:
	print("невисокосний")

elif year % 400 == 0:
	print("невисокосний")
if year % 100 == 0:
	print("високосний")

else:
	print("високосний")
printTimeStamp('Жаботинський Іван,Осередько Андрій')
input('\n')
