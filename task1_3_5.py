#Умножение бинарных чисел в формате строк
x1 = input()
x2 = input()

y1 = int(x1, 2)
y2 = int(x2, 2)

number = y1 * y2

number = format(number , 'b')

print(number)