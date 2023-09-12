<h1 align="center">
Basketball Game 🏀
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
</p>

## Intuition 💡
<!-- Describe your first thoughts on how to solve this problem. -->
The code is designed to simulate and calculate the final score of a game based on a series of commands provided in the input. It processes the commands, which include adding, doubling, and removing elements from a list, to determine the game's final score.

## Approach 🚀
<!-- Describe your approach to solving the problem. -->
I implemented a function `check(arr)` that performs the following operations on an array:
- If an element is a digit or a negative number, it appends it to a temporary list as an integer.
- If an element is "C," it removes the last element from the temporary list.
- If an element is "D," it doubles the last element in the temporary list.
- If an element is "+," it adds the last two elements in the temporary list and appends the result.

The function returns the sum of elements in the temporary list.

## Explanation 📚
<!-- Describe your explanation in short with steps. -->
Here's how the code works:
1. Initialize an empty list `temp` to store numbers.
2. Iterate through the input array `arr`.
3. For each element in `arr`, perform the corresponding operation as described above and update `temp`.
4. Finally, return the sum of elements in `temp`.

## Complexity 📊
- Time complexity: O(n)
  - The code iterates through the input array once, where n is the length of the array.
- Space complexity: O(n)
  - The space complexity depends on the size of the `temp` list, which can grow up to n elements.

## Usage 🧑‍💻
To use this code, provide an integer `n` as input, followed by a space-separated array of commands. For example:

Feel free to use this code to find the final score of Basketball Game  🏀⚽🗑️⛹️‍♂️
