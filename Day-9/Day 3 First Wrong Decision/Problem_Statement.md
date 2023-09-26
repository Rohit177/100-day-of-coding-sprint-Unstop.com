<h1 align="center">
First Wrong Decision 💡
</h1>

<p align="center">
  <a href="https://www.python.org/downloads/release/python-380/">
    <img src="https://img.shields.io/badge/Python-3.8%2B-blue" alt="Python Version">
  </a>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/-Data%20Structures-lightgrey" alt="Data Structures">
  <img src="https://img.shields.io/badge/-Lists-brightgreen" alt="Lists">
  <img src="https://img.shields.io/badge/-Enumerate-orange" alt="enumerate">
  <img src="https://img.shields.io/badge/-Loops-blue" alt="Loops">
</p>



## Intuition 🚀
<!-- Describe your approach to solving the problem. -->
The code aims to find the index of the first occurrence of the character 'W' in a given string of decisions. It represents a scenario where a series of decisions are made, and we need to identify when the first wrong decision ('W') occurs.

## Approach 📚
<!-- Describe your approach to solving the problem. -->
The code follows these steps:
1. It takes a string 'decisions' as input, representing a sequence of decisions.
2. It iterates through the string using a for loop and 'enumerate' to track the index 'i' and the corresponding 'decision' character.
3. Inside the loop, it checks if the 'decision' is 'W' (wrong decision).
4. If a 'W' is found, it returns the index 'i' indicating the position of the first wrong decision.
5. If no 'W' is found, it returns -1 to indicate that there are no wrong decisions in the string.

## Explanation 📚
<!-- Describe your explanation in short with steps. -->
Here's how the code works:
1. The code takes a string 'decisions' as input.
2. It iterates through the characters of the string using 'enumerate'.
3. For each character, it checks if it is 'W' (a wrong decision).
4. If 'W' is found, the code returns the index of that decision.
5. If no 'W' is found after iterating through the entire string, it returns -1 to indicate that there are no wrong decisions.

## Complexity 📊
- Time complexity: O(n)
  - The code iterates through the string 'decisions' once, where 'n' is the length of the string.
- Space complexity: O(1)
  - The code uses a constant amount of extra space for variables.

## Usage 🧑‍💻
To use this code, provide a string 'decisions' as input. For example:
WWLWLW

The output will be the index of the first wrong decision ('W') in the string, or -1 if there are no wrong decisions.
This code can be applied to scenarios where you need to identify the first occurrence of a specific character in a string.


