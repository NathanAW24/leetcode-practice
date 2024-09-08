# TIL
## TIL 1: Declaring `defaultdict(...)`
The argument inside `defaultdict(...)` has to be a function, so you can't do `defaultdict(0)`, but have to be `defaultdict(lambda: 0)`.

