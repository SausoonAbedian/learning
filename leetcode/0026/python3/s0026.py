from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0

    idx = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[idx]:
            idx += 1
            nums[idx] = nums[i]
    return idx + 1


assert remove_duplicates([1, 1, 2]) == 2
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
