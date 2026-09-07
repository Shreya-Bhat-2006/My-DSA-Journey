# **Maximum Number of Vowels in a Substring of Given Length**

### 1. Problem Statement

Given a string `s` and an integer `k`, find the **maximum number of vowels** (`a, e, i, o, u`) present in any substring of length `k`.

**Example:**

```
Input:
s = "abciiidef"
k = 3

Output:
3
```

### 2. Example

All substrings of length `3`:

```
"abc" → 1 vowel
"bci" → 1 vowel
"cii" → 2 vowels
"iii" → 3 vowels  ← maximum
"iid" → 2 vowels
"ide" → 1 vowel
"def" → 1 vowel
```

Therefore:

```
Answer = 3
```

---

## 3. Logic to Solve

We need to check every substring of size `k`.

A simple approach would count vowels in every substring separately, but that would repeat work.

Instead, use a **fixed-size sliding window**.

### Maintain:

- `l` → left end of window
- `r` → right end of window
- `c` → number of vowels in current window
- `maxi` → maximum vowels found so far

### Steps

**Step 1: Expand the window**

Move `r` forward and check the new character.

```
ifs[r]invowels:c+=1
```

**Step 2: If window becomes bigger than `k`**

Remove the character at `l`.

```
ifs[l]invowels:c-=1l+=1
```

**Step 3: When window size becomes exactly `k`**

Update the maximum:

```
maxi=max(maxi,c)
```

### The important pattern

```
Add right element
       ↓
Window > k ?
   ↓       ↓
  YES      NO
   ↓        ↓
Remove     Continue
left
   ↓
   └──────┐
          ↓
     Window = k
          ↓
     Update maxi
```

---

## 4. Code

```python
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        c=0
        l=0
        r=0
        maxi=0
        d={'a', 'e', 'i', 'o','u'}
        for i in s:
            r+=1
            if r-l<=k:
                if i in d:
                    c+=1
            else:
                if s[l] in d:
                    c-=1
                l+=1
                if i in d:
                   c+=1
            if r-l == k:
                maxi = max(maxi, c)
                
        return maxi
            

                
```

### 5. Complexity

Let `n = len(s)`.

**Time Complexity: `O(n)`**

We move `r` from left to right once, and `l` also moves only forward.

**Space Complexity: `O(1)`**

The vowel set contains only 5 characters, so its size is constant.

### Final pattern to remember

For **fixed-size sliding window**:

> **Add → Shrink if too big → Update answer when size = k**.
>
