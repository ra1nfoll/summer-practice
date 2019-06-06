import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))


a = input('Введіть велbчену в сантиметрах: ')

D = float(a) * 0.39

F = D / 12

print('Дюйми: ' + str(D))

print('Фути' + str(F))

printTimeStamp('\nОсередько Андрій, Ваня Жаботинський\n')


input('\n')