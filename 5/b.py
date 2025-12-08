import sys


class Ranges(object):
    def __init__(self):
        self.all = set()
        self.points = set()

    def add(self, start, end):
        self.all.add('%d-%d' % (start, end))
        self.points.add(start)
        self.points.add(end)
        
    def count(self):
        sorted_points = list(self.points)
        sorted_points.sort()
    
        tbc = set()
        for r in self.all:
            start, end = [int(x) for x in r.split('-')]
            last = None
            for sp in sorted_points:
                if last is not None:
                    if start <= last and end >= sp:
                        tbc.add('%d-%d' % (last, sp))
                last = sp

        rv = 0
        for r in tbc:
            start, end = [int(x) for x in r.split('-')]
            rv += end - start
        return rv

r = Ranges()
for l in sys.stdin:
    l = l.strip()
    if len(l):
        if '-' in l:
            start, end = [int(x) for x in l.split('-')]
            r.add(start, end+1)

print(r.count())
