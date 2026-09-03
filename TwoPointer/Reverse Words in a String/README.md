# **Reverse Words in a String**

## 1. Problem Statement

Given a string `s` containing words separated by spaces, **reverse the order of the words**.

You should:

- Remove extra spaces.
- Keep each word unchanged.
- Return the words in reverse order.
- Use only **one space** between words.

### Example

**Input:**

```
"the sky is blue"
```

**Output:**

```
"blue is sky the"
```

Another example:

**Input:**

```
"  hello   world  "
```

**Output:**

```
"world hello"
```

---

## 2. Logic to Solve

We can solve it in **3 simple steps**:

### Step 1: Split the string

```
words=s.split()
```

For:

```
"  hello   world  "
```

we get:

```
["hello","world"]
```

`split()` automatically removes extra spaces.

### Step 2: Reverse the words

```
words.reverse()
```

Now:

```
["world","hello"]
```

### Step 3: Join the words

```
" ".join(words)
```

This gives:

```
"world hello"
```

---

## 3. Code

```
class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        words.reverse()
        return " ".join(words)
```

## 4. Complexity

Let `n` = length of the input string.

### Time Complexity: `O(n)`

- `split()` → `O(n)`
- `reverse()` → `O(n)` in the worst case
- `join()` → `O(n)`

Overall:

```
Time = O(n)
```

### Space Complexity: `O(n)`

We store the words in a list and create the result string.

```
Space = O(n)
```

### Final

```
Time Complexity  : O(n)
Space Complexity : O(n)
```

**This is an efficient and clean solution.**
