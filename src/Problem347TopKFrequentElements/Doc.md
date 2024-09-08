# TIL
## TIL 1: Declaring `defaultdict(...)`
The argument inside `defaultdict(...)` has to be a function, so you can't do `defaultdict(0)`, but have to be `defaultdict(lambda: 0)`.

## TIL 2: Sorting Hash Keys based on Corresponding values
Using the line in 
```python
...
        return sorted(hash.keys(), key=lambda hash_key: hash[hash_key], reverse=True)[0:k]
...
```
We can sort `hash.keys()`, by calling the value `hash[hash_key]` is the value used to compare against each other.