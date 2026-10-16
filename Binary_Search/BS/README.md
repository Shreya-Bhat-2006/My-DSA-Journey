# Problem 1: Binary Search (LeetCode 704)

## 1. Problem Statement

Given an array of integers `nums` sorted in ascending order and an integer `target`, find the index of `target` in the array.

If the target exists, return its index. Otherwise, return `-1`.

Example:

Input: nums = [-1, 0, 3, 5, 9, 12], target = 9

Output: 4

Explanation: The target 9 is present at index 4.

## 2. Logic to Solve

1. Initialize `l = 0` and `r = len(nums) - 1`.
2. Run a loop while `l <= r`.
3. Calculate the middle index using `mid = (l + r) // 2`.
4. If `nums[mid] == target`, return `mid`.
5. If `nums[mid] < target`, search the right half by setting `l = mid + 1`.
6. Otherwise, search the left half by setting `r = mid - 1`.
7. If the target is not found, return `1`.

Why Binary Search?

The array is sorted. Instead of checking every element one by one, we eliminate half of the remaining search space in each iteration.

## 3. Python Code

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1
```

## 4. Complexity Analysis

Time Complexity: O(log n)

Reason: The search space is reduced by half in every iteration.

Space Complexity: O(1)

Reason: Only a constant number of variables are used, regardless of the array size.
