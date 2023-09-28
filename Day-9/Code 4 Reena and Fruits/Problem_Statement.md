<h1 align="center">
Reena and Fruits 💡
</h1>

<p align="center">
  <a href="https://www.python.org/downloads/release/python-380/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  </a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/-Data%20Structures-lightgrey" alt="Data Structures">
  <img src="https://img.shields.io/badge/-Lists-brightgreen" alt="Lists">
  <img src="https://img.shields.io/badge/-Loops-blue" alt="Loops">
  <img src="https://img.shields.io/badge/Function-Implemented-brightgreen" alt="Function">
  <img src="https://img.shields.io/badge/Sorting-Implemented-yellow" alt="Function">

</p>


## Intuition 🚀
<!-- Describe your approach to solving the problem. -->
The code is designed to maximize the sum of pairs from a list of integers. It sorts the list and selects every alternate element to form pairs, aiming to maximize the total sum.

## Approach 📚
<!-- Describe your approach to solving the problem. -->
The code follows these steps:
1. It takes an integer 'n' as input, representing the number of integers in the list.
2. It takes a list of integers 'nums' as input, containing 'n' integers.
3. It sorts the 'nums' list in ascending order.
4. It initializes 'max_sum' to 0 to store the maximum sum of pairs.
5. It iterates through the sorted 'nums' list using a loop, selecting every alternate element (i.e., elements at even indices).
6. It adds each selected element to 'max_sum.'
7. Finally, it returns 'max_sum' as the maximum sum of pairs.

## Explanation 📚
<!-- Describe your explanation in short with steps. -->
Here's how the code works:
1. The code sorts the 'nums' list in ascending order, ensuring that smaller numbers come first.
2. It initializes 'max_sum' to 0.
3. The loop iterates through the sorted 'nums' list, starting from the first element (index 0).
4. In each iteration, it adds the current element to 'max_sum' and moves to the next element, effectively forming pairs.
5. Since the list is sorted, selecting elements at even indices guarantees the maximum sum of pairs.
6. The final 'max_sum' is returned as the result.

## Complexity 📊
- Time complexity: O(n log n)
  - The code sorts the 'nums' list, which takes O(n log n) time.
- Space complexity: O(1)
  - The code uses a constant amount of extra space for variables.

## Usage 🧑‍💻
To use this code, provide an integer 'n' as input, followed by 'n' space-separated integers representing the list of numbers. For example: \
6 \
1 3 5 2 4 6

The output will be the maximum sum of pairs that can be formed from the list of numbers.

This code is helpful for finding the maximum sum of pairs in a list of integers, where you want to pair elements to maximize the total sum.
