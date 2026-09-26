# Problem: Number of Sub-arrays With Average Greater Than or Equal to Threshold

### Problem Statement

Given an integer array `arr` and two integers `k` and `threshold`, find the number of **contiguous subarrays of size `k`** whose average is **greater than or equal to `threshold`**.

Return the count.

### Example 1

```
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
```

The size-3 subarrays are:

```
[2,2,2] → average = 2      ❌
[2,2,2] → average = 2      ❌
[2,2,5] → average = 3      ❌
[2,5,5] → average = 4      ✅
[5,5,5] → average = 5      ✅
[5,5,8] → average = 6      ✅
```

Therefore:

```
Answer = 3
```

---

# 🧠 Main Logic

We need:

```
average >= threshold
```

Average is:

```
sum / k >= threshold
```

Multiply both sides by `k`:

```
sum >= k × threshold
```

So instead of calculating the average, we can simply check:

```
window_sum>=k*threshold
```

This also avoids unnecessary division.

---

# 🔴 Your First Approach

You initially came up with the idea of maintaining a `sub` list:

```
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        sub = []
        c = 0

        for i in arr:
            sub.append(i)

            if len(sub) == k:
                if sum(sub) // k >= threshold:
                    c += 1

                sub.remove(sub[0])

        return c
```

### How your approach works

You maintain a window:

```
[2,2,2]
```

Check it.

Then remove the first element:

```
[2,2]
```

Add the next element:

```
[2,2,5]
```

Check again.

So your **basic idea was already sliding window**. 👍

### The problem

Every time you do:

```
sum(sub)
```

Python goes through all `k` elements again.

For example:

```
[2,2,5]
 ↓ ↓ ↓
2 + 2 + 5
```

Then for the next window:

```
[2,5,5]
 ↓ ↓ ↓
2 + 5 + 5
```

You're repeatedly calculating sums of elements you've already processed.

Also:

```
sub.remove(sub[0])
```

removes the first element from a Python list, which can require shifting the remaining elements.

### Complexity of your approach

Because `sum(sub)` takes `O(k)` and you do it for approximately `O(n)` windows:

```
Time = O(n × k)
```

And the `sub` list stores `k` elements:

```
Space = O(k)
```

### Efficient O(n) solution

```
class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        target=k*threshold
        ws=sum(arr[:k])
        c=0
        if ws>=target:
            c+=1
        for i in range(k,len(arr)):
            ws+=arr[i]
            ws-=arr[i-k]
            if ws>=target:
               c+=1
        return c
        

```

# 🔍 How the Efficient Approach Works

Suppose:

```
arr = [2,2,2,2,5,5,5,8]
k = 3
```

First window:

```
[2,2,2]
```

Calculate its sum once:

```
ws = 6
```

Now move the window.

### Window 1

```
[2,2,2]
```

Sum:

```
6
```

---

### Move one position

Old window:

```
[2,2,2]
 ↑
remove this 2
```

New window:

```
[2,2,5]
       ↑
    add this 5
```

Instead of calculating:

```
2 + 2 + 5
```

again, do:

```
ws-=2ws+=5
```

So:

```
6 - 2 + 5 = 9
```

---

### Move again

```
[2,2,5]
   ↓
[2,5,5]
```

Remove:

```
2
```

Add:

```
5
```

So:

```
9 - 2 + 5 = 12
```

And so on.

---

# ⭐ Why Is This Better?

### Your approach

For every window:

```
Calculate all k elements again
```

```
Window 1 → k operations
Window 2 → k operations
Window 3 → k operations
...
```

Therefore:

```
O(n × k)
```

---

### Optimized approach

For every new window:

```
Remove ONE element
Add ONE element
```

So each window takes constant time:

```
O(1)
```

for approximately `n` windows.

Therefore:

```
O(n)
```

# 3. That's the major difference

Your code does:

```
Window
   ↓
sum ALL k elements
   ↓
check
   ↓
move window
   ↓
sum ALL k elements AGAIN
   ↓
check
```

Efficient code does:

```
First window
     ↓
sum k elements ONCE
     ↓
move window
     ↓
remove ONE old element
add ONE new element
     ↓
check
     ↓
move window
     ↓
remove ONE old element
add ONE new element
```
