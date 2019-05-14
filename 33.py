a=int(input('N='))
l={'','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
c=a-1
b=1
for i in range (a+1):
    a-=1
    print(' '+(a+1),'#'*i)
for i in range(c,-1,-1):
    print(' '+b,'#'*i)
