"""Sea of Thieves"""
n, k, t = map(int, input().split())
i = 0
r = 0
while not r or i:
    if i == t-1:
        r += 1
        break
    r += 1
    i = (i + k) % n
print(r)
