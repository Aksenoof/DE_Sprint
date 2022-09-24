#Палиндром строки
x = str(input())
x = ''.join(x.split())
a = x[::-1]
if x == a:
  print("yes")
else:
  print("no")