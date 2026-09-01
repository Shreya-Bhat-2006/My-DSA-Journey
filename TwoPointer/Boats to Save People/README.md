## 🚤 Problem: Boats to Save People

### Problem Statement

You are given an array `people`, where `people[i]` represents the weight of the `i`-th person.

You are also given an integer `limit`, which is the **maximum weight a boat can carry**.

Each boat can carry **at most 2 people**.

Find the **minimum number of boats** required to rescue everyone.

---

### Example 1

```
Input:
people = [1, 2]
limit = 3

Output:
1
```

Because:

```
[1, 2] → weight = 3
```

One boat is enough.

---

### Example 2

```
Input:
people = [3, 2, 2, 1]
limit = 3

Output:
3
```

Possible arrangement:

```
[1, 2]
[2]
[3]
```

So we need **3 boats**.

---

### Example 3

```
Input:
people = [3, 5, 3, 4]
limit = 5

Output:
4
```

No two people can be paired without exceeding the limit, so everyone needs their own boat.

---

# 🧠 Logic to Solve

### Step 1: Sort the people

Sort the weights from smallest to largest.

This allows us to use two pointers:

- `l` → lightest person
- `r` → heaviest person

### Step 2: Focus on the heaviest person

The heaviest person **must get into a boat**.

Try to pair them with the lightest person.

### Step 3: Check if they can share

If:

```
lightest + heaviest <= limit
```

then put them together.

Move both pointers.

Otherwise, the heaviest person must go alone.

Move only the `r` pointer.

### Step 4: Count the boat

Every time we handle the heaviest person, **one boat is used**.

Continue until all people are handled.

# Code

```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l=0
        r=len(people)-1
        count=0
        while l<=r:
            if people[l]+people[r]<=limit:
               l+=1
            r-=1
            count+=1
       
        
        return count
```

### Key Insight ⭐

> **Always handle the heaviest person first. Try to pair them with the lightest person.**
> 

If even the lightest person cannot fit with the heaviest, then **nobody else can fit either**, so the heaviest person must go alone.

## Complexity

- **Time:** `O(n log n)` — sorting
- **Space:** `O(1)` extra space
