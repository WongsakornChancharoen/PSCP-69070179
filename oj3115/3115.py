"""Store check"""
num, check = map(int, input().split())
stores = []
for i in range(num):
    if not i or i:
        start, stop = map(int, input().split())
        stores.append([start, stop])
check_times = input().split()
results = []
for i in range(check):
    count = 0
    for openTime in stores:
        if openTime[0] <= int(check_times[i]) < openTime[1]:
            count += 1
    results.append(count)
print(" ".join(str(num) for num in results))
