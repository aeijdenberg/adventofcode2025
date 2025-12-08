import sys

lines = [x.strip() for x in sys.stdin]
rv = 0
for idx, line in enumerate(lines):
    if 'S' in line:
        beams = [False] * len(line)
        beams[line.index('S')] = True
    else:
        for cidx, ch in enumerate(line):
            if ch == '^':
                if beams[cidx]:
                    rv += 1
                    beams[cidx] = False
                    if cidx > 0:
                        beams[cidx-1] = True
                    if cidx < len(beams) - 1:
                        beams[cidx+1] = True

print(rv)