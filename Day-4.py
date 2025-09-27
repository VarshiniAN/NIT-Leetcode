def digitsum(n):
    s=0
    while(n>0):
        a=n%10
        s+=a*a
        n=n//10
    return s
def HappyNum(n):
    if (n<=0):
        return False
    t=digitsum(n)
    while (t!=1 and t!=4):
        t=digitsum(t)
    return t==1
n=int(input())
if(HappyNum(n)):
    print("true")
else:
    print("false")
