# Valid Palindrome II

## 1. Problem Statement

Given a string `s`, return `True` if `s` can become a **palindrome after deleting at most one character**.

You can:

- Delete **0 characters**, or
- Delete **1 character**

You cannot delete more than one character.

---

## 2. Examples

### Example 1

```
Input: s = "aba"
Output: True
```

`"aba"` is already a palindrome, so we don't need to delete anything.

```
aba
↑ ↑
a = a
```

---

### Example 2

```
Input: s = "abca"
Output: True
```

`"abca"` is not a palindrome:

```
a b c a
↑     ↑
a = a

  b c
  b ≠ c
```

We can delete either `b` or `c`:

```
delete b → "aca" → palindrome
```

or

```
delete c → "aba" → palindrome
```

Therefore:

```
True
```

---

### Example 3

```
Input: s = "abc"
Output: False
```

Delete `a`:

```
"bc" → not palindrome
```

Delete `b`:

```
"ac" → not palindrome
```

Delete `c`:

```
"ab" → not palindrome
```

Therefore:

```
False
```

---

# 3. Your First Logic — Brute Force

Your first idea was:

> First check whether the original string is already a palindrome.
> 
> 
> If it isn't, try deleting **each character one by one**.
> 
> After every deletion, check whether the resulting string is a palindrome.
> 

### Example: `"abca"`

Try deleting every character:

```
Original: "abca"

Delete index 0:
"bca" → not palindrome

Delete index 1:
"aca" → palindrome ✓
```

As soon as we get a palindrome, return `True`.

---

## Your First Code

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]:
            return True

        i = 0

        while i < len(s):
            S = s[:i] + s[i+1:]

            if S == S[::-1]:
                return True

            i += 1

        return False
```

### Important syntax

```
s[::-1]
```

means:

> Reverse the string.
> 

And:

```
s[:i]+s[i+1:]
```

means:

> Remove the character at index `i`.
> 

For example:

```
s = "abca"
i = 1

s[:1]    → "a"
s[2:]    → "ca"

"a" + "ca" → "aca"
```

Then:

```
S==S[::-1]
```

checks whether `"aca"` is a palindrome.

---

# 4. Complexity of Your First Logic

Suppose the string has `n` characters.

You potentially try deleting **every character**:

```
n times
```

For each deletion, you create a new string and check whether it is a palindrome:

```
O(n)
```

Therefore:

```
Time Complexity: O(n²)
Space Complexity: O(n)
```

The `O(n)` space is because you're creating new strings.

This is why your submission eventually got **Time Limit Exceeded**.

---

# 5. Efficient Logic — Two Pointers

Instead of deleting every character, we can be smarter.

Use two pointers:

```
left →                    ← right
       a b c a
```

Compare the characters from both ends.

### If they are equal

Move both pointers inward:

```
a b c a
↑     ↑
```

`a == a`

Then:

```
  b c
  ↑ ↑
```

---

### What if they are different?

Suppose:

```
a b c a
  ↑ ↑
  b c
```

We find:

```
b != c
```

Since we are allowed to delete **only one character**, there are only two possibilities:

### Option 1 — Delete the left character

Delete `b`:

```
a c a
```

Check whether the remaining part is a palindrome.

### Option 2 — Delete the right character

Delete `c`:

```
a b a
```

Check whether the remaining part is a palindrome.

So:

```
delete left OR delete right
```

We don't need to try deleting any other character.

## Code

```
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        def check(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
                

        while l<r:
            if s[l]!=s[r]:
               return check(l+1,r) or check(l,r-1)
            l+=1
            r-=1
        return True

    
            

```

# 7. How the Efficient Code Works

Take:

```
s = "abca"
```

Initially:

```
l = 0
r = 3

a b c a
↑     ↑
```

Compare:

```
a == a
```

So:

```
l+=1r-=1
```

Now:

```
a b c a
  ↑ ↑
  l r
```

Compare:

```
b != c
```

Now we execute:

```
returncheck(l+1,r)orcheck(l,r-1)
```

There are two possibilities:

```
check(l+1,r)
```

means:

> Skip/delete the left character (`b`) and check the remaining portion.
> 

And:

```
check(l,r-1)
```

means:

> Skip/delete the right character (`c`) and check the remaining portion.
> 

The `check()` function actually verifies whether that remaining portion is a palindrome.

---

# 8. Why `check()` Doesn't Need to Check Everything Again

This is an important part of the algorithm.

For:

```
a b c a
↑     ↑
```

we already checked:

```
a == a
```

So we **know** the outer `a`s are correct.

When we reach:

```
a b c a
  ↑ ↑
  b c
```

we only need to investigate the mismatch.

If we skip `b`:

```
a [b] c a
    ↓
a   c a
```

The outer `a`s were already verified.

`check()` only needs to check the remaining **unverified section**.

---

# 9. Complexity of Efficient Logic

The main `while` loop moves from both ends toward the center:

```
O(n)
```

When a mismatch occurs, `check()` can scan the remaining characters:

```
O(n)
```

But this happens only for the **one mismatch**, because we are allowed to delete only one character.

Therefore the total is still:

```
Time Complexity: O(n)
```

The helper function uses only pointer variables:

```
Space Complexity: O(1)
```
