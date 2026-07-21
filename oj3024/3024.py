'''Surprising votes'''
def main():
    '''supriseeee'''
    total = float(input('Total score'))
    highest = float(input('Highest score'))

    lowest = total - highest * 2
    if lowest < 0:
        lowest = 0
    if highest - lowest > 2:
        print('Surprising')
    else:
        print('Not surprising')
main()
