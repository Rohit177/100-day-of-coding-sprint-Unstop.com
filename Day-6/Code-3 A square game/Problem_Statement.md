<h1 align="center">
A square game
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


## Intuition
The intuition behind this code is to first calculate the squares of the numbers in the list. This can be done using the ** operator in Python. Once the squares of the numbers are calculated, they can be sorted using the built-in sort() function. Finally, the sorted squares can be printed using the print() function.

## Approach
The approach to implementing this code is as follows:

- Read the number of integers from the user.
- Read the list of integers from the user.
- Calculate the squares of the numbers in the list.
- Sort the squares of the numbers.
- Print the squares of the numbers in sorted order.

## Explanation
1. We need to calculates the squares of the numbers in the list. This is done using a list comprehension, which is a concise way to create a new list from an existing list. In this case, the list comprehension creates a new list of the squares of the numbers in the nums list.

2. Sorts the squares of the numbers. This is done using the built-in sort() function. The sort() function sorts the list in ascending order by default.

3. Prints the squares of the numbers in sorted order. This is done using the print() function. The print() function prints the contents of the list to the console.

## Complexity
The time complexity of this code is O(n log n), where n is the number of integers in the list. This is because the sorting algorithm used (i.e., the sort() function) has a time complexity of O(n log n).

The space complexity of this code is O(n), where n is the number of integers in the list. This is because the code creates a new list to store the squares of the numbers, which has a size of n.
