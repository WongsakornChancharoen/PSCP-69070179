"""Calling Imposter from Among Us at 3AM D:)"""
import json
players = {}
dead_players = {}
imposters = 0
while True:
    js = input()
    if js == "Start":
        break
    data:dict = json.loads(js)
    if 'Impostor' in data.values():
        imposters += 1
    players.update(data)
while True:
    name = input()
    if name == "End":
        break
    status = players.pop(name)
    if status == "Impostor":
        imposters -= 1
    dead_players[name] = status
players = dict(sorted(players.items()))
dead_players = dict(sorted(dead_players.items()))
print(f"{imposters} Impostor Remains")
print("***Alive***")
for name, status in players.items():
    print(f"{name} : {status}")
print("***Dead***")
for name, status in dead_players.items():
    print(f"{name} : {status}")
