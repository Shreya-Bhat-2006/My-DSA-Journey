# **Insert Delete GetRandom O(1)**

## 1. Problem Statement

Implement the `RandomizedSet` class with the following operations:

- `insert(val)` — Insert `val` if it is not already present. Return `True` if inserted, otherwise `False`.
- `remove(val)` — Remove `val` if it exists. Return `True` if removed, otherwise `False`.
- `getRandom()` — Return a random element from the set. Every element must have an **equal probability** of being selected.

Each operation should work in **average `O(1)` time**.

---

## 2. Example

### Input

```
["RandomizedSet", "insert", "remove", "insert",
 "getRandom", "remove", "insert", "getRandom"]

[[], [1], [2], [2], [], [1], [2], []]
```

### Output

```
[null, true, false, true, 2, true, false, 2]
```

### Explanation

```
RandomizedSet()
```

Initially:

```
{}
```

### `insert(1)`

`1` doesn't exist, so insert it.

```
{1}
```

Returns:

```
True
```

### `remove(2)`

`2` doesn't exist.

Returns:

```
False
```

### `insert(2)`

`2` doesn't exist, so insert it.

```
{1, 2}
```

Returns:

```
True
```

### `getRandom()`

There are two elements:

```
1, 2
```

It can return either `1` or `2`.

### `remove(1)`

Remove `1`.

```
{2}
```

Returns:

```
True
```

### `insert(2)`

`2` already exists.

Returns:

```
False
```

### `getRandom()`

Only `2` remains, so it must return:

```
2
```

---

# 3. Logic to Solve

We need **two data structures**:

### 1. List

```
self.l= []
```

The list stores the actual values.

For example:

```
l = [10, 20, 30]
```

We use it because `random.choice()` can select an element randomly in `O(1)`.

---

### 2. Dictionary

```
self.d= {}
```

The dictionary stores:

```
value → index
```

For example:

```
l = [10, 20, 30]

d = {
    10: 0,
    20: 1,
    30: 2
}
```

This lets us find the position of a value in `O(1)`.

---

## `insert(val)`

Check whether `val` already exists.

```
ifvalinself.d:returnFalse
```

Otherwise:

```
self.l.append(val)self.d[val]=len(self.l)-1
```

Return `True`.

---

## `remove(val)`

This is the most important part.

Suppose:

```
l = [10, 20, 30, 40]
```

We want to remove `20`.

We don't want to use:

```
self.l.remove(20)
```

because that can take `O(n)`.

Instead:

### Step 1 — Find the index

```
index=self.d[val]
```

For `20`:

```
index = 1
```

### Step 2 — Get the last element

```
last=self.l[-1]
```

```
last = 40
```

### Step 3 — Replace `20` with `40`

```
Before:

[10, 20, 30, 40]

After:

[10, 40, 30, 40]
```

### Step 4 — Remove the last element

```
self.l.pop()
```

Now:

```
[10, 40, 30]
```

### Step 5 — Update the dictionary

`40` moved from index `3` to index `1`:

```
self.d[40]=1
```

Finally remove `20`:

```
delself.d[20]
```

This makes removal `O(1)`.

---

## `getRandom()`

Because all values are stored in the list:

```
random.choice(self.l)
```

returns a random element with equal probability.

---

# 4. Code

```
import random
class RandomizedSet:

    def __init__(self):
        self.d={}
        self.l=[]

    def insert(self, val: int) -> bool:
        if val in self.d:
           return False
        
        self.l.append(val)
        self.d[val]=len(self.l)-1
        return True
    
        
           
        

    def remove(self, val: int) -> bool:
        if val in  self.d:
            index=self.d[val]
            last=self.l[-1]
            self.l[index]=last
            self.l.pop()
            self.d[last]=index
            del(self.d[val])
            return True

          
        
        return False
        

    def getRandom(self) -> int:
        
        return random.choice(self.l)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```

# 5. Complexity

| Operation | Time |
| --- | --- |
| `insert()` | **O(1) average** |
| `remove()` | **O(1) average** |
| `getRandom()` | **O(1)** |

### Space Complexity

We store every element in both the list and dictionary:

```
O(n)
```

### Final idea to remember

```
Dictionary → tells us WHERE the value is
List       → stores values and gives random access
```

The combination of:

```
HashMap + Array
```
