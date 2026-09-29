# Permutation in String — Sliding Window

## 1. Problem Statement

Given two strings `s1` and `s2`, return `True` if **any permutation of `s1` appears as a substring of `s2`**.

Otherwise, return `False`.

A **permutation** means rearranging the characters without changing how many times each character occurs.

For example:

```
s1 = "ab"

Permutations:
"ab"
"ba"
```

---

## 2. Examples

### Example 1

```
Input:
s1 = "ab"
s2 = "eidbaooo"

Output:
True
```

Why?

`s2` contains:

```
eid[ba]ooo
```

`"ba"` is a permutation of `"ab"`.

Therefore:

```
True
```

---

### Example 2

```
Input:
s1 = "ab"
s2 = "eidboaoo"

Output:
False
```

There is no substring of length `2` having the same characters as `"ab"`.

Therefore:

```
False
```

---

### Example 3

```
Input:
s1 = "abc"
s2 = "xxcbaxx"

Output:
True
```

Because:

```
xx[cba]xx
```

`"cba"` is a permutation of `"abc"`.

---

# 3. Logic to Solve

The important observation is:

> We don't need to generate all permutations.
> 

For example:

```
s1 = "abb"
```

Its permutations include:

```
abb
bab
bba
```

All of them have the same character frequency:

```
a → 1
b → 2
```

So instead of generating permutations, we simply check:

> **Does any substring of `s2` of length `len(s1)` have the same character frequencies as `s1`?**
> 

We use a **sliding window**.

---

### Step 1: Count characters in `s1`

For:

```
s1 = "ab"
```

we create:

```
d1= {'a':1,'b':1}
```

---

### Step 2: Create a window of size `len(s1)`

Since:

```
len(s1) = 2
```

we examine two characters at a time in `s2`.

For:

```
s2 = "eidbaooo"
```

the windows are:

```
"ei"
"id"
"db"
"ba"
"ao"
"oo"
"oo"
```

---

### Step 3: Move the window

Instead of creating a new dictionary for every window, we:

- **Add** the new character entering the window.
- **Remove** the old character leaving the window.

For example:

```
[e i] d b a o o o
```

Move one position:

```
e [i d] b a o o o
```

We remove `e` and add `d`.

Move again:

```
e i [d b] a o o o
```

Remove `i`, add `b`.

Eventually:

```
e i d [b a] o o o
```

The frequency becomes:

```
d1 = {'a': 1, 'b': 1}

d2 = {'b': 1, 'a': 1}
```

They are equal.

Therefore, return `True`.

---

# 4. Code

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        d1 = {}

        for i in s1:
            d1[i] = d1.get(i, 0) + 1

        d2 = {}
        k = len(s1)

        for r in range(len(s2)):

            d2[s2[r]] = d2.get(s2[r], 0) + 1

            if r >= k:
                lc = s2[r - k]

                d2[lc] -= 1

                if d2[lc] == 0:
                    del d2[lc]

            if d1 == d2:
                return True

        return False
```

# 5. Why `r >= k`?

Suppose:

```
k = 2
```

Initially:

```
r = 0 → window size 1
r = 1 → window size 2
```

This is the correct window size.

When:

```
r = 2
```

we have added a third character.

So:

```
window size = 3
```

We remove:

```
s2[r-k]
```

which is:

```
s2[2-2]
s2[0]
```

So the window goes back to size `2`.

After that, every time `r` increases, we add one character and remove one character.

---

# 6. Complexity

Let:

- `n = len(s2)`
- `m = len(s1)`

### Time Complexity

```
O(n)
```

We move through `s2` only once.

### Space Complexity

```
O(1)
```

because the strings contain only lowercase English letters, so the frequency dictionaries can contain at most **26 characters**.
