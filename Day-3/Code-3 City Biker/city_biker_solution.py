def highestAltitude(gain):
    gain = [0] + gain 
    for i in range(1, len(gain)):
      gain[i] += gain[i-1]

    return max(gain)

n = int(input())
gain = list(map(int, input().split()))

result = highestAltitude(gain)
print(result)
