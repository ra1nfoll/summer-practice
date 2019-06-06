import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))



print('Перевод из температури в Цельсіях, в Кельвіни та Фаренгейти')


a = input('Введіть температуру в Цельсіях:')

bor = 9 / 5

t = 32

K = float(a) - 273.15 

F = float(a) * float(bor) + float(t)



print('\nТемпература в Фаренгейтах: ' + str(F))

print('\nТемпература в Кельвінах: ' + str(K))

printTimeStamp('\nОсередько Андрій, Ваня Жаботинський\n')


input('\n')
