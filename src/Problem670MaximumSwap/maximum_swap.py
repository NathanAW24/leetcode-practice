from typing import List


class Solution:
    def maximumSwap(self, num: int) -> int:

        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        def name(arr: List[str], left_ptr, right_ptr):
            if left_ptr == right_ptr:
                # nothing to swap, its already largest possible permutation of number order
                return

            max_digit = 0
            max_idx = 0
            arr_slice = arr[left_ptr:right_ptr+1]
            print(f'new arr sliced {arr_slice}')
            for idx, digit in enumerate(arr_slice):
                # find max digit and idx
                # max digit has to consider both cases
                # arr_slice[idx] is same as digit
                if arr_slice[0] < arr_slice[idx] and int(digit) >= max_digit:
                    # PRINSIP A: anchor dipindahin hanya jika
                    # PRINSIP B: angka belakang lebih ada beban kalo dipindah ke depan (result lebih gede)
                    # this ur condition earlier, int(digit) > max_digit
                    # this is wrong bcs --> ga lengkap
                    # (a)(i) arr_slice[0] < arr_slice[idx], needed for comparing the 'left pointer anchor' with the 'left pointer mover', TRUE if there is an element greater than the first anchor
                    # (a)(ii) in the case of 98368, when u go anchor at idx=1, then compare with the last element idx=4, u dw max_idx move to 4 also
                    # (a)(iii) more exp on (a) please
                    # (b)(i) You want to take the larget from the back
                    max_digit, max_idx = int(digit), idx

            print(f"max idx {max_idx}, max digit {max_digit}")
            max_idx += left_ptr  # fix positioning, since your pointer fks up in recursion

            if max_idx == left_ptr:
                name(arr, left_ptr + 1, right_ptr)
            else:  # max_idx != left_ptr, confirm max_idx > left_ptr bcs we sliding window
                swap(arr, left_ptr, max_idx)

        num_str = str(num)
        num_ls = list(num_str)

        name(num_ls, 0, len(num_ls) - 1)

        num_str = ''.join(num_ls)

        return int(num_str)


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSwap(1211))
    print(solution.maximumSwap(98368))
    print(solution.maximumSwap(1993))
