# 1. Remove Duplicates from Sorted Array

### Problem Statement

You are given a **sorted array** `nums`.

Remove the duplicate elements **in-place** so that every element appears only once.

Return the **number of unique elements**.

The order of the unique elements should remain the same.

**Example:**

```
Input:
nums = [1,1,2,2,3]

Output:
3

Modified nums:
[1,2,3,_,_]
```

Only the first `3` elements matter because we returned `3`.

---

# 2. Logic to Solve

Since the array is **sorted**, all duplicates are next to each other.

For example:

```
[1,1,2,2,3,3]
```

So we use **two pointers**:

- `slow` → points to the **last unique element**
- `fast` → scans the array to find the next unique element

Initially:

```
slow = 0
fast = 1
```

### Step 1

```
[1,1,2,2,3]
 ↑ ↑
slow fast
```

`nums[slow] == nums[fast]`

Both are `1`, so it's a duplicate.

➡️ Don't move `slow`.

Move `fast`.

---

### Step 2

```
[1,1,2,2,3]
 ↑    ↑
slow fast
```

Now:

```
nums[slow] != nums[fast]
1 != 2
```

We found a **new unique element**.

So:

```
slow+=1nums[slow]=nums[fast]
```

Array becomes:

```
[1,2,2,2,3]
   ↑
  slow
```

Then continue.

Eventually:

```
[1,2,3,2,3]
```

We return:

```
slow + 1 = 3
```

Therefore, the unique elements are:

```
[1,2,3]
```

### The important idea

We are **not actually deleting elements**.

We are simply **moving unique elements to the front** of the array.

---

# 3. Code

```
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
           return 0
        slow=0
        fast=1
        while fast<len(nums):
            if nums[slow]!=nums[fast]: 
                slow+=1
                nums[slow]=nums[fast]
    
            fast+=1
        return slow+1

        
```

# 4. Complexity

### Time Complexity: `O(n)`

`fast` goes through the array once.

```
n elements → one scan → O(n)
```

### Space Complexity: `O(1)`

We don't create another array.

We only use:

```
slow
fast
```

So:

```
Time  → O(n)
Space → O(1)
```
