## 1. Nested lists

This code doesn't work as expected because of how Python handles list multiplication and references:

- `row = ['']*3` creates a single list `['', '', '']`.
- `field = [row]*3` creates a list of three references to the **same** `row` list, not three independent copies.
- Modifying `field[0][0] = 'X'` changes the first element of every row, because all rows reference the same list.
- As a result, `field` becomes `[["X", "", ""], ["X", "", ""], ["X", "", ""]]`, which does **not** match the `expected` list.

To fix it, you need to create independent copies of each row, e.g.:  
```python
field = [row.copy() for _ in range(3)]
```

## 2. All operator

This code behaves in a way that can be surprising because of how Python's built-in `all()` function works. Key points:

- `all(iterable)` returns **True if all elements of the iterable are truthy**, or if the iterable is empty.  
- `all([])` → True, because the iterable is empty.  
- `all([[]])` → False, because the single element is an empty list, which is falsy.  
- `all([[[]]])` → True, because the single element is a non-empty list (even if it contains an empty list), which is truthy.  

The subtlety is that `all()` checks the **truthiness of the elements**, not their type or length, and an empty iterable is considered trivially true.

## 3. Rounding error

This code doesn't behave as some might expect because of how Python's `round()` function works. Python uses "bankers' rounding" (round half to even):

- `round(1.5)` → 2  (because 2 is even)  
- `round(2.5)` → 2  (because 2 is even)  

So the assertion `round(1.5) == round(2.5)` is actually **True**, not False. If you expected traditional rounding (always rounding .5 up), this can be surprising.


## 4. Needle in a haystack

This line of code:
```python
x, y = (0, 1) if True else None, None
```

Actually means this line of code:
```python
x, y = (0, 1) if True else None, None
```

Similar to:
```python
>> a = 5, 6
>> a
(5, 6)
```

## 5. Key type conversion

This code doesn't work as you might expect because of how Python handles dictionary keys:

- In Python, dictionary keys must be **hashable**, and `1`, `True`, and `1.0` are considered equal when used as keys (`1 == True == 1.0`).
- Adding them to the dictionary overwrites the previous value for that key:
  ```python
  d = {1: 'a', True: 'b', 1.0: 'c'}
  # Only one key exists (1), with the last value 'c'

## 6. Mutating the immutable

This example highlights the subtle difference between **immutable tuples** and **mutable objects inside them**:

1. `some_tuple = ("A", "tuple", "with", "values")` creates a tuple of strings. Both the tuple and strings are immutable.  
   - Attempting `some_tuple[2] = "change this"` raises a `TypeError` because tuple elements cannot be reassigned.

2. `another_tuple = ([1, 2], [3, 4], [5, 6])` creates a tuple containing **lists**, which are mutable objects.  
   - `another_tuple[1].append(9)` works because it **modifies the list in-place**, without reassigning the tuple element.

3. `another_tuple[2] += [99, 999]` looks like it modifies the list, but Python interprets it as:  
```python
   another_tuple[2] = another_tuple[2] + [99, 999]
```
This is reassigning a tuple element, which is not allowed, so it raises a TypeError, however the list inside the tuple still mutates.