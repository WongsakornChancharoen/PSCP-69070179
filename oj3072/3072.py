"""AEIOU"""
def main():
    """Squid games"""
    vow = ["a", "e", "i", "o", "u"]
    existingVows = {}
    for c in input():
        if c.lower() in vow:
            if not c.lower() in existingVows:
                existingVows[c.lower()] = 1
            else:
                existingVows[c.lower()] += 1
    for v in vow:
        if v in existingVows:
            print(f"{v} : {existingVows[v]}")
main()
