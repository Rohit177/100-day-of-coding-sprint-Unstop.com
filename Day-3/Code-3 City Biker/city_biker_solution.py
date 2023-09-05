# Code
```
class Solution(object):
    def largestAltitude(self, gain):
        highest = 0
        current_altitude = 0

        for alt_gain in gain:
            current_altitude += alt_gain
            highest = max(highest, current_altitude)

        return highest

        
```
