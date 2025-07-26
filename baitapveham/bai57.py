n=int(input())
def gt(n):
    tich=1
    for i in range(1,n+1):
        tich*=i
    return tich
print(gt(n))
