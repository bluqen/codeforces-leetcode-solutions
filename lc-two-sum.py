class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        l = []
        for i in enumerate(nums):
            for _ in enumerate(nums):
                if _[0] == i[0]:
                    continue
                if _[1] + i[1] == target:
                    return [i[0], _[0]]
                    break