# 3Sum Closest

## 1. Problem Statement

Given an integer array `nums` and an integer `target`, find **three different elements** in the array whose sum is **closest to `target`**.

Return the **sum of those three elements**.

You can assume that there is **exactly one answer**.

---

## 2. Example 1

```
Input:
nums = [-1, 2, 1, -4]
target = 1
```

First sort:

```
[-4, -1, 1, 2]
```

Possible 3-number sums include:

```
-4 + -1 + 2 = -3
-4 + 1 + 2  = -1
-1 + 1 + 2  = 2
```

Compare with target `1`:

```
|-3 - 1| = 4
|-1 - 1| = 2
| 2 - 1| = 1   ← closest
```

Therefore:

```
Output = 2
```

---

## 3. Example 2

```
Input:
nums = [0, 0, 0]
target = 1
```

Only possible sum:

```
0 + 0 + 0 = 0
```

Difference:

```
|1 - 0| = 1
```

Therefore:

```
Output = 0
```

---

# 4. Logic to Solve

The main idea is:

### Step 1: Sort the array

```
nums.sort()
```

Sorting allows us to use the **two-pointer technique**.

---

### Step 2: Fix one number using `i`

```
foriinrange(len(nums)-2):
```

`i` represents the **first number**.

For example:

```
nums = [-4, -1, 1, 2]

         i
         ↓
[-4, -1, 1, 2]
```

---

### Step 3: Use two pointers for the remaining two numbers

```
l=i+1r=len(nums)-1
```

So:

```
         i    l          r
         ↓    ↓          ↓
[-4,    -1,   1,         2]
```

Now we have:

```
nums[i]+nums[l]+nums[r]
```

---

### Step 4: Calculate the current sum

```
cur=nums[i]+nums[l]+nums[r]
```

---

### Step 5: Check whether this sum is closer

```
ifabs(target-cur)<abs(target-close):close=cur
```

`close` stores the **closest sum found so far**.

We initialize it with a real 3-number sum:

```
close=nums[0]+nums[1]+nums[2]
```

---

### Step 6: Move the pointers

This is the most important part.

#### If current sum is too small:

```
ifcur<target:l+=1
```

We need a **larger sum**, so move `l` right.

```
l →
```

Because the array is sorted, moving right gives a larger number.

#### If current sum is too large:

```
elifcur>target:r-=1
```

We need a **smaller sum**, so move `r` left.

#### If exactly equal:

```
else:returncur
```

Because if:

```
cur == target
```

then the difference is:

```
0
```

Nothing can be closer than that. 🎯

---

# 5. Code

```
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
     
        cur=0
        close = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):

            l=i+1
            r=len(nums)-1
            while l<r:
                cur=nums[i]+nums[l]+nums[r]
                if (abs(target-cur)<abs(target-close)):
                    close=cur
                if cur<target:
                    l+=1
                elif cur>target:
                    r-=1
                else :
                    return cur
        return close
```

# 6. Dry Run

For:

```
nums = [-1, 2, 1, -4]
target = 1
```

After sorting:

```
[-4, -1, 1, 2]
```

Start:

```
close = -4 + -1 + 1
      = -4
```

### `i = 0`

```
i   l       r
↓   ↓       ↓
-4  -1   1   2
```

```
cur = -4 + -1 + 2
    = -3
```

- `3` is closer than `4`, so:

```
close = -3
```

Since `-3 < 1`:

```
l++
```

---

Next:

```
i   l   r
↓   ↓   ↓
-4   1  2
```

```
cur = -4 + 1 + 2
    = -1
```

Update:

```
close = -1
```

Again `cur < target`, so `l++`.

---

### `i = 1`

```
i   l   r
↓   ↓   ↓
-1   1  2
```

```
cur = -1 + 1 + 2
    = 2
```

Difference from target:

```
|1 - 2| = 1
```

So:

```
close = 2
```

Final:

```
Output = 2
```

---

# 7. Complexity

### Time Complexity

Sorting:

```
O(n log n)
```

Outer `for` loop + two pointers:

```
O(n²)
```

Overall:

```
O(n²)
```

### Space Complexity

Apart from sorting:

```
O(1)
```
