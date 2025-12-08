import re
import sys

lines = [l[:-1] for l in sys.stdin]

nums = []
row = None
for l2 in zip(*(lines[:-1])):
    pot_num = (''.join(l2).strip())
    if len(pot_num):
        if row is None:
            row = []
            nums.append(row)
        row.append(int(pot_num))
    else:
        row = None

rv = 0
for col, op in enumerate(re.split(' +', lines[-1].strip())):
    if op == '+':
        ca = 0
        for cv in nums[col]:
            ca += cv
    else:
        ca = 1
        for cv in nums[col]:
            ca *= cv
    rv += ca

print(rv)
