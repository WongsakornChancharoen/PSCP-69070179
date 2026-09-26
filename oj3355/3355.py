"""Short king"""
short = []
prev = None
a, b = None, None
while True:
    n = int(input())
    if n == -1:
        if a == b:
            short.append(a)
        else:
            short.append(f"{a}-{b}")
        break
    if prev is None:
        prev = n
        a, b = n, n
        continue
    if prev == n-1:
        b = n
    else:
        if a == b:
            short.append(a)
        else:
            short.append(f"{a}-{b}")
        a, b = n, n
    prev = n
if len(short) > 1 or short[0] is not None:
    print(", ".join(map(str, short)))
