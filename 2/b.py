import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def dividers(n):
    rv = []
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            rv.append(i)
    return rv

def invalid(s):
    for d in dividers(len(s)):
        if invalid_with(s, d):
            return True
    return False
        
def invalid_with(s, d):
    first, s = s[:d], s[d:]
    while s:
        if s[:d] != first:
            return False
        s = s[d:]
    return True

rv = 0
for line in sys.stdin:
    for part in line.strip().split(','):
        if len(part):
            first, last = (int(x) for x in part.split('-'))
            for i in range(first, last + 1):
                if invalid(str(i)):
                    rv += i

print(rv)
