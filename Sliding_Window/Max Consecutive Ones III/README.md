# **Max Consecutive Ones III**

> **Note:** The code you solved is actually for **“Max Consecutive Ones III”**, where you can flip at most `k` zeros to `1`. So I'll document the exact problem you solved.
> 

## 1. Problem Statement

Given a binary array `nums` containing only `0` and `1`, and an integer `k`, return the **maximum number of consecutive `1`s** in the array if you can **flip at most `k` zeros into ones**.

### Example 1

```
Input:
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2

Output:
6
```

### Explanation

We can choose the subarray:

```
[1,1,1,0,0,1]
```

It contains exactly **2 zeros**.

Flip those two zeros:

```
[1,1,1,1,1,1]
```

Therefore, the length is:

```
6
```

So the answer is:

```
6
```

---

## 2. Example 2

```
Input:
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

Output:
10
```

We need to find the **longest continuous subarray containing at most 3 zeros**.

One possible valid window has length `10`.

The zeros inside that window can be flipped to `1`.

Therefore:

```
Output = 10
```

---

# 3. Main Logic

The important observation is:

> We don't actually need to flip any zeros.
> 

Instead, we need to find:

> **The longest continuous subarray containing at most `k` zeros.**
> 

Why?

Suppose:

```
[1,1,0,0,1,1]
```

There are `2` zeros.

If:

```
k = 2
```

we can flip both:

```
[1,1,1,1,1,1]
```

Therefore, this window is valid.

But:

```
[1,1,0,0,0,1]
```

has `3` zeros.

If:

```
k = 2
```

we cannot flip all three.

Therefore, this window is invalid.

So our condition is simply:

```
number of zeros <= k
```

---

# 4. Sliding Window

We use two pointers:

```
l = left pointer
r = right pointer
```

and maintain a window:

```
[l ........ r]
```

We also maintain:

```
c = number of zeros in the current window
```

### Step 1 — Expand the window

Move `r` from left to right.

Whenever:

```
nums[r] == 0
```

increase:

```
c += 1
```

---

### Step 2 — Check whether the window is valid

A window is valid when:

```
c <= k
```

If:

```
c > k
```

the window has too many zeros.

---

### Step 3 — Shrink the window

Move `l` forward until the window becomes valid again.

When removing an element:

```
if nums[l] == 0:    c -= 1l += 1
```

So after the `while` loop:

```
c <= k
```

again.

---

### Step 4 — Calculate the window length

The current window is:

```
[l ........ r]
```

Its length is:

```
r - l + 1
```

Keep the maximum:

```
maxi = max(maxi, r - l + 1)
```

---

# 5. Dry Run

Consider:

```
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
```

Initially:

```
l = 0
c = 0
maxi = 0
```

We keep expanding `r`.

Eventually we get:

```
[1,1,1,0,0]
```

Number of zeros:

```
c = 2
```

Valid because:

```
2 <= k
```

Length:

```
5
```

Then we add another `0`:

```
[1,1,1,0,0,0]
```

Now:

```
c = 3
```

But:

```
3 > 2
```

So the window is invalid.

We move `l` forward until one zero is removed.

Now the window becomes valid again.

We continue this process until we've checked the entire array.

The maximum valid window length is:

```
6
```

---

# 6. Code

```python
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=0
        c=0
        maxi=0
        for r in range(len(nums)):
            
            if nums[r]==0:
                c+=1

            
            while c>k:
                if nums[l]==0:
                    l+=1
                    c-=1
                else:
                    l+=1
                    
            valid=r-l+1
                    

            if valid>maxi:
                maxi=valid

        return maxi
            
            
```

---

# 7. Why `while`, not `if`?

This is important.

We use:

```
while c > k:
```

because we need to keep removing elements until the window becomes valid.

For example:

```
k = 2
c = 4
```

We have too many zeros.

Removing one zero gives:

```
c = 3
```

Still invalid.

So we need to continue.

Removing another zero:

```
c = 2
```

Now it is valid.

Therefore:

```
while c > k:
```

is the correct approach.

---

# 8. Why do we always do `l += 1`?

We have:

```
while c > k:    if nums[l] == 0:        c -= 1    l += 1
```

The important thing is that `l` must **always move**.

If the element being removed is `0`, we decrease `c`.

If it's `1`, we don't change `c`.

But in both cases:

```
l += 1
```

because we're removing that element from the window.

---

# 9. Complexity

### Time Complexity: `O(n)`

`r` moves from left to right once.

`l` also moves from left to right at most once through the array.

Therefore:

```
Time = O(n)
```

Even though there is a `for` loop and a `while` loop, it is **not `O(n²)`**.

---

### Space Complexity: `O(1)`

We only use a few variables:

```
l
r
c
maxi
valid
```

No extra array or data structure is used.

Therefore:

```
Space = O(1)
```

---

# 10. Pattern to Remember

Whenever you see a problem like:

> **Find the longest/shortest continuous subarray satisfying some condition**
> 

think:

```
Sliding Window
      ↓
Two pointers
      ↓
left + right
      ↓
Maintain some condition
      ↓
If invalid → move left
      ↓
If valid → calculate answer
```

For this problem specifically:

```
Longest window
       ↓
At most k zeros
       ↓
Sliding window
       ↓
Count zeros
       ↓
If zeros > k → shrink
       ↓
r - l + 1
       ↓
Maximum
```
