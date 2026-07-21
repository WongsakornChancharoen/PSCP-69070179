'''Bill'''
price = int(input('Enter price'))
serviceprice = max(min(price * 0.1, 1000), 50)
vat = (price + serviceprice) * 0.07
total = price + serviceprice + vat

print(f"{total:.2f}")
