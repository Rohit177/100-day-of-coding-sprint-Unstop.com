def check(s):
  a_after_b = False
  for i in range(1, len(s)):
    if s[i - 1] == 'b' and s[i] == 'a':
        a_after_b = True
        break
  return "NO" if a_after_b else "YES"

s = input()

print(check(s))
