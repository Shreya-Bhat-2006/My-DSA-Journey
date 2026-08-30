# **Backspace String Compare**

# 1. Problem

### **Backspace String Compare — LeetCode 844**

Given two strings `s` and `t`, determine whether they are equal after applying all the backspaces (`#`).

---

# 2. Problem Statement

You are given two strings `s` and `t`.

The character `#` represents a **backspace**, which removes the character immediately before it.

If there is no character before `#`, it does nothing.

Return:

- `True` → if the final strings are equal.
- `False` → otherwise.

### Example 1

```
s = "ab#c"
t = "ad#c"
```

Process `s`:

```
ab#c
  ↑
# removes b

"ac"
```

Process `t`:

```
ad#c
  ↑
# removes d

"ac"
```

Therefore:

```
"ac" == "ac"

Output: True
```

### Example 2

```
s = "ab##"
t = "c#d#"
```

`s`:

```
a b # #
    ↓
a # #
  ↓
""
```

`t`:

```
c # d #
↓   ↓
""  ""
```

Both become empty strings.

```
Output: True
```

---

# 3. First Logic — Stack

### Idea

We can simulate the backspace operation using a **stack**.

For each character:

- Normal character → `append()` it to the stack.
- `#` → remove the last character using `pop()`.
- If the stack is empty, ignore `#`.

After processing both strings, compare the two stacks.

### Code

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def check(s):
            s1 = []

            for i in s:
                if i == "#":
                    if s1:
                        s1.pop()
                else:
                    s1.append(i)

            return s1

        return check(s) == check(t)
```

### Example

```
s = "ab#c"
```

Stack execution:

```
a → [a]
b → [a, b]
# → [a]
c → [a, c]
```

Final:

```
[a, c]
```

Similarly:

```
t = "ad#c"

a → [a]
d → [a, d]
# → [a]
c → [a, c]
```

Final:

```
[a, c]
```

Therefore:

```
True
```

### Complexity

Let:

- `n = len(s)`
- `m = len(t)`

**Time Complexity:**

```
O(n + m)
```

We visit every character once.

**Space Complexity:**

```
O(n + m)
```

because we create stacks for both strings.

---

# 4. Second Logic — Two Pointers ⭐

The stack solution is good, but we can make it **more space-efficient**.

Instead of creating another string/stack, we process the strings **from right to left**.

### Key idea

When we encounter:

```
#
```

it means:

> The next valid character to the left must be skipped.
> 

So we maintain a counter:

```
sk1
```

for pending backspaces in `s`.

And:

```
sk2
```

for pending backspaces in `t`.

---

### Code

```
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
       
        r1=len(s)-1
        r2=len(t)-1
        sk1=0
        sk2=0
        while r1>=0 or r2>=0:
            while r1>=0:
                if s[r1]=="#":
                    sk1+=1
                    r1-=1
                elif sk1>0:
                    sk1-=1
                    r1-=1
                else:
                    break

            while r2>=0:
                if t[r2]=="#":
                    sk2+=1
                    r2-=1
                elif sk2>0:
                    sk2-=1
                    r2-=1
                else:
                    break
            if r1>=0 and r2 >=0:
                if s[r1]!=t[r2]:
                    return False
            elif r1>=0 or r2>=0:
                return False
            r1-=1
            r2-=1
        return True

                    

```

# 5. How the Two-Pointer Logic Works

Take:

```
s = "ab#c"
t = "ad#c"
```

We start from the end:

```
s = a b # c
          ↑ r1

t = a d # c
          ↑ r2
```

### First

Both pointers see `c`.

```
s[r1] = c
t[r2] = c
```
