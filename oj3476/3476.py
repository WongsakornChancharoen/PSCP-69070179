"""Kawaii"""
import json
def main():
    """Main fucction"""
    animals = {"Garfield":"Cat01","Fubuki":"Fox01"}
    for _ in range(int(input())):
        data = json.loads(input())
        name, code = list(data.items())[0]
        keys_to_remove = [k for k, v in animals.items() if v == code]
        for k in keys_to_remove:
            animals.pop(k)
        animals[name] = code
    cat, fox = {}, {}
    cat_count, fox_count = 0, 0
    for k, v in animals.items():
        if v.lower().startswith("cat"):
            cat_count += 1
            cat[k] = v
        elif v.lower().startswith("fox"):
            fox_count += 1
            fox[k] = v
    cat = list(sorted(cat.items(), key=lambda item: int(item[1][3:])))
    fox = list(sorted(fox.items(), key=lambda item: int(item[1][3:])))
    animals = dict(cat + fox)
    print(f"Cat : {cat_count}")
    print(f"Fox : {fox_count}")
    for key, value in animals.items():
        print(f"{key} : {value}")
main()
