def highest_altitude(n, gain):
    highest = 0
    current_altitude = 0

    for alt_gain in gain:
        current_altitude += alt_gain
        highest = max(highest, current_altitude)

    return highest

n = int(input())
gain = list(map(int, input().split()))

result = highest_altitude(n, gain)
print(result)
