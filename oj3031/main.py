'''Bendy was a little devil thing'''
import math
def main():
    """It's Bendy and the Ink Machine"""
    pi = 3.1416

    s, n = input().split(" ")
    s = int(s)
    n = int(n)

    pos = []
    for _ in range(n):
        x, y = input().split(" ")
        x = int(x)
        y = int(y)

        pos.append((x, y))

    total = 0
    for p in pos:
        dist = p[0] ** 2 + p[1] ** 2
        total += math.ceil((dist / s) * pi) - total
        print(total)
main()
