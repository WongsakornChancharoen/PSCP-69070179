"""It was THIS BIG"""
n = int(input())
res = "YES" if n != 1 else "NO"
for div in range(2, int(n ** 0.5)+1):
    if n / div == n // div:
        res = "NO"
        break
print(res)
