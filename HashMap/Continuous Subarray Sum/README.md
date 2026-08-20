# Continuous Subarray Sum

## 1. Problem Statement

Given an integer array `nums` and an integer `k`, return `True` if there exists a **contiguous subarray** that:

1. Has a length of **at least 2**
2. Has a sum that is a **multiple of `k`**

Otherwise, return `False`.

A number is a multiple of `k` if:

```
sum % k == 0
```

### Example

```
nums = [23, 2, 4, 6, 7]
k = 6
```

One valid subarray is:

```
[2, 4]
```

because:

```
2 + 4 = 6
6 % 6 = 0
```

So:

```
Output: True
```

There are actually other valid subarrays too:

```
[2, 4, 6] → 12 → 12 % 6 = 0
```

We only need **one** valid subarray.

---

# 2. Logic / Idea

The key idea is:

> **Use Prefix Sum + Remainder + HashMap.**
> 

### Step 1: Calculate prefix sum

For:

```
[23, 2, 4, 6, 7]
```

Prefix sums are:

```
23
25
29
35
42
```

### Step 2: Find the remainder

Since `k = 6`:

```
23 % 6 = 5
25 % 6 = 1
29 % 6 = 5
35 % 6 = 5
42 % 6 = 0
```

So:

```
Index:      0   1   2   3   4
Remainder:  5   1   5   5   0
```

We see remainder `5` again.

It occurred at:

```
index 0
index 2
```

If two prefix sums have the **same remainder**, their difference is divisible by `k`.

Here:

```
29 - 23 = 6
```

And that difference represents:

```
[2, 4]
```

whose sum is `6`.

---

# 3. What does the HashMap store?

We store:

```
remainder → first index
```

For example:

```
d = {
    0: -1,
    5: 0,
    1: 1
}
```

When we see remainder `5` again at index `2`:

```
2 - 0 = 2
```

Length is `2`, so:

```
True
```

### Why `{0: -1}`?

This handles a subarray that starts from index `0`.

For example:

```
nums = [2, 4]
k = 6
```

Prefix sum:

```
[2, 6]
```

At index `1`:

```
6 % 6 = 0
```

We pretend remainder `0` existed at index `-1`:

```
d = {0: -1}
```

Then:

```
1 - (-1) = 2
```

So `[2,4]` has length 2 → valid.

---

# 4. Algorithm

1. Create a variable `ps` for prefix sum.
2. Create a HashMap:
    
    ```
    d = {0: -1}
    ```
    
3. Traverse the array.
4. Add the current number to `ps`.
5. Calculate:
    
    ```
    r = ps % k
    ```
    
6. If `r` is already in the HashMap:
    - Calculate the distance between the current index and stored index.
    - If distance ≥ 2 → return `True`.
7. If `r` is not in the HashMap:
    - Store its index.
8. If we finish the loop without finding anything → return `False`.

### Important

We store **only the first index** of a remainder.

```
if r in d:
    # check distance
else:
    d[r] = i
```

We don't overwrite the first index.

---

# 5. Code

```
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        ps=0
        
        
        d={0:-1}
        for i in range(len(nums)):
            ps+=nums[i]
            r=ps%k
            if r in d:
                if i-d[r]>=2:
                    return True
            else:
                d[r]=i
        
       
            
        
        return False
        
```

# 6. Complexity

### Time Complexity

```
O(n)
```

We go through the array only once.

HashMap lookup is approximately `O(1)`.

### Space Complexity

```
O(n)
```

In the worst case, we may store up to `n` different remainders.
