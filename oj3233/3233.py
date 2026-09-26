"""Here's come the MONEY"""
rA, rNum = input().split()
lotA, lotNum = input().split()
money = 0
if lotNum == rNum:
    money = 1000000
elif lotNum[-3:] == rNum[-3:]:
    money = 2000
elif lotNum[-2:] == rNum[-2:]:
    money = 1000
if lotA != rA:
    money //= 10
elif not money:
    money = 20
print(money)
