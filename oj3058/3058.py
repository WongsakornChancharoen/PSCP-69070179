"""Brick Bridge"""
def main():
    """Bridge"""
    a = int(input()) #smol
    b = int(input()) #beeg
    goal = int(input())
    need = goal - min(goal//5, b) * 5
    if need > a:
        print(-1)
    else:
        print(need)
main()
