The main difference is that a list is mutable and a tuple is immutable.

| | List | Tuple |
|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | Yes: you can add, remove, or change items | No: contents are fixed after creation |
| Hashable | No, so it can't be a dict key or set member | Yes, if all its items are hashable |
| Methods | Many (`append`, `remove`, `sort`, ...) | Only `count` and `index` |
| Memory and speed | Slightly more overhead | Slightly smaller and faster to create |

```python
nums = [1, 2, 3]
nums[0] = 99          # fine
nums.append(4)        # fine

point = (1, 2)
point[0] = 99         # TypeError: 'tuple' object does not support item assignment

locations = {(40.7, -74.0): "NYC"}   # tuple as a dict key works
# {[40.7, -74.0]: "NYC"}             # TypeError: unhashable type: 'list'
```

**When to use which**

- Use a list for a collection that grows, shrinks, or changes, and whose items are all the same kind of thing (a list of usernames, for example).
- Use a tuple for a fixed group of values where position has meaning, such as `(x, y)` coordinates, `(name, age)` records, or multiple return values from a function. Tuples also work well as dict keys.

One caveat is that a tuple is only shallowly immutable. If it holds a mutable object, such as a list, that inner object can still change:

```python
t = (1, [2, 3])
t[1].append(4)   # t is now (1, [2, 3, 4])
```
