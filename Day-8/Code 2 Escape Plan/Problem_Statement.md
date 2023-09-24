# Code Documentation 📝

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)

## Intuition 💡
<!-- Describe your first thoughts on how to solve this problem. -->
The code aims to find the middle element of a given array after sorting it. The middle element is determined based on the array's length, ensuring that it's the median value.

## Approach 🚀
<!-- Describe your approach to solving the problem. -->
The code follows a straightforward approach:
1. It takes an integer 'n' as input, representing the number of elements in the array.
2. It takes an array 'arr' as input, containing 'n' integers.
3. The 'findMiddle' function sorts the 'arr' in ascending order.
4. It calculates the middle index by dividing 'n' by 2.
5. It extracts the middle element from the sorted array as the median.
6. The median element is returned as the output.

## Explanation 📚
<!-- Describe your explanation in short with steps. -->
Here's how the code works:
1. The 'findMiddle' function sorts the input array 'arr' in ascending order.
2. It determines the middle index by performing integer division of 'n' by 2.
3. The middle element, located at the middle index of the sorted 'arr', is extracted and returned as the result.
4. The result is the median value of the given array.

## Complexity 📊
- Time complexity: O(n * log(n))
  - The code sorts the input array 'arr' using an efficient sorting algorithm, which typically takes O(n * log(n)) time.
- Space complexity: O(n)
  - The code uses additional space to store the sorted array, which has a space complexity of O(n).

## Usage 🧑‍💻
To use this code, provide an integer 'n' as input, followed by 'n' space-separated integers representing the array elements. For example:

