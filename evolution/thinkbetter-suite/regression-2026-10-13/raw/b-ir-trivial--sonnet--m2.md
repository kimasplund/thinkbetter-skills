The main difference is that a list is mutable and a tuple is immutable.

```python
nums = [1, 2, 3]
nums[0] = 99          # fine
nums.append(4)        # fine

point = (1, 2, 3)
point[0] = 99         # TypeError: 'tuple' object does not support item assignment
```

**Lists**
- Written with square brackets: `[1, 2, 3]`
- You can add, remove, and change items after creating them.
- Meant for collections that grow or change, usually of the same kind of thing (for example, a list of filenames).
- Not hashable, so they can't be dictionary keys or set members.

**Tuples**
- Written with parentheses: `(1, 2, 3)`. A single-item tuple needs a trailing comma: `(1,)`.
- Fixed once created.
- Meant for a fixed group of values that belong together, often of different kinds (for example, `(name, age, city)` or `(x, y)` coordinates).
- Hashable if all their items are hashable, so they can be dictionary keys or set members.
- Slightly smaller in memory and a bit faster to create.

One caveat: a tuple is immutable, but it can contain mutable objects. In `([1, 2], 3)`, you can still change the inner list. The tuple just can't be made to point at a different object.

Rule of thumb: use a list when the contents will change, and a tuple when they are a fixed record.
