# 4Sum

## 1. Problem Statement

Given an integer array `nums` and an integer `target`, find **all unique quadruplets** `[a, b, c, d]` such that:

- The four elements come from **different indices**.
- Their sum is equal to `target`.
- The result should not contain duplicate quadruplets.

### Example

**Input:**

`nums = [1,0,-1,0,-2,2]`

`target = 0`

**Output:**

`[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]`

---

# 2. Logic to Solve

### Step 1: Sort the array

First, sort the array.

Sorting helps us:

- Use the two-pointer technique.
- Easily identify and skip duplicate values.

Example:

`[1,0,-1,0,-2,2]`

becomes:

`[-2,-1,0,0,1,2]`

---

### Step 2: Fix the first element

Choose one element as the **first element** of the quadruplet.

Move through the array and try every possible first element.

If the current value is the same as the previous value, skip it to avoid duplicate quadruplets.

---

### Step 3: Fix the second element

For every first element, choose a **second element** from the remaining part of the array.

Again, if the current second value is the same as the previous second value, skip it to avoid duplicates.

Now the first two numbers are fixed.

---

### Step 4: Use two pointers

For the remaining two numbers, use:

- **Left pointer** → starts just after the second element.
- **Right pointer** → starts at the end of the array.

Calculate the sum of the four selected elements.

---

### Step 5: Compare the sum with the target

There are three possibilities:

**If sum < target:**

Move the left pointer to the right.

Because the array is sorted, this increases the sum.

**If sum > target:**

Move the right pointer to the left.

This decreases the sum.

**If sum = target:**

We found a valid quadruplet.

Add it to the result and move both pointers.

---

### Step 6: Skip duplicates

After finding a valid quadruplet, skip repeated values for the left and right pointers.

This prevents the same quadruplet from being added multiple times.

---

## 3. Code

```
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        L=[]
       
        sum=0
        
        for i in range(0,len(nums)-3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and  nums[j]==nums[j-1]:
                    continue
                left=j+1
                right=len(nums)-1
                while left<right:
                    sum=nums[i]+nums[j]+nums[left]+nums[right]
                    if sum<target:
                        left+=1
                    elif sum>target:
                        right-=1
                    else:
                        L.append([nums[i],nums[j],nums[left],nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                        
                    
        return L

            

```

## 4. Complexity

**Time Complexity:** `O(n³)`

- Sorting → `O(n log n)`
- Selecting first two elements + two-pointer search → `O(n³)`
- Overall → **`O(n³)`**

**Space Complexity:** `O(1)` extra space, excluding the output list.

### Easy way to remember

**Sort → Fix first → Fix second → Two pointers → Compare sum → Skip duplicates**
