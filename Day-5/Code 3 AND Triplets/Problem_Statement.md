<h1 align="center">
Count AND Triplets
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


## :bulb: Intuition

The problem involves counting the number of triplets (a, b, c) in a given list `nums` such that the bitwise AND operation between any two of them results in 0. In other words, we need to find triples of numbers whose bitwise AND is 0.

## :rocket: Approach

1. We can use a dictionary `freq` to store the frequency of each bitwise AND result among all pairs of elements in `nums`.

2. We iterate through `nums` twice using two nested loops, calculating the bitwise AND of pairs of elements and updating the `freq` dictionary accordingly.

3. Finally, we iterate through `nums` again and for each element `n`, we check all entries in the `freq` dictionary. If the bitwise AND of `n` and a value in the dictionary is 0, we increment the result counter by the frequency of that value in `freq`.

4. The result counter keeps track of the count of AND triplets.

## :pencil: Explain

1. Initialize `res` to 0, which will store the count of AND triplets.

2. Create an empty dictionary `freq` to store the frequency of each bitwise AND result.

3. Get the length of the input list `nums` and store it in `n`.

4. Iterate through `nums` twice using two nested loops (i and j) to calculate the bitwise AND of all pairs of elements in `nums`. Store the result in `t`.

5. Check if `t` is not already a key in the `freq` dictionary. If not, initialize its count to 0. Then, increment the count of `t` by 1 in the `freq` dictionary.

6. Now, iterate through `nums` again using a nested loop to find AND triplets. For each element `n` in `nums`, iterate through the keys in the `freq` dictionary.

7. Inside the inner loop, check if the bitwise AND of `n` and the current key (which represents a bitwise AND result) is equal to 0. If it is, increment `res` by the frequency of that key in the `freq` dictionary.

8. After both loops, return the final count of AND triplets stored in `res`.

## :chart_with_upwards_trend: Complexity

- Time complexity: O(n^2) - We have two nested loops to calculate the bitwise AND of all pairs of elements in `nums`, where `n` is the length of `nums`.

- Space complexity: O(n) - We use the `freq` dictionary to store the frequency of bitwise AND results, which can have at most `n` different values.
