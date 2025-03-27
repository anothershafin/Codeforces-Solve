n=int(input())
if (1<=n<=1000):
    count=0
    for i in range (n):
        a=input()
        l1=a.split(" ")
        summ=int(l1[0])+int(l1[1])+int(l1[2])
        if(summ>1):
            count+=1
    print(count)
