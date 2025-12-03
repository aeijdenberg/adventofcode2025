import sys


def jolts(digits, array):
    if digits == 0:
        return 0
    if digits == 1:
        digit = max(array)
    else:
        digit = max(array[:-(digits-1)])
    return (digit * (10 ** (digits - 1))) + jolts(digits - 1, array[array.index(digit)+1:])

rv = 0
for line in sys.stdin:
    volts = [int(ch) for ch in line.strip()]
    if len(volts):
        rv += jolts(12, volts)

print(rv)
