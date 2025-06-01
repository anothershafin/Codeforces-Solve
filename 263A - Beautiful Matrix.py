pos=[]
for i in range(5):
  row=input().split()
  if "1" in row:
    for j in range(len(row)):
      if row[j]=="1":
        pos=[i,j]
        break

moves=abs(pos[0]-2)+abs(pos[1]-2)
print(moves)
