### Problem Statement

Given an integer array `nums` and an integer `k`, return `True` if there are **two distinct indices** `i` and `j` such that:

```
nums[i] == nums[j]
```

and

```
abs(i - j) <= k
```

Otherwise, return `False`.

### Example 1

```
Input:
nums = [1, 2, 3, 1]
k = 3

Output:
True
```

Why?

`1` appears at indices `0` and `3`.

```
nums[0] = nums[3] = 1

|0 - 3| = 3
```

Since `3 <= k`, answer is `True`.

---

### Example 2

```
Input:
nums = [1, 0, 1, 1]
k = 1

Output:
True
```

The `1`s occur at:

```
index 0
index 2
index 3
```

Check the last two:

```
|3 - 2| = 1
```

Since `1 <= k`, answer is `True`.

---

### Example 3

```
Input:
nums = [1, 2, 3, 1, 2, 3]
k = 2

Output:
False
```

For `1`:

```
indices: 0, 3
distance = 3 > 2
```

For `2`:

```
indices: 1, 4
distance = 3 > 2
```

For `3`:

```
indices: 2, 5
distance = 3 > 2
```

So there is no valid pair.

---

# Logic

We use a dictionary `d`.

### What will the dictionary store?

For every number, store its **most recent index**.

For example:

```
nums = [1, 2, 3, 1]
```

After processing the first three elements:

```
d= {1:0,2:1,3:2
}
```

Meaning:

```
1 was last seen at index 0
2 was last seen at index 1
3 was last seen at index 2
```

When we see another `1` at index `3`:

```
3 - d[1]
= 3 - 0
= 3
```

Since:

```
3 <= k
```

we return `True`.

### Why store only the latest index?

Suppose:

```
1 occurs at indices: 0, 4, 7
k = 3
```

When we reach index `4`:

```
4 - 0 = 4 > 3
```

Not valid.

So we update:

```
d[1] = 4
```

When we reach index `7`:

```
7 - 4 = 3 <= 3
```

Now we found a valid pair.

The **latest occurrence is always the closest previous occurrence**, so that's the only index we need.

---

# Code

```
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d={}
        for i in range (len(nums)):
            if nums[i] in d and i-d[nums[i]]<=k:
                return True
            else:
                d[nums[i]]=i
        return False
```

### Code in simple words

```
d= {}
```

Create dictionary.

```
foriinrange(len(nums)):
```

Go through every index.

```
ifnums[i]ind
```

Have we seen this number before?

If yes:

```
i-d[nums[i]]<=k
```

Check whether the previous occurrence is close enough.

If yes:

```
returnTrue
```

We found the answer.

Otherwise:

```
d[nums[i]]=i
```

Update the number's **latest index**.

If we finish the entire array without finding a pair:

```
returnFalse
```

---

# Complexity

### Time Complexity: `O(n)`

We go through the array once.

Dictionary lookup and insertion are **O(1)** on average.

Therefore:

```
O(n)
```

### Space Complexity: `O(n)`

In the worst case, every number is different:

```
[1, 2, 3, 4, 5, 6, ...]
```

The dictionary could contain `n` elements.

Therefore:

```
O(n)
```

### Final answer

```
Time:  O(n)
Space: O(n)
```

**Core idea to remember:**

> **Store the latest index of each number. When you see the same number again, check whether the distance from its latest index is `<= k`.**
>
