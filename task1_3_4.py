# Валидность скобок

x = input()

def check(s):
    left1 = []
    left2 = []
    left3 = []
    right1 = []
    right2 = []
    right3 = []
    for i in range(0,len(s)):
        if s[i] == '(':
            left1 = left1 + ['(']
        elif s[i] == '[':
            left2 = left2 + ['[']
        elif s[i] == '{':
            left3 = left3 + ['{']
        elif s[i] == ')':
            if len(left1) != 0:
                right1 = right1 + [')']
        elif s[i] == ']':
            if len(left2) != 0:
                right2 = right2 + [']']
        elif s[i] == '}':
            if len(left3) != 0:
                right3 = right3 + ['}']

    if (len(left1) == len(right1)) and (len(left2) == len(right2)) and (len(left3) == len(right3)):
        return 'True'
    else:
        return 'False'

print(check(x))