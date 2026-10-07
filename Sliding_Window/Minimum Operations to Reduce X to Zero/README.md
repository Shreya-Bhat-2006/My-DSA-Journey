# **Minimum Operations to Reduce X to Zero**

## Problem Statement

You are given an integer array `nums` and an integer `x`.

In one operation, you can remove either the **leftmost** or the **rightmost** element from `nums` and subtract its value from `x`.

The array changes after every operation.

Return the **minimum number of operations** required to reduce `x` to exactly `0`. If it is impossible, return `-1`.

### Example 1

```
Input:  nums = [1,1,4,2,3], x = 5
Output: 2
```

**Explanation:** Remove `2` and `3` from the right:

```
5 - 2 - 3 = 0
```

So the answer is `2`.

### Example 2

```
Input:  nums = [5,6,7,8,9], x = 4
Output: -1
```

It is impossible to obtain `4` by removing elements only from the two ends.

### Example 3

```
Input:  nums = [3,2,20,1,1,3], x = 10
Output: 5
```

Remove:

```
3 + 2       from the left
1 + 1 + 3   from the right
```

Total:

```
3 + 2 + 1 + 1 + 3 = 10
```

So the answer is `5`.

---

# Logic to Solve

The direct approach would be to try different combinations of removing elements from the left and right. That can become expensive.

Instead, we use a **complementary idea**.

### Step 1: Find the total sum

Let:

```
total = sum(nums)
```

Suppose we remove elements whose sum is `x`.

Then the elements we **don't remove** must have sum:

```
total - x
```

So instead of finding the elements to remove, we find the **longest contiguous subarray whose sum is `total - x`**.

Why contiguous?

Because after removing elements from the left and right, the elements remaining in the middle always form a contiguous subarray.

---

### Step 2: Calculate the target

```
target = total - x
```

For example:

```
nums = [1,1,4,2,3]
x = 5

total = 11

target = 11 - 5
       = 6
```

Now we need to find the **longest subarray with sum `6`**.

```
[1, 1, 4] = 6
```

We keep these 3 elements.

Therefore, we remove:

```
5 - 3 = 2 elements
```

Answer:

```
2
```

---

### Step 3: Use Sliding Window

All `nums[i]` are **positive**, which makes sliding window possible.

Maintain:

```
l = left side of window
r = right side of window
summ = current window sum
```

For every `r`:

```
summ += nums[r]
```

If the sum becomes greater than the target:

```
while summ > target:    summ -= nums[l]    l += 1
```

When:

```
summ == target
```

we have found a valid subarray.

Calculate its length:

```
r - l + 1
```

and keep the **maximum length**.

Finally:

```
minimum operations = n - longest subarray length
```

---

### Special Cases

If:

```
target < 0
```

then:

```
sum(nums) < x
```

There isn't enough total sum to reduce `x` to zero.

So return:

```
-1
```

If:

```
target == 0
```

then we need to remove the **entire array**, so:

```
return len(nums)
```

If no subarray with sum `target` exists, return `-1`.

---

# Code

```python
class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        target=sum(nums)-x
        if target<0:
            return -1
        if target==0:
            return len(nums)
        l=0
        maxi=-1
        summ=0
        for r in range(len(nums)):
            summ+=nums[r]
            while summ>target:
                summ-=nums[l]
                l+=1
            if summ==target:
                maxi=max(maxi,r-l+1)
        if maxi==-1:
            return -1
        return (len(nums)-maxi)
```

# Complexity

### Time Complexity

```
O(n)
```

Each element is added to the window once and removed from the window at most once.

### Space Complexity

```
O(1)
```

We only use a few variables (`l`, `r`, `summ`, `maxi`), without any additional data structure.

### Final Idea to Remember

The most important trick is:

```
Remove elements with sum x
          ↓
Keep elements with sum total - x
          ↓
Find the LONGEST such subarray
          ↓
answer = n - longest_length
```

This converts an **"remove from both ends"** problem into a **sliding-window longest-subarray** problem.
