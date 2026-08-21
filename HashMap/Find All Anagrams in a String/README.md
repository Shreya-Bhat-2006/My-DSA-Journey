# Find All Anagrams in a String

### Problem Statement

Given two strings `s` and `p`, find **all starting indices of `p`'s anagrams in `s`**.

An **anagram** means the two strings contain the **same characters with the same frequencies**, but the order can be different.

Return the starting indices in any order.

### Example

```
s = "cbaebabacd"
p = "abc"
```

Anagrams of `"abc"` inside `s` are:

```
"cba" → index 0
"bac" → index 6
```

So the answer is:

```
[0, 6]
```

Another example:

```
s = "abab"
p = "ab"
```

Windows of size 2:

```
"ab" → index 0 → anagram
"ba" → index 1 → anagram
"ab" → index 2 → anagram
```

Answer:

```
[0, 1, 2]
```

---

# Logic

We use a **sliding window**.

### Step 1: Count characters in `p`

For:

```
p = "abc"
```

we create:

```
d2 = {
    'a': 1,
    'b': 1,
    'c': 1
}
```

### Step 2: Create a window in `s`

The window size must always be:

```
len(p)
```

So if `p` has length `3`, we examine:

```
cba
bae
aeb
...
```

### Step 3: Keep frequency of the current window

For:

```
window = "cba"
```

we get:

```
d1 = {
    'c': 1,
    'b': 1,
    'a': 1
}
```

Compare:

```
d1 == d2
```

If equal → the window is an anagram → add `l`.

### Step 4: Slide the window

After checking the window, remove the leftmost character:

```
d1[s[l]] -= 1
```

If its count becomes zero, remove it:

```
if d1[s[l]] == 0:
    del d1[s[l]]
```

Then:

```
l += 1
```

and continue moving `r`.

---

# Code

```
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1={}
        d2={}
        l=0
        r=0
        L=[]
        for i in p:
            d2[i]=d2.get(i,0)+1
        
        while r<len(s):
            d1[s[r]] = d1.get(s[r], 0) + 1
            if r - l + 1 == len(p):
                if d1==d2:
                    L.append(l)
                d1[s[l]]-=1
                if d1[s[l]] == 0:
                    del d1[s[l]]
                l+=1
            r+=1
        return L
                       
            
```

### Complexity

Let `n = len(s)` and `m = len(p)`.

**Time Complexity: `O(n)`**

We move `r` through `s` once and `l` also moves only forward. The dictionaries contain at most 26 lowercase letters.

**Space Complexity: `O(1)`**

Because there can be at most 26 different lowercase English characters in the dictionaries.

### Pattern to remember

```
Create frequency of p
        ↓
Create sliding window in s
        ↓
Add right character
        ↓
Window size == len(p)?
        ↓
Compare frequencies
        ↓
Anagram → store left index
        ↓
Remove left character
        ↓
Move left
        ↓
Continue
```
