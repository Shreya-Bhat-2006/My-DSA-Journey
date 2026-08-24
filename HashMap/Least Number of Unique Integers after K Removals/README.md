# Least Number of Unique Integers after K Removals

## 1. Problem Statement

You are given:

- An integer array `arr`
- An integer `k`

You have to **remove exactly `k` elements** from the array.

After removing them, return the **minimum possible number of unique integers** remaining.

### What does "unique integer" mean?

A unique integer means a **different value**, regardless of how many times it appears.

For example:

```
arr = [4, 3, 1, 1, 3, 3, 2]
```

The different values are:

```
4, 3, 1, 2
```

So there are:

```
4 unique integers
```

---

# 2. Example

### Example 1

```
arr = [5, 5, 4]
k = 1
```

Frequencies:

```
5 → 2
4 → 1
```

We can remove only 1 element.

If we remove `4`:

```
[5, 5]
```

Now only:

```
5
```

is left.

So the answer is:

```
1
```

---

### Example 2

```
arr = [4,3,1,1,3,3,2]
k = 3
```

Frequency:

```
4 → 1
3 → 3
1 → 2
2 → 1
```

Initially:

```
Unique = 4
k = 3
```

We want to reduce the number of unique values.

So remove the values with the **smallest frequency first**.

```
4 → 1
2 → 1
1 → 2
3 → 3
```

Remove `4`:

```
k = 3 - 1 = 2
unique = 3
```

Remove `2`:

```
k = 2 - 1 = 1
unique = 2
```

Now `1` occurs 2 times, but we only have 1 removal left.

We cannot completely remove `1`.

So final unique values are:

```
1, 3
```

Answer:

```
2
```

---

# 3. Logic to Solve

The most important observation is:

> **We should completely remove a number whenever possible.**
> 

Suppose:

```
A → 1 occurrence
B → 3 occurrences
C → 5 occurrences
```

If we have `k = 1`:

Removing `A` costs only 1 removal and completely eliminates one unique number.

But removing one `B` doesn't eliminate `B`.

Therefore:

> **Remove the least frequent numbers first.**
> 

### General steps

```
1. Count the frequency of every number.
             ↓
2. Process frequencies from smallest to largest.
             ↓
3. If we have enough k:
       completely remove that number
       decrease k
       decrease unique count
             ↓
4. If we don't have enough k:
       stop
             ↓
5. Return the remaining unique count.
```

---

# 4. Method 1 — Sorting

We first count frequencies:

```
d= {}foriinarr:d[i]=d.get(i,0)+1
```

Then:

```
c=sorted(d,key=d.get)
```

This sorts the **numbers according to their frequency**.

For:

```
4 → 1
3 → 3
1 → 2
2 → 1
```

we get:

```
c = [4, 2, 1, 3]
```

Then remove them from smallest frequency to largest.

### Code

```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}

        # Count frequency
        for i in arr:
            d[i] = d.get(i, 0) + 1

        # Sort numbers by frequency
        c = sorted(d, key=d.get)

        # Remove least frequent numbers first
        for i in c:
            if d[i] <= k:
                k -= d[i]
                del d[i]
            else:
                break

        return len(d)
```

### Complexity

Let:

```
n = length of arr
m = number of unique elements
```

Frequency counting:

```
O(n)
```

Sorting:

```
O(m log m)
```

Loop:

```
O(m)
```

Therefore:

```
Time  = O(n + m log m)
      = O(n log n)    (worst case)

Space = O(m)
      = O(n)          (worst case)
```

---

# 5. Method 2 — Bucket Sort

We can make it more efficient.

The problem with Method 1 is:

```
sorted(d,key=d.get)
```

Sorting takes `O(n log n)`.

But frequency can only be between:

```
1 and n
```

So instead of sorting, we can create **frequency buckets**.

For:

```
4 → 1
2 → 1
1 → 2
3 → 3
```

we create:

```
bucket[1] = [4, 2]
bucket[2] = [1]
bucket[3] = [3]
```

Now we naturally process:

```
frequency 1
     ↓
frequency 2
     ↓
frequency 3
```

No sorting required.

### Code

```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d = {}

        # Count frequency
        for i in arr:
            d[i] = d.get(i, 0) + 1

        # Create frequency buckets
        buckets = [[] for _ in range(len(arr) + 1)]

        for num, freq in d.items():
            buckets[freq].append(num)

        unique = len(d)

        # Process smallest frequencies first
        for freq in range(1, len(arr) + 1):

            for num in buckets[freq]:

                if freq <= k:
                    k -= freq
                    unique -= 1
                else:
                    return unique

        return unique
```

### Example

For:

```
arr = [4,3,1,1,3,3,2]
k = 3
```

Buckets:

```
bucket[1] = [4, 2]
bucket[2] = [1]
bucket[3] = [3]
```

Process:

```
freq = 1
```

Remove `4`:

```
k = 2
unique = 3
```

Remove `2`:

```
k = 1
unique = 2
```

Next:

```
freq = 2
```

But:

```
2 > k
2 > 1
```

So we can't completely remove that number.

Answer:

```
2
```

---

# 6. Complexity Comparison

| Method | Time | Space |
| --- | --- | --- |
| **Sorting** | `O(n log n)` | `O(n)` |
| **Bucket Sort** | **`O(n)`** | `O(n)` |
