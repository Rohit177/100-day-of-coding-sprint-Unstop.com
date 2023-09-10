<h1 align="center">
Exchange Gift 🎁
</h1>
<p align="center">
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/downloads/release/python-380/)
</p>

## Intuition 🤔
The problem is about finding the youngest family member in a family based on the gift exchange data.

## Approach 🛠️
We can solve this problem by keeping track of two key pieces of information:
1. Gifts received by each family member.
2. Family members who have given at least one gift.

Once we have this information, we can identify the youngest family member based on the following criteria:
- They should not have given any gifts to anyone.
- They should have received gifts from all other family members except themselves.

## Explain 🔍
1. Initialize two data structures: `gift_r` (a list) to count how many gifts each family member received, and `gave_gift` (a set) to keep track of family members who have given gifts.

2. Iterate through the gift exchange data (a list of pairs `a` and `b`) and update `gift_r` and `gave_gift` accordingly.

3. Once we have processed all the gift exchanges, iterate through the family members and check if a member meets the criteria to be the youngest:
   - They should not be in the `gave_gift` set (haven't given any gifts).
   - They should have received gifts from all other family members except themselves (the count in `gift_r` should be `n - 1`).

4. Return the youngest family member found, or `-1` if no such member is found.

## Complexity 📊
- Time complexity: O(m) where `m` is the number of gift exchanges.
- Space complexity: O(n) where `n` is the number of family members.

---

Feel free to use this code to find the youngest family member in your exchange gift! 🎅🤶🎄🏡

