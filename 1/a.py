import sys

pos = 50
password = 0
for line in sys.stdin:
    l = line.strip()
    if len(l):
        i = int(l[1:])
        if l[0] == 'R':
            i *= -1
        pos += i
        pos %= 100
        if pos == 0:
            password += 1

print(password)