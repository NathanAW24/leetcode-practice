# Scribbles
## Scribble 1
```
1 -> 2 -> 3 -> 4 -> 5
^
n1
```
`n = 0`
Can go until the end

`(1).next => (2)` &rarr; n = 0 + 1 = 1
    `(2).next => (3)` &rarr; n = 1 + 1 = 2
        `(3).next => (4)` &rarr; n = 2 + 1 = 3
            `(4).next => (5)` &rarr; n = 3 + 1 = 4
                `(5).next => (None)` &rarr; n = 4 + 1 = 5

I got the `n` already &rarr; `maxIndex = n-1`.
Two pointers `nodeL` and `nodeR`.`

`nodeL` just moves accordingly but how about `nodeR`?

Everytime we finish an operation of moving for 1 `<start-end>` pair, we add `c += 1`, then starting from `nodeL` do `.next` sebanyak `2*c-1` times, that's the value of `nodeR` we want.

Then with these two nodes, we want to do, in this order
- `nodeR.next = nodeL.next` point 5 -> 2
- `nodeL.next = nodeR` point 1 -> 5
- `nodeL = nodeL.next.next` move `nodeL` from 1 to 5 to 2