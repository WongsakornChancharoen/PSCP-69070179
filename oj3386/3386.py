"""Duplicateeee"""
n, m = int(input()), int(input())
a, b = set(), set()
for _ in range(n):
    a.add(int(input()))
for _ in range(m):
    b.add(int(input()))
a.intersection_update(b)
if a:
    for d in sorted(a, reverse=True):
        print(d)
else:
    print("Nope")
