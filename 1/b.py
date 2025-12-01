import sys

pos = 50
password = 0
for line in sys.stdin:
    l = line.strip()
    if len(l):
        i = int(l[1:])
        if l[0] == 'R':
            i *= -1
        for _ in range(int(l[1:])):
            if l[0] == 'R':
                pos -= 1
            else:
                pos += 1
            pos %= 100
            if pos == 0:
                password += 1

print(password)
