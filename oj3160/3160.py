"""Optimum Prime O O O A A"""
start, end = map(int, input().split())
primes = []
for n in range(start, end+1):
    if n <= 1:
        continue
    is_prime = True
    for dih in range(2, n):
        if not n % dih: # dihvision (ToT)
            is_prime = False
            break
    if is_prime:
        primes.append(n)
if primes:
    print(" ".join(map(str, primes)))
print(f"Total primes: {len(primes)}")
