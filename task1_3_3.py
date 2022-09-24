#Перевод арабского числа в римское
number = str()
number1 = str()
number2 = str()
number3 = str()
number4 = str()

x = int(input())
# тысячные
if x >= 1000:
	y = x // 1000
	for i in range(y):
		number1 = number1 + 'M'
		x = x - 1000
# сотые
if 100 <= x <= 399:
	y = x // 100
	for i in range(y):
		number2 = number2 + 'C'
		x = x - 100
elif 400 <= x <= 499:
	number2 = 'CD'
	x = x - 400
if 500 <= x <= 599:
	number2 = 'D'
	x = x - 500
elif 600 <= x <= 899:
	x = x - 500
	y = x // 100
	number2 = 'D'
	for i in range(y):
		number2 = number2 + 'C'
		x = x - 100
elif 900 <= x <= 999:
	number2 = 'CM'
	x = x - 900
# десятичные
if 10 <= x <= 39:
	y = x // 10
	for i in range(y):
		number3 = number3 + 'X'
		x = x - 10
elif 40 <= x <= 49:
	number3 = 'XL'
	x = x - 40
elif 50 <= x <= 59:
	number3 = 'L'
	x = x - 50
elif 60 <= x <= 89:
	x = x - 50
	y = x // 10
	number3 = 'L'
	for i in range(y):
		number3 = number3 + 'X'
		x = x - 10
elif 90 <= x <= 99:
	number3 = 'XC'
	x = x - 90
# еденичные
if 1 <= x <= 3:
	for i in range(x):
		number4 = number4 + 'I'
		x = x - 1
elif x == 4:
	number4 = 'IV'
	x = x - 4
elif x == 5:
	number4 = 'V'
	x = x - 5
elif 6 <= x <= 8:
	x = x - 5
	number4 = 'V'
	for i in range(x):
		number4 = number4 + 'I'
		x = x - 1
elif x == 9:
	number4 = 'IX'
	x = x - 9

number = number1 + number2 + number3 + number4

print(number)
