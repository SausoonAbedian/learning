from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [0] * (2 * n)
    for i, num in enumerate(nums):
        ans[i] = ans[i + n] = num
    return ans


assert get_concatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
assert get_concatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
