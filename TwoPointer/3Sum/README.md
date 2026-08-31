## 3Sum

### 📌 Problem

Given an integer array `nums`, find **all unique triplets** `[nums[i], nums[j], nums[k]]` such that:

- `i`, `j`, and `k` are different indices.
- `nums[i] + nums[j] + nums[k] = 0`.
- The answer must not contain duplicate triplets.

**Example:**

```
Input:
[-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2], [-1, 0, 1]]
```

---

# 💡 Logic / Idea to Solve

### Step 1: Sort the array

Sort the array first.

Example:

```
[-1, 0, 1, 2, -1, -4]

        ↓

[-4, -1, -1, 0, 1, 2]
```

Sorting helps us:

- Use the **two-pointer technique**.
- Easily identify and skip duplicates.

---

### Step 2: Fix one element

Take each element as the **first number** of the triplet.

For every `i`, we now need to find **two numbers** after `i` whose sum is:

```
0 - nums[i]
```

For example, if the fixed number is `-1`:

```
-1 + x + y = 0

Therefore:

x + y = 1
```

---

### Step 3: Use two pointers

After fixing `i`:

- Put `left` immediately after `i`.
- Put `right` at the end of the array.

Then calculate the sum of the three numbers.

#### If the sum is less than 0:

We need a **larger value**, so move `left` to the right.

#### If the sum is greater than 0:

We need a **smaller value**, so move `right` to the left.

#### If the sum is 0:

We found a valid triplet.

Add it to the result and move both pointers.

---

### Step 4: Avoid duplicate triplets

Because the array is sorted, duplicate values will be next to each other.

There are two places where duplicates need to be skipped:

**For `i`:**

If the current value is the same as the previous value, skip it.

**For `left` and `right`:**

After finding a valid triplet, skip any repeated values before continuing.

This ensures every triplet appears only once.

# Code

```
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s=sorted(nums)
      
        
        l=[]
        for i in range(len(s)-2):
            if i>0 and s[i]==s[i-1]:
                continue
            left=i+1
            right=len(s)-1
            while left<right:
                sum=s[i]+s[left]+s[right]
                if sum<0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    l.append([s[i],s[left],s[right]])
                    left+=1
                    right-=1
                    while left < right and s[left] == s[left - 1]:
                        left += 1

                    while left < right and s[right] == s[right + 1]:
                        right -= 1
                    
        return l

```

```
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        s=sorted(nums)
      
        
        l=[]
        for i in range(len(s)-2):
            if i>0 and s[i]==s[i-1]:
                continue
            left=i+1
            right=len(s)-1
            while left<right:
                sum=s[i]+s[left]+s[right]
                if sum<0:
                    left+=1
                elif sum>0:
                    right-=1
                else:
                    l.append([s[i],s[left],s[right]])
                    left+=1
                    right-=1
                    while left < right and s[left] == s[left - 1]:
                        left += 1

                    while left < right and s[right] == s[right + 1]:
                        right -= 1
                    
        return l

```

### Complexity

**Time:** `O(n²)`

- Sorting → `O(n log n)`
- Two-pointer search → `O(n²)`
- Overall → **O(n²)**

**Space:** `O(n)`
