"""Giraffe"""
n = int(input())
giraf = []
for _ in range(n):
    giraf.append(int(input()))
count = 0
for i in range(n):
    left = giraf[i - 1] if i - 1 >= 0 else 0
    right = giraf[i + 1] if i + 1 < n else 0
    if right < giraf[i] > left:
        count += 1
print(count)
