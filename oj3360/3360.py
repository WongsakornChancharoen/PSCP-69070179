"""Bread (thumbs up)"""
w, h, m, n = map(int, input().split())
verts = []
horiz = []
for p1 in input().split():
    verts.append(int(p1))
for p2 in input().split():
    horiz.append(int(p2))
x = [0] + verts + [w]
widths = [ #cut vertically
    x[i] - x[i - 1] for i in range(1,m+2)
]
y = [0] + horiz + [h]
heights = [ #cut horizontally
    y[i] - y[i - 1] for i in range(1,n+2)
]
widths.sort(reverse=True)
heights.sort(reverse=True)
largest = widths[0] * heights[0]
second_large = max(
    widths[0] * heights[1],
    widths[1] * heights[0]
)
print(largest, second_large)
