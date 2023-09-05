# Intuition
- We want to calculate the highest altitude the biker reaches during the trip.
- To do this, we need to iterate through the altitude gains and keep track of the current altitude.

# Approach
1. Initialize variables: highest = 0 (to store the highest altitude) and current = 0 (to store the current altitude).
2. Iterate through each gain in the gain list.
3. Update the current altitude by adding the gain to it.
4. Check if the current altitude is higher than the highest altitude seen so far.
   - If yes, update the highest altitude.
5. Continue iterating through all gains.
6. Return the highest altitude as the result.

# Complexity
- Time complexity: O(n) - We iterate through the gain list once.

- Space complexity: - We use a constant amount of extra space for variables.
