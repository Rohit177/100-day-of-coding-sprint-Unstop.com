# Intuition
# We want to count the total number of set bits (1s) in binary representation of numbers from 1 to N.

# Approach
# We iterate through numbers from 1 to N and for each number, we count the number of set bits (1s) in its binary representation.
# We use the built-in bin() function to convert a number to its binary representation, and then we count the '1's in the binary string.

# Time complexity:
# The time complexity of this code is O(N * log(N)), where N is the input number. For each number from 1 to N, we calculate the binary representation, which has a length of log(N).

# Space complexity:
# The space complexity of this code is O(1), as it uses a constant amount of space regardless of the input size.

