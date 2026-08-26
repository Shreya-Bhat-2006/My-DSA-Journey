# Intersection of Two Arrays II

## 1. Problem Statement

Given two integer arrays `nums1` and `nums2`, find their **intersection**.

The important point is that **duplicates should be included** as many times as they appear in **both arrays**.

You can return the answer in **any order**.

---

## 2. Example

### Example 1

```
Input:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

Output:
[2, 2]
```

Why?

```
nums1 → 2 appears 2 times
nums2 → 2 appears 2 times
```

So `2` appears **2 times** in the result.

---

### Example 2

```
Input:
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

Output:
[4, 9]
```

`[9, 4]` is also correct because the order doesn't matter.

---

# 3. Logic

We use a **dictionary** to store how many times each number appears in `nums1`.

### Step 1: Count `nums1`

For:

```
nums1 = [1, 2, 2, 1]
```

we create:

```
d = {
    1: 2,
    2: 2
}
```

Meaning:

```
1 → appears 2 times
2 → appears 2 times
```

### Step 2: Go through `nums2`

For every number in `nums2`:

- Check if it exists in the dictionary.
- Check if its count is greater than `0`.
- If yes → add it to the result.
- Decrease its count by `1`.

For:

```
nums2 = [2, 2]
```

First `2`:

```
d[2] = 2
```

Add `2`:

```
result = [2]
d[2] = 1
```

Second `2`:

```
d[2] = 1
```

Add `2`:

```
result = [2, 2]
d[2] = 0
```

So the final result is:

```
[2, 2]
```

### In short:

```
Count nums1
     ↓
Go through nums2
     ↓
Is number present?
     ↓
Is its count > 0?
     ↓
Yes → add to result
     ↓
Decrease count
```

---

# 4. Code

```
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        d={}
        for i in nums1:
            d[i]=d.get(i,0)+1
        for num in nums2:
            if num in d and d[num]>0:
               l.append(num)
               d[num]-=1
        return l
```

# 5. Complexity

Let:

- `n` = length of `nums1`
- `m` = length of `nums2`

### Time Complexity

We go through both arrays once:

```
O(n + m)
```

### Space Complexity

The dictionary stores the counts of elements in `nums1`:

```
O(n)
```

### Final

```
Time:  O(n + m)
Space: O(n)
```

**Key idea to remember:**

> **Count the elements of the first array, then consume those counts while checking the second array.**
>
