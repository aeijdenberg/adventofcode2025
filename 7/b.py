import sys
from functools import lru_cache

all_lines = [x.strip() for x in sys.stdin]
lines = all_lines[1:]

@lru_cache(maxsize=None)
def count_quantum(pos, row):
    if row == len(lines):
        return 1
    if lines[row][pos] == '^':
        rv = 0
        if pos > 0:
            rv += count_quantum(pos-1, row+1)
        if pos < (len(lines[row])-1):
            rv += count_quantum(pos+1, row+1)
        return rv
    else:
        return count_quantum(pos, row+1)

print(count_quantum(all_lines[0].index('S'), 0))
