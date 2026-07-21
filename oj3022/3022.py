'''Tempurature conversion'''
num = float(input("Value"))
temp1 = input("From")
temp2 = input("To")

celsius = num
if temp1 == 'K':
    celsius = num - 273.15
elif temp1 == 'F':
    celsius = (num - 32) * 5/9
elif temp1 == 'R':
    celsius = num * 5/9 - 273.15

result = celsius
if temp2 == 'K':
    result = celsius + 273.15
elif temp2 == 'F':
    result = (celsius * 9/5) + 32
elif temp2 == 'R':
    result = (celsius + 273.15) * 9/5

print(f'{result:.2f}')
