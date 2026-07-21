'''Castle'''
def main():
    '''JoJos Bizarre Castle'''
    room = int(input())
    floor = 1
    low = 1
    high = 1
    while room > high:
        high += 2 * floor + 1
        low += 2 * (floor - 1) + 1
        floor += 1
    path = 0
    if room > 1:
        if (room - low) % 2:
            path = (floor - 1) * 2 - 1
        else:
            path = (floor - 1) * 2
    print(path)
main()
