
<h1 align="center">
Decode Enigma 📝
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



## Intuition 🚀
<!-- Describe your approach to solving the problem. -->
The code is designed to interpret an enigmatic command by replacing specific phrases with their corresponding meanings. It transforms a given input command into a more understandable form.

## Approach 📚
<!-- Describe your approach to solving the problem. -->
The code follows these steps:
1. It takes a string 'command' as input, representing an enigmatic command.
2. It uses the 'replace' method to replace specific phrases within the command with their corresponding meanings:
   - "S" is replaced with "send ".
   - "[]" is replaced with "the ".
   - "[sps]" is replaced with "ships ".
3. It splits the modified 'command' into individual words using 'split()'.
4. It joins the words back together into a single sentence, separated by spaces.
5. The resulting sentence is returned as the interpretation of the enigmatic command.

## Explanation 📚
<!-- Describe your explanation in short with steps. -->
Here's how the code works:
1. The code modifies the 'command' by replacing specific phrases with their meanings.
2. It then splits the modified 'command' into individual words.
3. The words are joined back together into a single sentence.
4. The resulting sentence represents the interpretation of the enigmatic command.
5. The code prints the interpretation as the output.

## Complexity 📊
- Time complexity: O(n)
  - The code processes the 'command' string linearly, where 'n' is the length of the string.
- Space complexity: O(n)
  - The code uses additional space for the modified 'command' string, which has a space complexity of O(n).

## Usage 🧑‍💻
To use this code, provide an enigmatic command as input. For example: \
"S[] [sps]" \
The output will be the interpretation of the command: \
"send the ships" 

This code can be applied to scenarios where you need to translate enigmatic or coded messages into understandable language.

