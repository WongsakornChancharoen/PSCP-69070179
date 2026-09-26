"""Point sorting"""
def f(p):
    """x + y"""
    return p[0] + p[1]
def y_is_greater(p):
    """if y is greater than another"""
    return -p[1]
def main():
    """Main function"""
    points = []
    for _ in range(int(input())):
        points.append([])
        for _ in range(int(input())):
            points[-1].append(list(map(int, input().split())))
        points[-1].sort(key=y_is_greater)
        points[-1].sort(key=f)
    for l in points:
        for p in l:
            print(*p)
main()
