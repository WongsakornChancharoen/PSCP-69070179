"""Give to you!"""
n, s = map(int, input().split())
students = []
for _ in range(n):
    students.append(int(input()))
sent = {s:True}
count = 1
while True:
    s = students[s-1]
    if s and not sent.get(s):
        sent[s] = True
        count += 1
    else:
        break
print(count)
