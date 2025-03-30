from typing import List


def remove_duplicates(nums: List[int]) -> int:
    if len(nums) <= 1:
        return len(nums)

    left: int = 0

    for right in range(1, len(nums)):
        if nums[left] == nums[right]:
            continue
        left += 1
        nums[left] = nums[right]

    return left + 1


assert remove_duplicates([1, 1, 2]) == 2
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
