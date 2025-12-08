import sys

rolls = {}
for row, l in enumerate(sys.stdin):
    for col, ch in enumerate(l.strip()):
        if ch == '@':
            rolls['%d_%d' % (row, col)] = True

def adjacents(rolls, key):
    y, x = [int(x) for x in key.split('_')]
    rv = -1 # don't count self
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if rolls.get('%d_%d' % (y + dy, x + dx), False):
                rv += 1
    return rv

rv = 0
for candidate in rolls:
    if adjacents(rolls, candidate) < 4:
        rv += 1

print(rv)
    