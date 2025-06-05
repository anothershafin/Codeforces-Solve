word=input()
if 65<=ord(word[0])<=90:
  print(word)
else:
  print(chr(ord(word[0])-32)+word[1:])
