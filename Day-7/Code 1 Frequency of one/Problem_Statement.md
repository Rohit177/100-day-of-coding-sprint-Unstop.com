
<h1 align="center">
Frequency of one 📝
</h1>

<p align="center">
  <a href="https://www.python.org/downloads/release/python-380/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  </a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/-Data%20Structures-lightgrey" alt="Data Structures">
  <img src="https://img.shields.io/badge/-Lists-brightgreen" alt="Lists">
  <img src="https://img.shields.io/badge/-Dictionaries-orange" alt="Dictionaries">
  <img src="https://img.shields.io/badge/-Loops-blue" alt="Loops">
  <img src="https://img.shields.io/badge/-Bits-purple" alt="Bits">
</p>



## Intuition 💡
<!-- Describe your first thoughts on how to solve this problem. -->
The code calculates the total number of set bits (1s) in the binary representation of integers from 1 to 'n'. It does so by iterating through each integer in the range and counting the set bits using bitwise operations.

## Approach 🚀
<!-- Describe your approach to solving the problem. -->
The code consists of two main functions:
1. `count_set_bits(n)`: This function counts the number of set bits in the binary representation of an integer 'n' using a bitwise operation.
2. `total_set_bits_from_1_to_n(n)`: This function calculates the total number of set bits in the binary representations of integers from 1 to 'n' by iterating through the range and using the `count_set_bits` function.

The result is the total count of set bits, which is printed as the output.

## Explanation 📚
<!-- Describe your explanation in short with steps. -->
Here's how the code works:
1. The `count_set_bits(n)` function counts the set bits in 'n' by repeatedly performing the 'n & (n - 1)' operation, which clears the rightmost set bit in 'n' until 'n' becomes 0.
2. The `total_set_bits_from_1_to_n(n)` function calculates the total set bits in the binary representations of integers from 1 to 'n' by iterating through each integer and using the `count_set_bits` function.
3. The result is printed as the total count of set bits.

## Complexity 📊
- Time complexity: O(n * log(n))
  - The code iterates through each integer from 1 to 'n', and for each integer, it counts set bits in its binary representation, which takes O(log(n)) time.
- Space complexity: O(1)
  - The code uses a constant amount of extra space for variables, regardless of the input 'n'.

