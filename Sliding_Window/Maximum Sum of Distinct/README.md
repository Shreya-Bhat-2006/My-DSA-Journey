# Maximum Sum of Distinct Subarrays With Length K

## 1. Problem Statement

Given an integer array `nums` and an integer `k`, find the **maximum sum of a subarray of length `k`** where all the elements are **distinct**.

If there is no valid subarray, return `0`.

---

## 2. Examples

### Example 1

**Input:**

`nums = [1, 5, 4, 2, 9, 9, 9]`

`k = 3`

Subarrays of length 3:

- `[1, 5, 4]` → sum = 10 ✅
- `[5, 4, 2]` → sum = 11 ✅
- `[4, 2, 9]` → sum = 15 ✅
- `[2, 9, 9]` → duplicate ❌
- `[9, 9, 9]` → duplicate ❌

**Output: `15`**

---

### Example 2

**Input:**

`nums = [4, 4, 4]`

`k = 3`

The only subarray is `[4, 4, 4]`, but it contains duplicates.

**Output: `0`**

---

## 3. Logic to Solve

We use the **Sliding Window** technique.

We maintain a window between two pointers: `left` and `right`.

### Step 1: Expand the window

Move `right` through the array and add each new element to the current window.

We also maintain the sum of the current window.

### Step 2: Handle duplicates

Before adding a new element, check whether it is already present in the window.

If it is a duplicate, move `left` forward and remove elements from the window until the duplicate is removed.

This guarantees that the current window contains only distinct elements.

### Step 3: Check the window size

Once the window contains distinct elements, check its size.

If its size is exactly `k`, we have a valid subarray.

Compare its sum with the maximum sum found so far.

### Step 4: Move to the next window

Once a valid window of size `k` has been processed, remove the leftmost element and move `left` forward.

This allows the next window to be examined.

### Why use a Set?

A set lets us quickly check whether an element already exists in the current window.

### Why use a Running Sum?

Instead of calculating the entire window's sum every time, we update the sum whenever an element enters or leaves the window.

This makes the solution much faster.

---

## 4. Code

```python
class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        s=set()
        
        maxi=0
        left=0
        cur_sum=0
        for right in range(len(nums)):
            while nums[right]  in s:
                s.remove(nums[left])
                cur_sum-=nums[left]
                left+=1
                
                
        
            
            s.add(nums[right])
            cur_sum+=nums[right]             
            if right-left+1==k:
                if maxi<cur_sum:
                    maxi=cur_sum
                s.remove(nums[left])
                cur_sum-=nums[left]
                left+=1
        
        return maxi
            

       

```

## 5. Complexity

**Time Complexity:** `O(n)`

Each element is added and removed from the window at most once.

**Space Complexity:** `O(k)`

The set stores the elements currently inside the window.
