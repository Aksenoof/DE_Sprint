#Палиндром строки
x = str(input())

def check_palidrom(s):
  t = ''.join(s.split())
  a = t[::-1]
  if t == a:
    return True
  else:
    return False

print(check_palidrom(x))