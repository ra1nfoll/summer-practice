import datetime

def printTimeStamp(name):

  print('Автор програми: ' + name)

  print('Час компіляції: ' + str(datetime.datetime.now()))
print ("{:>0}{:>5}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}{:>4}".format("",1,2,3,4,5,6,7,8,9,10)) 
for i in range(1,11):
    print((i), end= '')
for j in range(1,11):
    print("%4d" % (i*j), end='')
print()
printTimeStamp('Жаботинський Іван,Осередько Андрій')
input('\n')
