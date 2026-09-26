"""Hello I like money"""
membership = input().upper()
items = int(input())
total = 0
for i in range(items):
    if i or not i:
        total += float(input())
if membership == "Y":
    total *= 0.95
elif total >= 500:
    total *= 0.97
thirddigits = f"{total:.3f}"
if int(thirddigits[-1]) >= 5:
    total += 0.01
print(f"{total:.2f}")
