name=input()
count=0
temp=[]
for i in name:
  if i not in temp:
    temp.append(i)
    count+=1

if count%2==0:
  print(f"CHAT WITH HER!")
else:
  print(f"IGNORE HIM!")
