import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
num = int(input("Введіть чотиризначні числа: "))
g = num //1000
a = (num - g*1000)//100
b = (num - g*1000 - a*100)//10
c = num - g*1000 - a*100 - b*10
print("Сума цифр у номері", g+a+b+c)
 printTimeStamp('Жаботинський Іван,Осередько Андрій')
 input('\n')