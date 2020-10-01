large-numbersonly-last-digit-to-be-printed
n = int(input())

if n<=1:
    print(n)  
    quit()
lesser = (n+2)%60
if lesser==1:
    print(0)
    quit()
elif lesser==0:
    print(9)
    quit()
def fibo(n):
    a,b = 0, 1
    for _ in range(2,lesser+1):
        k = a+b
        k = k%10
        b, a = k, b
    if k!=0:
        print(k-1)
    else:
        print(9)
fibo(lesser)
