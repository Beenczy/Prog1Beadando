#beker szamokat amig 0-t nem kap es eldonti hogy paros vagy paratlan

n=int(input('Give me a number:'))
while n!=0:
    if n%2==0:
        print('The given numer is even')

    else:
        print('The given numer is odd')
    n = int(input('Give me a number:'))

