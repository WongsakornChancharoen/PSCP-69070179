"""Card"""
t = input().upper()
front = t[:-1]
back = t[-1]
prefix = {
    'A' : 'ace', 'J' : 'jack',
    'Q' : 'queen', 'K' : 'king'
}
suffix = {
    'D' : 'diamonds', 'H' : 'hearts',
    'S' : 'spades', 'C' : 'clubs'
}
if prefix.get(front):
    front = prefix[front]
print(f"{front} of {suffix[back]}")
