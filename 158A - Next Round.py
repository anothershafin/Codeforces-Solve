x=input()
x=x.split()
n=int(x[0])
k=int(x[1])
if (1<=k<=50) and (1<=n<=50) and (k<=n):
    y=input()
    y=y.split()
    test=int(y[k-1])
    result=0
    for i in y:
        if int(i)==0:
            break
        if int(i) >= test:
            result+=1
            
    print(result)
