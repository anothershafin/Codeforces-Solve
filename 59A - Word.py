s=input()
count=0
for i in s:
  if 64<ord(i)<91:
    count+=1
if count>(len(s)//2):
  print(s.upper())
else:
  print(s.lower())
