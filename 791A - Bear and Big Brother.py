weight=input().split()
a=int(weight[0])
b=int(weight[1])
years=0
while a<=b:
  a*=3
  b*=2
  years+=1
print(years)
