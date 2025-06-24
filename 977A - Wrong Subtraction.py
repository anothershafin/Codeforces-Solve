n=input().split()
out=n[0]
for i in range(int(n[1])):
  if out[-1]=="0":
    out=out[:-1]
  else:
    out=str(int(out)-1)
print(out)
