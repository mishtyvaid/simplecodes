n = int(input('enter number'))
flag=False
if n>1:
    for i in range(2,n):
        if (n%i)==0:
            flag=True
            break
if flag:
    print('number entered is not prime')
else:
    print('number is prime')
