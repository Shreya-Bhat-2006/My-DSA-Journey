# LeetCode: Search Insert Position

## 1. Problem Statement

Given a sorted array of distinct integers `nums` and an integer `target`, return the index if the target is found.

If the target is not found, return the index where it would be inserted in order.

You must write an algorithm with O(log n) runtime complexity.

### Example 1

Input:

```
nums = [1, 3, 5, 6]target = 5
```

Output:

```
2
```

Explanation: The target `5` exists at index `2`.

### Example 2

Input:

```
nums = [1, 3, 5, 6]target = 2
```

Output:

```
1
```

Explanation: The number `2` should be inserted at index `1`, between `1` and `3`.

### Example 3

Input:

```
nums = [1, 3, 5, 6]target = 7
```

Output:

```
4
```

Explanation: The number `7` should be inserted at the end of the array.

## 2. Logic to solve

We use Binary Search because the array is sorted.

1. Initialize `l = 0` and `r = len(nums) 1`.
2. Calculate the middle index: `mid = (l + r) // 2`.
3. Compare `nums[mid]` with `target`:
    - If equal, return `mid`.
    - If `nums[mid] < target`, search the right half by setting `l = mid + 1`.
    - Otherwise, search the left half by setting `r = mid 1`.
4. Repeat while `l <= r`.
5. If the target is not found, return `l`, which is the correct insertion position.

## 3. Python code

```
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(r+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return l
```

## 4. Complexity analysis

- Time complexity: (O(log n)) — Each iteration eliminates approximately half of the remaining search space.
- Space complexity: (O(1)) — We use only a constant number of variables (`l`, `r`, and `mid`).
