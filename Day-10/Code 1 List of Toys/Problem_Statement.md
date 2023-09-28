<h1 align="center">
List of Toys 💡
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
</p>


## Intuition 🚀
<!-- Describe your approach to solving the problem. -->
The code aims to reconstruct two separate lists from a merged list of product IDs and sizes. The merged list contains alternating product IDs and sizes, and the goal is to separate them back into their original lists.

## Approach 📚
<!-- Describe your approach to solving the problem. -->
The code follows these steps:
1. It takes an integer 'n' as input, representing the number of products.
2. It takes a merged list 'merged_list' as input, containing alternating product IDs and sizes.
3. It splits the 'merged_list' into two separate lists: 'product_ids' and 'product_sizes' by slicing it.
4. It initializes an empty list 'recovered_list' to store the reconstructed list.
5. It iterates through the range 'n' using a loop.
6. In each iteration, it appends the 'i-th' product ID and 'i-th' product size to the 'recovered_list'.
7. Finally, it prints the 'recovered_list,' which now contains the original product IDs and sizes in their correct order.

## Explanation 📚
<!-- Describe your explanation in short with steps. -->
Here's how the code works:
1. The code splits the 'merged_list' into 'product_ids' and 'product_sizes' by using slicing.
2. It then initializes an empty 'recovered_list.'
3. In each iteration of the loop, it appends the 'i-th' product ID and 'i-th' product size to the 'recovered_list.'
4. The final 'recovered_list' contains the original product IDs and sizes in the correct order.
5. The code prints the 'recovered_list' as the output.

## Complexity 📊
- Time complexity: O(n)
  - The code iterates through the merged list once to reconstruct the original lists, where 'n' is the number of products.
- Space complexity: O(n)
  - The code uses additional space to store the 'recovered_list,' which has a space complexity of O(n).

## Usage 🧑‍💻
To use this code, provide an integer 'n' as input, followed by '2n' space-separated integers representing the merged list of product IDs and sizes. For example: \
3 \
2 5 1 3 4 7

The output will be the reconstructed list of product IDs and sizes in their original order:
2 3 5 4 1 7

