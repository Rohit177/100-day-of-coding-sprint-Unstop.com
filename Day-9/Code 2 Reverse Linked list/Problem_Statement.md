
<h1 align="center">
Reverse Linked list
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
  <img src="https://img.shields.io/badge/-LinkedList-red" alt="Linked List">
</p>





## Intuition 💡
<!-- Describe your first thoughts on how to solve this problem. -->
The code focuses on reversing a singly linked list. It uses the iterative approach to reverse the order of nodes in the linked list, and then prints the reversed list.

## Approach 🚀
<!-- Describe your approach to solving the problem. -->
The code uses the following components:
1. `ListNode` class: Defines a node of the singly linked list, which has a value `val` and a reference to the next node `next`.
2. `reverseLinkedList(head)`: A function that reverses the given linked list using an iterative approach. It maintains three pointers: `prev`, `current`, and `next_node`. It iterates through the list, reversing the `next` pointers to reverse the list's order.
3. `printLinkedList(head)`: A function that prints the values of the linked list nodes in order.

## Explanation 📚
<!-- Describe your explanation in short with steps. -->
Here's how the code works:
1. The `reverseLinkedList` function initializes `prev` as `None` and `current` as the `head` of the linked list.
2. It enters a loop where it iterates through the linked list.
3. Inside the loop, it maintains `next_node` to store the reference to the next node.
4. It reverses the `next` pointer of the `current` node to point to `prev`.
5. It updates `prev` to `current` and `current` to `next_node` for the next iteration.
6. Once the loop finishes, `prev` becomes the new head of the reversed linked list.
7. The `printLinkedList` function then prints the values of the nodes in the reversed linked list.

## Complexity 📊
- Time complexity: O(n)
  - The code iterates through the linked list once, where 'n' is the number of nodes in the list.
- Space complexity: O(1)
  - The code uses a constant amount of extra space for variables, regardless of the size of the linked list.
