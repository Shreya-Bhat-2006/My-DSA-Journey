# **Longest Consecutive Sequence**

## 1. Problem Statement

You are given an **unsorted array of integers** `nums`.

Find the length of the **longest sequence of consecutive integers**.

The numbers in the sequence must increase by exactly `1`.

### Example

```
nums = [100, 4, 200, 1, 3, 2]
```

The consecutive sequence is:

```
1 → 2 → 3 → 4
```

So the answer is:

```
4
```

Another example:

```
nums = [1, 4, 3, 5, 7]
```

Consecutive sequences are:

```
1

3 → 4 → 5

7
```

The longest one is `3 → 4 → 5`.

**Answer = 3**

---

# 2. Logic to Solve

### Step 1: Convert the array into a set

```
s=set(nums)
```

Why?

Because we need to quickly check whether a number exists.

For example:

```
4ins
```

takes approximately **O(1)** time.

---

### Step 2: Find the beginning of a sequence

For every number `i`, check:

```
ifi-1notins:
```

Why?

If `i - 1` does **not** exist, then `i` must be the **starting number** of a consecutive sequence.

Example:

```
1 → 2 → 3 → 4
↑
```

For `1`:

```
0 does not exist
```

So `1` is the beginning.

But for `3`:

```
2 exists
```

So `3` is **not** the beginning.

This prevents us from unnecessarily checking:

```
1 → 2 → 3 → 4
2 → 3 → 4
3 → 4
4
```

We only check from `1`.

---

### Step 3: Count the consecutive numbers

Once we find the beginning:

```
count=1
```

Then keep checking:

```
whilei+countins:count+=1
```

Suppose:

```
i = 1
```

We check:

```
1 + 1 = 2  → exists ✅
1 + 2 = 3  → exists ✅
1 + 3 = 4  → exists ✅
1 + 4 = 5  → doesn't exist ❌
```

Therefore:

```
1 → 2 → 3 → 4
```

has length `4`.

---

### Step 4: Keep the maximum

```
ans=max(ans,count)
```

If we find a longer sequence, update `ans`.

---

# 3. Code

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0

        s = set(nums)

        for i in s:
            # i is the beginning of a sequence
            if i - 1 not in s:
                count = 1

                # Count consecutive numbers
                while i + count in s:
                    count += 1

                ans = max(ans, count)

        return ans
```

# 4. Complexity

### Time: `O(n)`

- Creating the set → `O(n)`
- Checking numbers → overall `O(n)`
- Set lookup → approximately `O(1)`

So overall:

**Time = O(n)**

### Space: `O(n)`

The set can contain up to `n` different numbers.

**Space = O(n)**
