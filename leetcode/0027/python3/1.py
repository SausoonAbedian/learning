from typing import List


def remove_element(nums: List[int], val: int) -> int:
    if len(nums) == 0:
        return 0
    idx = 0
    for i in range(0, len(nums)):
        if nums[i] == val:
            continue
        nums[idx] = nums[i]
        idx += 1
    return idx


assert remove_element([3, 2, 2, 3], 3) == 2
assert remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
