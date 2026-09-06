# **Merge Sorted Array**

## 1. Problem Statement

You are given two sorted arrays:

- `nums1` contains `m` valid elements followed by `n` empty spaces (`0`s).
- `nums2` contains `n` sorted elements.
- Merge `nums2` into `nums1` so that `nums1` becomes one sorted array.
- You must modify `nums1` **in-place**.
- Do not return the array.

### Example

```
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Output:
[1,2,2,3,5,6]
```

---

## 2. Logic to Solve

The main problem is:

If we merge from the **left side**, we may overwrite elements of `nums1` that we still need.

So, we merge from the **right side**.

We use **3 pointers**:

```
r1 → last valid element of nums1
r2 → last element of nums2
p  → last empty position in nums1
```

Initially:

```
r1 = m - 1
r2 = n - 1
p = m + n - 1
```

### Step 1: Compare from the back

Compare:

```
nums1[r1] and nums2[r2]
```

Take the **larger element** and put it at:

```
nums1[p]
```

Then move the pointer of the element we used backward.

Also move `p` backward.

### Step 2: Continue

Keep doing this while both arrays have elements:

```
while r1 >= 0 and r2 >= 0
```

### Step 3: Copy remaining `nums2`

If `nums1` finishes first, `nums2` may still contain elements.

Copy those remaining elements into `nums1`.

We don't need to copy remaining `nums1` elements because they are already in the correct position.

### Example

```
nums1 = [1,5,6,0,0,0]
nums2 = [2,4,5]
```

Start from the right:

```
6 vs 5 → put 6
5 vs 5 → put 5
5 vs 4 → put 5
1 vs 4 → put 4
1 vs 2 → put 2
```

Result:

```
[1,2,4,5,5,6]
```

---

## 3. Code

```
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        r1=m-1
        r2=n-1
        p=len(nums1)-1
        while r1>=0 and r2>=0:
            if nums1[r1]>nums2[r2]:
                nums1[p]=nums1[r1]
                r1-=1
                

            else:
                nums1[p]=nums2[r2]
                r2-=1
            p-=1
        while r2>=0:
            nums1[p]=nums2[r2]
            p-=1
            r2-=1

            
```

## 4. Complexity

### Time Complexity: `O(m + n)`

Every element from both arrays is considered at most once.

### Space Complexity: `O(1)`

We don't create another array. We modify `nums1` directly.
