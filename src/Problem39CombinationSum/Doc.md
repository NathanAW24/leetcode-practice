# Thought Process
It want all unique combinations, so it has to go through the combination of the values repeatedly, each time we add a number we append it to `result` array. If it `sum` reaches `7`, it will stop and append `result` to an array of `results`. If it exceeds 7, it will also stop but `result` wont be appended to `results`.

For example 1
```python
candidates = [2, 3, 6, 7]
target = 7
print(Solution().combinationSum(candidates, target))
```

Mermaid graph will be `(<candidate-number>, <current-sum-after-adding-current-candidate-number>)`.
- `<current-sum> = <previous-sum> + <current-candidate-number>`
- `<previous-sum>` inclues the `<previous-candidate-number>` already
```mermaid
  graph TD;
    nil,0 --> 2,2
    nil,0 --> 3,3
    nil,0 --> 6,6
    nil,0 --> 7,7

    2,2-->2,4;
    2,2-->3,5;
    2,2-->6,8,STOP
    2,2-->7,9,STOP

    2,4-->2,6
    2,4-->3,7,YES
    2,4-->6,10,STOP
    2,4-->7,11,STOP

    2,6-->2,8,STOP
    2,6-->3,9,STOP
    2,6-->6,12,STOP
    2,6-->7,13,STOP


    3,5-->2,7,YES
    3,5-->3,8,STOP
    3,5-->6,11,STOP
    3,5-->7,12,STOP
```
This mermaid graph shows a partial condition of what happens, but the key is to add every value of the array for every iteration until it leads to `7` or greater.