class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.maxSize = maxSize
        return

    def push(self, x: int) -> None:
        arr_size = len(self.arr)

        if arr_size < self.maxSize:
            self.arr.append(x)

        return

    def pop(self) -> int:
        arr_size = len(self.arr)
        if arr_size > 0:
            return self.arr.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        n = len(self.arr)

        d = n - k

        def increment_gt_k(d, popped=None):
            if d > 0:
                increment_gt_k(d-1, self.pop())
                if popped != None:
                    self.push(popped)
            elif d == 0:
                increment_lte_k(k)
                if popped != None:
                    self.push(popped)

        def increment_lte_k(n, popped=None):  # n <= k, if n == 0,
            # pop all increment all
            # base case if n = 0
            if n > 0:
                increment_lte_k(n-1, self.pop())
                if popped != None:
                    self.push(popped + val)
            elif n == 0:
                if popped != None:
                    self.push(popped + val)

        if n <= k:
            increment_lte_k(n)
        else:
            increment_gt_k(d)

    def __str__(self):
        return str(self.arr)


if __name__ == "__main__":
    stk = CustomStack(4)
    stk.push(2)
    stk.push(3)
    stk.push(4)
    stk.push(6)
    print(stk)
    stk.increment(3, 100)

    print(stk)
