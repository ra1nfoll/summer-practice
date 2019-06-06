import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
water = int(input("Введіть скільки ви використали води в кубометрах: "))
if water <= 30:
  print("Ви маєте заплатити - "+str(20+(water*9.68)))
elif 30 < water <= 50:
  print("Ви маєте заплатити - "+str(20+(30*9.68)+((water-30)*11.22)))
elif 50 < water <= 60:
  print("Ви маєте заплатити - "+str(20+(30*9.68)+(20*11.22)+((water-50)*13.06)))
elif water > 60:
  print("Ви маєте заплатити - "+str(20+(30*9.68)+(20*11.22)+(10*13.06)+(water-60)*17.89))
printTimeStamp('Жаботинський Іван,Осередько Андрій')
input('\n')
