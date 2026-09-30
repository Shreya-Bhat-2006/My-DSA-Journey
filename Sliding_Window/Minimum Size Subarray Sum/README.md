# Minimum Size Subarray Sum

## 1. Problem Statement

Given an array of **positive integers** `nums` and a positive integer `target`, find the **minimum length of a contiguous subarray** whose sum is **greater than or equal to `target`**.

If no such subarray exists, return `0`.

### In simple words:

We need to find a **continuous part of the array** whose sum is at least `target`, and among all possible parts, return the **smallest length**.

---

## 2. Example

### Example 1

```
target = 7
nums = [2,3,1,2,4,3]
```

We need a subarray whose sum is at least `7`.

Possible valid subarrays:

```
[2,3,1,2]       sum = 8    length = 4
[3,1,2,4]       sum = 10   length = 4
[1,2,4]         sum = 7    length = 3
[2,4,3]         sum = 9    length = 3
[4,3]           sum = 7    length = 2
```

The smallest length is `2`.

```
Output = 2
```

---

### Example 2

```
target = 4
nums = [1,4,4]
```

The subarray:

```
[4]
```

already has sum `4`.

Therefore:

```
Output = 1
```

---

### Example 3

```
target = 11
nums = [1,1,1,1,1,1,1,1]
```

The total sum is only `8`.

So there is no subarray whose sum is at least `11`.

```
Output = 0
```

---

# 3. Logic to Solve It

We use the **Sliding Window** technique.

We maintain a window:

```
[l ........ r]
```

where:

- `l` = left pointer
- `r` = right pointer
- `cur_sum` = sum of elements inside the window

### Step 1: Expand the window

Move `r` from left to right.

Every time we move `r`, add:

```
cur_sum+=nums[r]
```

We keep expanding until:

```
cur_sum >= target
```

---

### Step 2: We found a valid window

Once:

```
cur_sum >= target
```

we have a valid subarray.

Calculate its length:

```
r-l+1
```

Update the smallest length:

```
Len=min(Len,r-l+1)
```

---

### Step 3: Shrink the window

Now we want to see whether we can make the window **smaller**.

Remove the leftmost element:

```
cur_sum-=nums[l]l+=1
```

We keep doing this **while the sum is still ≥ target**.

That's why we use:

```
whilecur_sum>=target:
```

---

### Step 4: Why does this work?

Because all `nums[i]` are **positive**.

Therefore:

```
Moving r → sum increases
Moving l → sum decreases
```

So:

```
sum < target
      ↓
  EXPAND using r

sum >= target
      ↓
  SHRINK using l
```

The whole idea is:

> **Expand until the window becomes valid, then shrink it as much as possible while keeping it valid.**
> 

---

# 4. Dry Run

For:

```
target = 7
nums = [2,3,1,2,4,3]
```

Start:

```
cur_sum = 0
l = 0
Len = infinity
```

### Expand

```
[2]
sum = 2
```

Not enough.

```
[2,3]
sum = 5
```

Not enough.

```
[2,3,1]
sum = 6
```

Not enough.

Add `2`:

```
[2,3,1,2]
sum = 8
```

Now:

```
8 >= 7
```

Length:

```
4
```

So:

```
Len = 4
```

Now shrink:

```
[3,1,2]
sum = 6
```

No longer valid, so stop shrinking.

---

Continue expanding.

Add `4`:

```
[3,1,2,4]
sum = 10
```

Length = `4`.

Shrink:

```
[1,2,4]
sum = 7
length = 3
```

Update:

```
Len = 3
```

Shrink again:

```
[2,4]
sum = 6
```

Stop.

---

Add `3`:

```
[2,4,3]
sum = 9
length = 3
```

Shrink:

```
[4,3]
sum = 7
length = 2
```

Update:

```
Len = 2
```

Shrink again:

```
[3]
sum = 3
```

Stop.

Final answer:

```
2
```

---

# 5. Code

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        cur_sum=0
        l=0
        Len=float("inf")
        for r in range(len(nums)):
            cur_sum+=nums[r]
           
            while cur_sum>=target:
                Len=min(Len,r-l+1)
                cur_sum-=nums[l] 
                l+=1
        if Len==float("inf"):
            return 0

        return Len
```

# 7. Complexity

### Time Complexity: `O(n)`

Although we have a `for` loop and a `while` loop, it is still `O(n)`.

Why?

- `r` moves from `0 → n-1` once.
- `l` also moves from `0 → n-1` at most once.

So the total number of pointer movements is at most about `2n`.

```
Time = O(n)
```

### Space Complexity: `O(1)`

We only use a few variables:

```
cur_sum
l
r
Len
```

No extra array or data structure.

```
Space = O(1)
```

## ⭐ The pattern to remember

For **Minimum Size Subarray Sum**:

```
1. Expand → move r
2. Add nums[r]
3. If sum >= target
4. Record length
5. Shrink → move l
6. Repeat while sum >= target
7. Keep the minimum length
```

**One-line memory trick:**

> **"Expand until valid, shrink while valid, keep the minimum."**
>
