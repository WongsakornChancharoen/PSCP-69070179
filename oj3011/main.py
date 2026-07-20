'''Colors Mixing'''
def main():
    '''Color Mixing'''
    mix_colors = {
        "red": {"yellow": "Orange", "blue":"Violet", "red":"Red"},
        "yellow": {"red": "Orange", "blue":"Green", "yellow":"Yellow"},
        "blue": {"yellow": "Green", "red":"Violet", "blue":"Blue"}
    }

    aColor = input("Enter color A").lower().strip()
    bColor = input("Enter color B").lower().strip()

    if aColor in mix_colors:
        if bColor in mix_colors[aColor]:
            print(mix_colors[aColor][bColor])
        else:
            print("Error")
    else:
        print("Error")
main()
