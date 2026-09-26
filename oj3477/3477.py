"""Pad Thai"""
ingredients = ["Pad Thai Sauce","Tofu","Pickle Turnip",\
    "Shrimp","Bean Sprouts","Noodle","Chives","Lime","Egg",\
    "Oil","Peanuts"
]
flavors = ["Sweet","Sour","Salty"]
my_flavors = []
my_ingredients = []
not_pad_thai = False
while True:
    item = input()
    if item == "Cook":
        break
    if item not in ingredients:
        not_pad_thai = True
    if item not in my_ingredients:
        my_ingredients.append(item)
while True:
    taste = input()
    if taste == "End":
        break
    if taste not in my_flavors:
        my_flavors.append(taste)
if not_pad_thai:
    print("This is not Pad Thai!!!")
elif my_ingredients != ingredients:
    print("This is bad!")
elif my_ingredients == ingredients:
    if my_flavors == flavors:
        print("Delicious!")
    else:
        print("Not Bad...")
