import sys

rv = 0
for line in sys.stdin:
    for part in line.strip().split(','):
        if len(part):
            first, last = (int(x) for x in part.split('-'))
            for i in range(first, last + 1):
                s = str(i)
                if len(s) % 2 == 0:
                    if s[:len(s)//2] == s[len(s)//2:]:
                        rv += i
print(rv)
