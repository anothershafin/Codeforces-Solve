n,k=map(int,input().split())
for_in range(k):
    if n % 10==0:
        n//=10
    else:
        n-=1
print(n)
