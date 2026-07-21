'''Divide 10'''
def main():
    '''ben 10'''
    n = int(input())
    result = ''
    for i in range((n//10)*10, -1, -10):
        result += str(i) + (not i and '' or " ")
    print(result)
main()
