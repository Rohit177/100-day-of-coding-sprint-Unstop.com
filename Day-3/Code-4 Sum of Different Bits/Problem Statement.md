# Intuition
The problem asks us to find the total sum of differences between two binary strings 'a' and 'b'. We need to compare 'a' with all contiguous substrings of 'b' of the same length as 'a' and count the number of positions where the corresponding bits are different.

# Approach
1. Define a function `findTotalSum(a, b)` to calculate the total sum of differences.
2. Initialize variables `n` and `m` to store the lengths of strings 'a' and 'b', respectively.
3. Initialize the `total_sum` to 0 to keep track of the total sum of differences.
4. Iterate through 'b' using a loop from 0 to (m - n + 1) to consider all possible substrings of 'b' with the same length as 'a'.
5. For each substring, calculate the number of positions where the corresponding bits are different and store it in the `diff_count` variable.
6. Add the `diff_count` to the `total_sum`.
7. After the loop, return the `total_sum`.

# Complexity
- Time complexity: O((m - n + 1) * n), where 'm' is the length of 'b' and 'n' is the length of 'a'. In the worst case, we iterate through all possible substrings of 'b'.
- Space complexity: O(1), as we use a constant amount of space for variables.
