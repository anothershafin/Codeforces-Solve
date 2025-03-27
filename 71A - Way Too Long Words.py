n=int(input())
if (1<=n<=100):
    for i in range(n):
        a=input()
        if (len(a)<=10):
            print(a)
        elif(10<=len(a)<=100):
            out=a[0]+str(len(a)-2)+a[-1]
            print(out)
