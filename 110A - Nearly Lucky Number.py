n=input()
count=0
for i in n:
  if i=="4" or i=="7":
    count+=1
if all(c in "47" for c in str(count)) and count != 0:
    print("YES")
else:
    print("NO")
