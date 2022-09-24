def check(s):
	result = 0
	result1 = 0
	result2 = 0
	result3 = 0
	for i in range(len(s)):
		if "(" in i:
			result1 += 1
		elif ")" in i:
			result1 -= 1
		if "[" in i:
			result2 += 1
		elif "]" in i:
			result2 -= 1
		if "{" in i:
			result3 += 1
		elif "}" in i:
			result3 -= 1
		result = result1 + result2 + result3

	if result != 0:
		print('False')
	else:
		print('TRUE')
