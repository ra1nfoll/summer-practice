import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))


for i in range(0, 128):
    print(chr(i), end=' ')


printTimeStamp('\nОсередько Андрій, Ваня Жаботинський\n')


input('\n')