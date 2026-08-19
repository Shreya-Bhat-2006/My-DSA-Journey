# Minimum Window Substring

## Problem Statement

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the **minimum window substring of `s`** such that every character in `t`, including duplicates, is included in the window.

If no such substring exists, return `""`.

The answer is guaranteed to be unique.

### Example 1

```
Input:
s = "ADOBECODEBANC"
t = "ABC"

Output:
"BANC"
```

**Explanation:**

`"BANC"` contains:

```
A → 1
B → 1
C → 1
```

and it is the smallest substring of `s` containing all characters of `t`.

### Example 2

```
Input:
s = "a"
t = "a"

Output:
"a"
```

### Example 3

```
Input:
s = "a"
t = "aa"

Output:
""
```

**Explanation:** `t` requires two `a`s, but `s` contains only one.

---

# Logic 1 — Dictionary + Sliding Window

### Idea

Maintain two dictionaries:

```
d2 → characters required from t
d1 → characters currently present in the window
```

For example:

```
t = "AABC"
```

Then:

```
d2 = {
    'A': 2,
    'B': 1,
    'C': 1
}
```

We use two pointers:

```
left
right
```

The window is:

```
s[left:right]
```

### Steps

1. Create `d2` containing the frequency of every character in `t`.
2. Move `right` forward and add characters to `d1`.
3. Check whether `d1` contains all required characters and frequencies.
4. Once the window is valid:
    - Save the window if it is the smallest.
    - Move `left` forward to shrink it.
5. Stop shrinking when the window becomes invalid.
6. Continue expanding `right`.

### Code

```
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d1={}
        d2={}
        for i in t:
            if i in d2:
                d2[i]+=1
            else:
                d2[i]=1

        left=0
        right=0
        
        st=""
        while right<len(s):
            valid=True
            d1[s[right]]=d1.get(s[right],0)+1
            right+=1
            for key,value in d2.items():
                if d1.get(key,0)<value:
                   valid=False
                   break
            
                
            while valid:
                if st == "" or right - left < len(st):
                   st = s[left:right]
                
                d1[s[left]]-=1
                left+=1
                valid=True
                for key,value in d2.items():
                    if d1.get(key,0)<value:
                       valid=False
                       break
        return st

```

### Complexity

Let:

- `m = len(s)`
- `n = len(t)`
- `k = number of unique characters in t`

Since we repeatedly loop through `d2`:

```
Time:  O(m × k)
Space: O(k)
```

In the worst case, `k = n`:

```
Time:  O(m × n)
Space: O(n)
```

This solution is **correct**, but it repeatedly checks the entire dictionary, so we can optimize it.

---

# Logic 2 — Optimized Sliding Window Using `formed`

The main problem with Logic 1 is this:

```
for key, value in d2.items():
```

We don't need to check every character every time.

Instead, we keep track of how many character requirements are currently satisfied.

### Example

Suppose:

```
t = "AABC"
```

Required:

```
A → 2
B → 1
C → 1
```

There are **3 unique requirements**:

```
required = 3
```

We maintain:

```
formed = 0
```

When the window contains enough `A`s:

```
A → 2
```

then:

```
formed += 1
```

When it also contains enough `B`:

```
formed += 1
```

And enough `C`:

```
formed += 1
```

Now:

```
formed == required
```

means the window is valid.

### Important

We increase `formed` only when:

```
window[ch] == required[ch]
```

For example:

```
required A = 2

window A = 1 → not satisfied
window A = 2 → satisfied → formed += 1
window A = 3 → still satisfied → DON'T increase formed
```

Similarly, when shrinking, if removing a character makes its count insufficient, we decrease `formed`.

---

## Code

```
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Characters required from t
        d2 = {}

        for ch in t:
            d2[ch] = d2.get(ch, 0) + 1

        # Number of unique characters we need to satisfy
        required = len(d2)

        # Characters currently in the window
        d1 = {}

        formed = 0

        left = 0
        right = 0

        start = 0
        min_len = float('inf')

        while right < len(s):

            # Add right character
            ch = s[right]
            d1[ch] = d1.get(ch, 0) + 1

            # Requirement for this character is now satisfied
            if ch in d2 and d1[ch] == d2[ch]:
                formed += 1

            right += 1

            # Current window is valid
            while formed == required:

                # Save smallest window
                if right - left < min_len:
                    min_len = right - left
                    start = left

                # Remove left character
                ch = s[left]
                d1[ch] -= 1

                # Removing this character made
                # the requirement unsatisfied
                if ch in d2 and d1[ch] < d2[ch]:
                    formed -= 1

                left += 1

        # No valid window
        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]
```

# Logic 2 Example

For:

```
s = "ADOBECODEBANC"
t = "ABC"
```

Initially:

```
required = 3
formed = 0
```

As `right` moves:

```
A → formed = 1

B → formed = 2

C → formed = 3
```

Now:

```
formed == required
```

so the window is valid:

```
ADOBEC
```

We start moving `left`:

```
ADOBEC
 ↑
left
```

Remove `A`:

```
DOBEC
```

Now `A` is missing:

```
formed = 2
```

So stop shrinking.

Continue moving `right`.

Eventually we get:

```
BANC
```

All requirements are satisfied:

```
A → 1
B → 1
C → 1

formed = 3
required = 3
```

And:

```
len("BANC") = 4
```

which is smaller than the previous valid windows.

Therefore:

```
Output = "BANC"
```

---

# Complexity Comparison

| Approach | Time | Space |
| --- | --- | --- |
| **Logic 1 — Dictionary checking** | `O(m × k)` | `O(k)` |
| **Logic 2 — `formed` optimization** | **`O(m + n)`** | `O(n)` |

Where `k` is the number of unique characters in `t`.

### What to remember for the exam/interview

**Logic 1:**

```
Expand → check entire dictionary → shrink
```

**Logic 2:**

```
Expand → update formed → shrink while formed == required
```
