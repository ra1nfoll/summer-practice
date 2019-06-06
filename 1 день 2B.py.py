import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
num = int(input("Введіть магнітуду:"))
if (0<num<2.0):
  print("Мікро")
if (2.0<=num<3.0):
  print("Дуже слабкий")
if (3.0<=num<4.0):
  print("Слабкий")
if (4.0<=num<5.0):
  print("Легкий")
if (5.0<=num<6.0):
  print("Помірний")
if (6.0<=num<7.0):
  print("Сильний")
if (7.0<=num<8.0):
  print("Дуже сильний")
if (8.0<=num<10.0):
  print("Великий")
if (num>=10.0):
  print("Рідкісно великий")
if (num<=0):
  print("Немаэ")
printTimeStamp('Жаботинський Іван,Осередько Андрій')
input('\n')
