"""Delivery War"""
PATH = {
    "BKK" : {"CNX" : [10,30],"PKT" : [25,50]},
    "CNX" : {"UBP" : [15,40]},
    "UBP" : {"BKK" : [20,40],"PKT" : [40,70]},
    "PKT" : {"CNX" : [30,60]}
}
start, dest = input().upper().split()
weight = float(input())
if start in PATH and dest in PATH[start]:
    data = PATH[start][dest]
    print(f"{(data[0] + weight * data[1]):.2f}")
else:
    print("Error")
