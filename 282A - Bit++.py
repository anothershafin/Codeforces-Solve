n=int(input())
if 1<=n<=150:
    x=0
    for _ in range(n):
        y=input()
        if "++" in y:
            x+=1
        else:
            x-=1
    print(x)
