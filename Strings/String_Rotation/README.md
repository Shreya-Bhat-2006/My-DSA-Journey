## Check if One String is Rotation of Another

### 1. Problem Statement

Given two strings `s1` and `s2`, check whether `s2` is a **rotation** of `s1`.

A string is considered a rotation if we can move some characters from the **beginning** of `s1` to the **end**, without changing the order of the characters.

Return `True` if `s2` is a rotation of `s1`; otherwise, return `False`.

---

### 2. Example

**Example 1:**

```
s1 = "ABCD"
s2 = "CDAB"
```

Rotate `s1`:

```
ABCD
 ↓
CDAB
```

So:

```
Output: True
```

**Example 2:**

```
s1 = "ABCD"
s2 = "ACBD"
```

Possible rotations of `"ABCD"` are:

```
ABCD
BCDA
CDAB
DABC
```

`"ACBD"` is not a rotation.

```
Output: False
```

---

# Logic 1 — Try Every Rotation

### Idea

Start from every index of `s1` and create a new rotated string.

For:

```
s1 = "ABCD"
```

we generate:

```
ABCD
BCDA
CDAB
DABC
```

After creating each rotation, compare it with `s2`.

### Code

```python
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        new_string = s1[i:] + s1[:i]

        if new_string == s2:
            return True

    return False
```

### Complexity

For a string of length `n`:

- We try `n` rotations → `O(n)`
- Creating each rotated string takes `O(n)`
- Comparing strings takes `O(n)`

Therefore:

```
Time:  O(n²)
Space: O(n)
```

---

# Logic 2 — Using `s1 + s1`

### Key Observation

If `s2` is a rotation of `s1`, then `s2` will always occur inside:

```
s1 + s1
```

Example:

```
s1 = "ABCD"

s1 + s1
= "ABCDABCD"
```

Now:

```
"CDAB"
```

is present inside `"ABCDABCD"`.

### CODE:

```python
def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False

    return s2 in s1 + s1

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

print(is_rotation(s1, s2))
```

### Why does this work?

Take:

```
s1 = "ABCD"
```

`ABCDABCD` contains:

```
ABCD
 BCDA
  CDAB
   DABC
```

These are exactly the possible rotations of `"ABCD"`.

So instead of manually creating every rotation, we simply check whether `s2` exists in `s1 + s1`.

### Complexity

The concatenation:

```
s1 + s1
```

takes `O(n)` space.

The substring search `s2 in s1 + s1` is **implementation-dependent**; in Python, its practical complexity is typically near-linear, though you shouldn't claim a strict `O(n)` bound without specifying the underlying string-search algorithm.

For a typical DSA explanation, you can write:

```
Time:  O(n)   (typical/expected for substring search)
Space: O(n)
```

### Which one should you remember?

**Logic 1:** Better for understanding the problem.

> "I'll generate every possible rotation and compare."
> 

**Logic 2:** Better for writing a short solution.

> "Every rotation must occur inside `s1 + s1`."
>
