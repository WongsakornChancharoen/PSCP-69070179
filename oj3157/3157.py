"""Scoreeee"""
n = int(input())
total = 0
for i in range(n):
    if i < 0:
        break
    if input() == "+":
        total += 10
    else:
        total -= 5
print(total)
