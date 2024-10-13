# Thought Process
```
[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]

[4, 8]
```
res = []

newInterval = [4, 8]
[1, 2] --> no merge --> append [1, 2] --> res = [ [1,2] ]
newInterval is still [4, 8]



[3, 5] --> merge --> newInterval = [4, 8] --> append [4, 8] --> res = [ [1,2], [4,8] ]

[6, 7] --> merge --> newInterval = [4, 8] --> append