"""Frog Kob"""
x, y = map(int, input().split())
d = 0
i = 0
for j in range(x, 0, -2):
    d += j
    i += 1
    if d >= y:
        print(i)
        break
if d < y:
    print(-1)
