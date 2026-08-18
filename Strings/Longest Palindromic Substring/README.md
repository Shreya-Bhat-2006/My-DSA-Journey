

# Longest Palindromic Substring

## Problem Statement

Given a string `s`, return the **longest palindromic substring** in `s`.

A **palindrome** is a string that reads the same forward and backward.

### Example 1

```
Input: s = "babad"

Output: "bab"

Explanation:
"aba" is also a valid answer.
```

### Example 2

```
Input: s = "cbbd"

Output: "bb"
```

---

# Logic 1: Brute Force

### Idea

Check **every possible substring**.

For each substring:

1. Generate the substring using `left` and `cur`.
2. Check whether it is a palindrome.
3. If it is a palindrome, compare its length with `longest`.
4. Keep the longer palindrome.

### Thinking

For `"babad"`:

```
left = 0
    "b"
    "ba"
    "bab"     ← palindrome
    "baba"
    "babad"

left = 1
    "a"
    "ab"
    "aba"     ← palindrome
    "abad"

left = 2
    "b"
    "ba"
    "bad"

...
```

### Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def pal(st):
            return st == st[::-1]

        longest = ""

        for left in range(len(s)):
            for cur in range(left, len(s)):

                st = s[left:cur + 1]

                if pal(st):
                    if len(st) > len(longest):
                        longest = st

        return longest
```

### Complexity

There are **O(n²)** possible substrings.

Checking whether each substring is a palindrome takes **O(n)** because of:

```
st[::-1]
```

Therefore:

```
Time:  O(n³)
Space: O(n)
```

The space is due to creating substring/reversed-string objects.

---

# Logic 2: Expand Around Center — Efficient

Instead of generating every substring, we use the fact that:

> **Every palindrome has a center.**
> 

We start from the center and expand outward while the characters are equal.

There are **two types of palindromes**.

### 1. Odd-length palindrome

Example:

```
"aba"

a b a
  ↑
center
```

The center is one character.

So:

```
expand(i, i)
```

---

### 2. Even-length palindrome

Example:

```
"bb"

b | b
  ↑
center
```

The center is **between two characters**.

So:

```
expand(i, i + 1)
```

---

### Expansion

For every `i`, check both:

```
expand(i, i)       # odd
expand(i, i + 1)   # even
```

Inside `expand()`:

```
while left >= 0 and right < len(s) and s[left] == s[right]:
```

Keep moving:

```
left  ←
right →
```

as long as the characters match.

### Code

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def pal(l,r):
            while(l>=0 and r<len(s) and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]
        longest=""
        for i in range(len(s)):
            st1 = pal(i, i + 1)
            st2=pal(i,i)
            if len(st1)>len(longest):
                longest=st1
            if len(st2)>len(longest):
                longest=st2
        return longest

        

            
        return longest
```

# Complexity Comparison

| Approach | Idea | Time | Space |
| --- | --- | --- | --- |
| **Brute Force** | Generate every substring + check palindrome | **O(n³)** | O(n) |
| **Expand Around Center** | Expand from every possible center | **O(n²)** | O(n) |
