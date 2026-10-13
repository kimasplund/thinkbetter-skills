The main difference is mutability.

**List** (`[1, 2, 3]`) is mutable. You can add, remove, or replace items after creating it:

```python
nums = [1, 2, 3]
nums.append(4)     # [1, 2, 3, 4]
nums[0] = 10       # [10, 2, 3, 4]
```

**Tuple** (`(1, 2, 3)`) is immutable. Once created, its contents cannot change:

```python
point = (1, 2, 3)
point[0] = 10      # TypeError: 'tuple' object does not support item assignment
```

Practical consequences:

- **Hashability:** a tuple whose items are hashable can be a dict key or a set member. A list cannot.
- **Memory and speed:** tuples are slightly smaller and slightly faster to create and iterate over.
- **Intent:** tuples suit fixed collections, such as a coordinate pair or a database row, where position carries meaning. Lists suit collections of items of one kind that grow or shrink.

A one-item tuple needs a trailing comma: `(5,)`. Without it, `(5)` is just the integer 5.
