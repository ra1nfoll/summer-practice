import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))


print('Введіть проміжок часу:\n\n ')

d = input('День: ')
h = input('Години: ')
m = input('Хвилин: ')
c = input('Секунди: ')

mc = int(m) * 60
hc = int(h) * 3600
dc = int(d) * 86400

mhdc = int(mc) + int(hc) + int(dc) + int(c)

print(mhdc)

printTimeStamp('\nОсередько Андрій, Ваня Жаботинський\n')


input('\n')
