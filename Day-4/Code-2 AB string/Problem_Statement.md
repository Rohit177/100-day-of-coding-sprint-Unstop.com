# Intuition
The problem requires checking whether a given string is an AB string or not. An AB string is one where all the 'a's appear before all the 'b's. This implies that there should be no occurrence of 'a' after 'b'.

# Approach
The approach taken is to iterate through the characters of the string and check if there's any occurrence of 'a' after 'b'. If such an occurrence is found, we conclude that it's not an AB string and print "NO". Otherwise, we print "YES".

# Complexity
- Time complexity: O(n), where n is the length of the input string 's'.
- Space complexity: O(1), as we only use a boolean flag to check the condition.
