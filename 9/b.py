import sys

class LineInfo(object):
    def __init__(self):
        self.bits = []
    def addCrossover(self, left, right):
        self.bits.append([left, right])
    def finished(self):
        self.bits.sort(key=lambda x: x[0])
        self.ranges = []
        inside = False
        startIn = None
        for bit in self.bits:
            if inside:
                self.ranges.append([startIn, bit[1]])
                inside = False
            else:
                inside = True
                startIn = bit[0]
        self.bits = None
    def fits(self, left, right):
        for r in self.ranges:
            if r[0] <= left and left <= r[1]:
                return r[0] <= right and right <= r[1]
            if r[1] >= right:
                return False
        return False

coords = []
for line in sys.stdin:
    coords.append([int(z) for z in line.strip().split(',')])

lineInfos = {}

last = coords[-1]
for c in coords:
    if last[0] == c[0]: # vertical
        top, bottom = min(last[1], c[1]), max(last[1], c[1])
        for y in range(top+1, bottom):
            if y not in lineInfos:
                lineInfos[y] = LineInfo()
            lineInfos[y].addCrossover(c[0], c[0])
    else: # horizontal
        left, right = min(last[0], c[0]), max(last[0], c[0])
        if c[1] not in lineInfos:
            lineInfos[c[1]] = LineInfo()
        lineInfos[c[1]].addCrossover(left, right)
    last = c

for v in lineInfos.values():
    v.finished()


def checkRect(left, top, right, bottom):
    for y in range(top, bottom+1):
        if not lineInfos[y].fits(left, right):
            return False
    return True


best = 0
for i, c1 in enumerate(coords):
    for c2 in coords[i+1:]:
        left, top = min(c1[0], c2[0]), min(c1[1], c2[1])
        right, bottom = max(c1[0], c2[0]), max(c1[1], c2[1])
        score = (right - left + 1) * (bottom - top + 1)
        if score > best:
            if checkRect(left, top, right, bottom):
                best = score

print(best)