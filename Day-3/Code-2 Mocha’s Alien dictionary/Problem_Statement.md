# Problem Summary

John has a string `s`, and Mocha has a dictionary of words. John wants to know if he can break his string `s` into words from Mocha's dictionary.

# Code Summary

1. Initialize a list `dp` to track if substrings of `s` can be segmented. Set `dp[0]` to `True`.

2. Iterate through the indices of `s` and check if a substring can be segmented using words from the dictionary.

3. If a substring can be segmented, update `dp[i]` to `True`.

4. After iterating through all substrings, check if `dp[n]` is `True`, where `n` is the length of `s`. If `dp[n]` is `True`, print "true," indicating that `s` can be segmented; otherwise, print "false."

This code efficiently determines whether `s` can be segmented using Mocha's dictionary of words.
