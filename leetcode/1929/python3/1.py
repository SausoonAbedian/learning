from typing import List


def get_concatenation(nums: List[int]) -> List[int]:
    res = [0] * (len(nums) * 2)
    for i in range(0, len(nums)):
        res[i] = nums[i]
        res[i + len(nums)] = nums[i]
    return res


assert get_concatenation([1, 2, 1]) == [1, 2, 1, 1, 2, 1]
assert get_concatenation([1, 3, 2, 1]) == [1, 3, 2, 1, 1, 3, 2, 1]
