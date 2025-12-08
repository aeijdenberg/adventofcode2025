import re
import sys

nums = []
for l in sys.stdin:
    bits = re.split(' +', l.strip())
    if bits[0] in ['+', '*']:
        rv = 0
        for col, op in enumerate(bits):
            if op == '+':
                ca = 0
                for row in nums:
                    ca += row[col]
            else:
                ca = 1
                for row in nums:
                    ca *= row[col]
            rv += ca
        print(rv)
    else:
        nums.append([int(x) for x in bits])