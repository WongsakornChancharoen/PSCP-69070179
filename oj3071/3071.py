"""Numbers"""
def main():
    """hello my skibidi"""
    a = int(input())
    b = int(input())
    d = int(input())
    r = int(input())
    count = 0
    for x in range(a, b+1):
        if x % d == r:
            count += 1
    print(count)
main()
