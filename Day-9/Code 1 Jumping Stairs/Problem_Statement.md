
<h1 align="center">
Jumping Stairs 📝
</h1>

<p align="center">
  <a href="https://www.python.org/downloads/release/python-380/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  </a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/-Data%20Structures-lightgrey" alt="Data Structures">
  <img src="https://img.shields.io/badge/-Algorithms-orange" alt="Algorithms">
  <img src="https://img.shields.io/badge/-Lists-brightgreen" alt="Lists">
  <img src="https://img.shields.io/badge/-Loops-blue" alt="Loops">
</p>




# Code Documentation 📝

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green)](https://opensource.org/licenses/MIT)

## Intuition 💡
<!-- Describe your first thoughts on how to solve this problem. -->
The code addresses the problem of finding the distinct ways to climb a staircase with 'n' steps, where you can take either one or two steps at a time. The intuition is to use dynamic programming to calculate the number of distinct ways to reach the top of the staircase.

## Approach 🚀
<!-- Describe your approach to solving the problem. -->
The code follows these steps:
1. If 'n' is 1, return 1 because there is only one way to climb one step.
2. If 'n' is 2, return 2 because there are two ways to climb two steps (1+1 or 2).
3. Create an array 'dp' of size 'n+1' to store the number of distinct ways to reach each step.
4. Initialize 'dp[1]' to 1 and 'dp[2]' to 2 because we've already handled these base cases.
5. Iterate from 3 to 'n' using a loop:
   - For each step 'i', calculate 'dp[i]' as the sum of 'dp[i-1]' and 'dp[i-2]'.
6. 'dp[n]' will represent the total distinct ways to climb 'n' steps.

## Explanation 📚
<!-- Describe your explanation in short with steps. -->
Here's how the code works:
1. If 'n' is 1, the function returns 1 because there is only one way to climb one step.
2. If 'n' is 2, the function returns 2 because there are two ways to climb two steps.
3. For 'n' greater than 2, the code uses dynamic programming to calculate the number of distinct ways to climb 'n' steps.
4. It initializes an array 'dp' to store the results.
5. The loop iterates from step 3 to 'n', calculating 'dp[i]' by adding 'dp[i-1]' and 'dp[i-2]'.
6. The result 'dp[n]' represents the total distinct ways to climb 'n' steps.

## Complexity 📊
- Time complexity: O(n)
  - The code iterates through the staircase steps once to calculate the distinct ways using dynamic programming.
- Space complexity: O(n)
  - The code uses an array 'dp' of size 'n+1' to store intermediate results.

## Usage 🧑‍💻
To use this code, provide an integer 'n' as input, which represents the number of steps in the staircase. For example:

