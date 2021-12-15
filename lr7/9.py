with open('lr7\\9.txt', encoding='utf8') as file:
    n = int(file.readline())
    stations = dict.fromkeys([i for i in range(1, n+1)], 0)
    for string in file.readlines():
        _, _, st_in, st_out = string.split()
        for i in range(int(st_in), int(st_out)):
            stations[i] += 1

mx = max(stations.values())
for station, value in stations.items():
    if value == mx:
        print(f'{station}-{station+1}')