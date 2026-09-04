## Trapping Rain Water

### 1. Problem Statement

Given an array `height` where each number represents the height of a bar and each bar has width `1`, find the **total amount of rainwater that can be trapped** between the bars.

---

### 2. Example

**Example 1:**

```
Input:
height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output:
6
```

**Example 2:**

```
Input:
height = [4,2,0,3,2,5]

Output:
9
```

For Example 2:

```
[4, 2, 0, 3, 2, 5]

     water
4     █
█     █
█  █  █
█  █  █     █
█  █  █  █  █
█  █  █  █  █
----------------
4  2  0  3  2  5
```

Total trapped water = `2 + 4 + 1 + 2 = 9`.

---

# First Approach — Brute Force / Maximum on Both Sides

### Logic

For every bar:

1. Find the **maximum height on its left**.
2. Find the **maximum height on its right**.
3. Take the smaller of these two maximums.
4. Subtract the current bar's height.
5. Add the result to `count`.

Formula:

```
water = min(left_max, right_max) - current_height
```

If the result is negative, we take `0`.

### Code

```
class Solution:
    def trap(self, height: List[int]) -> int:

        cur = 1
        count = 0

        while cur < len(height) - 1:

            left_max = max(height[:cur])
            right_max = max(height[cur+1:])

            water_level = min(left_max, right_max)

            count += max(0, water_level - height[cur])

            cur += 1

        return count
```

### Complexity

```
Time:  O(n²)
Space: O(n)
```

Why `O(n²)`?

Because for every bar, we repeatedly search for:

```
max(height[:cur])max(height[cur+1:])
```

---

# Second Approach — Two Pointers

This is the **optimal approach**.

### Logic

Instead of finding the maximum on the left and right again and again, we maintain:

```
left_maxright_max
```

And use two pointers:

```
left →                 ← right

[4, 2, 0, 3, 2, 5]
```

At every step:

### Case 1

If:

```
height[left]<=height[right]
```

we process the **left side**.

Why?

Because the right side has a bar at least as tall as the current left bar, so the left side is the limiting side.

Then:

```
ifheight[left]>=left_max:left_max=height[left]
```

If the current bar is the new tallest left wall, there is no water above it.

Otherwise:

```
count+=left_max-height[left]
```

The difference is the trapped water.

---

### Case 2

If:

```
height[left]>height[right]
```

we process the **right side**.

If:

```
height[right]>=right_max:right_max=height[right]
```

we update the maximum.

Otherwise:

```
count+=right_max-height[right]
```

That difference is the trapped water.

---

### Code

Your version:

```
class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        left_max = 0

        right = len(height) - 1
        right_max = 0

        count = 0

        while left < right:

            if height[left] > height[right]:

                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    count += left_max - height[left]

                left += 1

            else:

                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    count += right_max - height[right]

                right -= 1

        return count
```

### Complexity

```
Time:  O(n)
Space: O(1)
```

### In short

| Approach | Idea | Time | Space |
| --- | --- | --- | --- |
| **First** | Find max left & max right for every bar | `O(n²)` | `O(n)` |
| **Second** | Two pointers + maintain left/right maximum | `O(n)` | `O(1)` |
