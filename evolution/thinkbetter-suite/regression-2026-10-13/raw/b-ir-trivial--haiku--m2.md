The main difference is mutability: a list can be changed after it is created, and a tuple cannot.

| | list | tuple |
|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | Yes: append, remove, and assign items | No: fixed once created |
| Hashable (usable as a dict key or set member) | No | Yes, if all its items are hashable |
| Memory and speed | Slightly larger and slower | Slightly smaller and faster |

```python
nums = [1, 2, 3]
nums.append(4)      # fine

point = (3, 4)
point[0] = 5        # TypeError: 'tuple' object does not support item assignment

grid = {(0, 0): "start"}   # tuples work as keys
# {[0, 0]: "start"}        # TypeError: unhashable type: 'list'
```

As a rule of thumb, use a list for a collection of items that grows, shrinks, or gets reordered, such as a queue of tasks. Use a tuple for a fixed group of values whose meaning depends on position, such as an `(x, y)` coordinate or a row from a database, and for multiple return values.
