import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))



ALPHA = "".join(map(chr, range(ord(" "), ord("я") + 1)))
 
def encode(text, step):
    return text.translate(
        str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))
 

b = input('Введіть значення ссуву: ')


a = input('Ввод: ')

print(encode(a, int(b)))

printTimeStamp('\nОсередько Андрій, Ваня Жаботинський\n')


input('\n')