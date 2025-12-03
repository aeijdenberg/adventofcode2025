import sys

rv = 0
for line in sys.stdin:
    volts = [int(ch) for ch in line.strip()]
    if len(volts):
        fd = max(volts[:-1])
        fi = volts.index(fd)
        sd = max(volts[fi+1:])
        rv += (fd*10) + sd

print(rv)
