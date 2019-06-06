import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
TGR = 13.12
fac1 = 0.6215
fac2 = -11.37 
fac3 = 0.3965
DRG = 0.16

temp = float(input("Введіть температуру повітря(в Цельсіях): "))
speed = float(input("Введіть швидкість вітру(км/год): "))

tfd = TGR + (fac1 * temp) + (fac2 * speed ** DRG) + (fac3 * temp * speed ** DRG)

print("Ваш індекс вітру ","%d"%(tfd))
printTimeStamp('Жаботинський Іван,Осередько Андрій')
input('\n')
