import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
num1 = int(input("Введіть першу цифру : "))
num2 = int(input("Введіть другу цифру : "))
num3 = int(input("Введіть третю цифру : "))
num4 = int(input("Введіть четверту цифру : "))
num5 = int(input("Введіть пяту цифру : "))
num6 = int(input("Введіть шосту цифру : "))
num7 = int(input("Введіть сьому цифру : "))
num8 = int(input("Введіть восьмуцифру : "))
num9 = int(input("Введіть девяту цифру : "))
num10 = int(input("Введіть десяту цифру : "))
num11 = int(input("Введіть одинадцяту цифру : "))
num12 = int(input("Введіть дванадцяту цифру : "))

nepar_sum = num1 + num3 + num5 + num7 + num9 + num11
par_sum = num2 + num4 + num6 + num8 + num10 + num12
par_sum_times3 = par_sum*3
total_nepar_par_times3=nepar_sum + par_sum_times3
total_rem10 = total_nepar_par_times3 % 10

if total_rem10 == 0:
  isbn13 = 0
else:
  isbn13 = 10 -total_rem10
print("Перевірочною цифрою є : ", isbn13)
printTimeStamp('Жаботинський Іван,Осередько Андрій')
input('\n')
