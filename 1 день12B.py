import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
gor = {
    0: 'Rat',
    1: 'Ox',
    2: 'Tiger',
    3: 'Hare',
    4: 'Dragon',
    5: 'Snake',
    6: 'Horse',
    7: 'Sheep',
    8: 'Monkey',
    9: 'Rooster',
    10: 'Dog',
    11: 'Pig',
}
print(gor[(int(input('>>> Year = ')) - 2008) % 12])
 printTimeStamp('Жаботинський Іван,Осередько Андрій')
 input('\n')
