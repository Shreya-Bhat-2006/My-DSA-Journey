# **Subarrays with K Different Integers**

## 1. Problem Statement

### Subarrays with K Different Integers

Given an integer array `nums` and an integer `k`, return the **number of contiguous subarrays that contain exactly `k` distinct integers**.

A distinct integer means a different value.

### Example

```
nums = [1,2,1,2,3]
k = 2
```

The subarrays containing exactly 2 distinct integers are:

```
[1,2]
[2,1]
[1,2]
[2,1,2]
[1,2,1]
[1,2,1,2]
```

Therefore:

```
Answer = 6
```

---

# 2. Logic to Solve

Directly finding subarrays with **exactly K** distinct values is slightly difficult.

So we use this important formula:

```
Exactly K
=
At Most K
-
At Most (K - 1)
```

### Why?

`At Most K` contains:

```
1 distinct
2 distinct
3 distinct
...
K distinct
```

`At Most K-1` contains:

```
1 distinct
2 distinct
...
K-1 distinct
```

When we subtract:

```
At Most K
-
At Most K-1
```

everything from `1` through `K-1` gets removed, leaving only:

```
Exactly K
```

---

## How do we find `At Most K`?

Use a **sliding window**.

Maintain:

```
l = left pointer
r = right pointer
```

and a dictionary:

```
s = {}
```

to store the frequency of each number in the current window.

### Step 1 — Expand the window

Move `r` from left to right:

```
s[nums[r]] = s.get(nums[r], 0) + 1
```

### Step 2 — If there are too many distinct values

If:

```
len(s) > k
```

move `l` forward and remove elements from the dictionary.

```
while len(s) > k:    s[nums[l]] -= 1    if s[nums[l]] == 0:        del s[nums[l]]    l += 1
```

After this loop:

```
len(s) <= k
```

So the current window contains **at most K distinct integers**.

---

## Step 3 — Count the valid subarrays

This is the important part:

```
ans += r - l + 1
```

Why?

If the current valid window is:

```
l             r
↓             ↓
[-------------]
```

then all these subarrays ending at `r` are valid:

```
[l ........ r]
[l+1 ...... r]
[l+2 .......r]
...
[r ........ r]
```

The number of possible starting positions is:

```
r - l + 1
```

So we add:

```
ans += r - l + 1
```

for every `r`.

---

# 3. Code

```
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atmost(k):
            s={}
            l=0
            ans=0
            for r in range (len(nums)):
                s[nums[r]]=s.get(nums[r],0)+1
                while len(s)>k:
                    s[nums[l]]-=1
                    if s[nums[l]]==0:
                        del(s[nums[l]])
                    l+=1
                ans+=r-l+1
            return ans
        return atmost(k)-atmost(k-1)
```

# 4. Complexity

### Time Complexity: **O(n)**

Each element is:

- added to the window once by `r`
- removed from the window at most once by `l`

And we call `atmost()` twice:

```
atmost(k)
atmost(k-1)
```

So:

```
O(n) + O(n) = O(n)
```

### Space Complexity: **O(k)**

The dictionary stores the distinct elements in the current window.

So approximately:

```
O(k)
```
