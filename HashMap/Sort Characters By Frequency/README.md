# **Sort Characters By Frequency**

## 1. Problem Statement

Given a string `s`, **sort the characters in decreasing order based on their frequency**.

In other words, characters that appear more times should come first.

If two characters have the same frequency, **their order does not matter**.

### Example 1

```
Input:  s = "tree"

Frequencies:
t → 1
r → 1
e → 2

Output: "eert"
```

`"eetr"` is also valid because `t` and `r` both occur once.

### Example 2

```
Input:  s = "cccaaa"

Frequencies:
c → 3
a → 3

Output: "cccaaa"
```

`"aaaccc"` is also valid.

---

## 2. Logic to Solve

### Step 1: Count the frequency of every character

Use a dictionary.

```
d[i]=d.get(i,0)+1
```

For:

```
"tree"
```

we get:

```
d = {
    't': 1,
    'r': 1,
    'e': 2
}
```

---

### Step 2: Sort characters according to their frequency

We use:

```
chars=sorted(d,key=d.get,reverse=True)
```

Here:

- `d` → dictionary containing characters
- `key=d.get` → sort according to the value/frequency
- `reverse=True` → highest frequency first

So:

```
['e', 't', 'r']
```

---

### Step 3: Build the answer

For every character, repeat it according to its frequency:

```
new+=i*d[i]
```

For `"tree"`:

```
e * 2 → "ee"
t * 1 → "t"
r * 1 → "r"
```

Final:

```
"eetr"
```

---

## 3. Code

```
class Solution:
    def frequencySort(self, s: str) -> str:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        chars=sorted(d,key=d.get,reverse=True)
        new=""
        for i in chars:
            new+=i*d[i]
        return new
```

## 4. Complexity

Let:

- `n` = length of the string
- `k` = number of unique characters

### Time Complexity

**Frequency counting:**

```
O(n)
```

**Sorting unique characters:**

```
O(k log k)
```

**Building the result:**

```
O(n)
```

Therefore:

**Overall: `O(n + k log k)`**

### Space Complexity

Dictionary + sorted character list:

**`O(k)`**

Since `k` is the number of unique characters.
