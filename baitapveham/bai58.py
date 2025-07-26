n=int(input())
def snt(x):
    if(x==2 or x==3):
        return 1
    if(x<2 or x%2==0 or x%3==0):
        return 0
    i=5
    while(i*i<=x):
        if(x%i==0 or x%(i+2)==0):
            return 0
        i+=6
    return 1
if(snt(n)):
    print(True)
else:
    print(False)
