# Intuition
We want to find the integer that appears most frequently in an array of integers.

# Approach
1. Take the size of the array `n` and the array elements as input.
2. Create a dictionary `count_dict` to store the count of each integer.
3. Loop through the array and count the occurrences of each integer by updating `count_dict`.
4. Initialize variables `max_count` and `most_common_num` to keep track of the integer with the highest count and its count, respectively.
5. Iterate through the items in `count_dict` and compare the count of each integer with `max_count`. If the count is greater than `max_count`, update `max_count` and `most_common_num` with the current integer and count.
6. Print the `most_common_num`, which is the integer that appears most frequently in the array.

# Complexity
- Time complexity: O(n), where n is the size of the array. We loop through the array once to count the occurrences of each integer.
- Space complexity: O(m), where m is the number of unique integers in the array. We use a dictionary to store counts, and in the worst case, there can be as many unique integers as there are elements in the array.
