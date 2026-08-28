# **Squares of a Sorted Array**

## 1. Problem Statement

Given a sorted integer array `nums`, return a new array containing the **squares of each number**, also sorted in **non-decreasing order**.

### Example

```
Input:
nums = [-7, -3, 2, 3, 11]

Output:
[4, 9, 9, 49, 121]
```

### Why?

First square every number:

```
(-7)² = 49
(-3)² = 9
2²   = 4
3²   = 9
11²  = 121
```

We get:

```
[49, 9, 4, 9, 121]
```

After sorting:

```
[4, 9, 9, 49, 121]
```

---

# 2. Logic to Solve

The simple approach is:

1. Square every element.
2. Sort the result.

But sorting takes **O(n log n)**.

We can do better using **Two Pointers** in **O(n)**.

### Step 1: Use two pointers

Since the array is already sorted:

```
[-7, -3, 2, 3, 11]
  ↑           ↑
  l           r
```

The **largest square** must come from either:

- the leftmost number `nums[l]`
- the rightmost number `nums[r]`

Why?

Because the numbers at the ends have the largest absolute values.

For example:

```
|-7| = 7
|11| = 11
```

So:

```
11² = 121
```

is the largest square.

---

### Step 2: Fill the answer from RIGHT to LEFT

Create:

```
ans= [0]*len(nums)
```

And use:

```
pos=len(nums)-1
```

The largest square goes at `ans[pos]`.

Example:

```
ans = [0, 0, 0, 0, 121]
                    ↑
                   pos
```

---

### Step 3: Compare the two ends

If:

```
abs(nums[l])>abs(nums[r])
```

take the left number:

```
ans[pos]=nums[l]*nums[l]l+=1
```

Otherwise, take the right number:

```
ans[pos]=nums[r]*nums[r]r-=1
```

After either case:

```
pos-=1
```

---

### Step 4: Continue until all elements are processed

Use:

```
whilel<=r:
```

The `<=` is important because when `l == r`, there is still **one element left** to process.

---

# 3. Code

---

```
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        pos=r
        l1=[0]*len(nums)
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
               
                l1[pos]=nums[l]*nums[l]
                l+=1
                pos-=1
            else:
                l1[pos]=nums[r]*nums[r]
                r-=1
                pos-=1
        
        return l1

            

```

# 4. Dry Run

For:

```
nums = [-7, -3, 2, 3, 11]
```

Initially:

```
l = 0
r = 4
pos = 4
```

### Step 1

Compare:

```
|-7| = 7
|11| = 11
```

Take `11² = 121`.

```
ans = [0, 0, 0, 0, 121]
```

Move `r` and `pos`.

---

### Step 2

Compare:

```
|-7| = 7
|3| = 3
```

Take `(-7)² = 49`.

```
ans = [0, 0, 0, 49, 121]
```

---

### Step 3

Compare:

```
|-3| = 3
|3| = 3
```

Take `3² = 9`.

```
ans = [0, 0, 9, 49, 121]
```

Continue...

Final:

```
[4, 9, 9, 49, 121]
```

---

# 5. Complexity

### Time Complexity: **O(n)**

Each element is processed only once.

### Space Complexity: **O(n)**

We create the `ans` array of size `n`.

```
Time  → O(n)
Space → O(n)
```
