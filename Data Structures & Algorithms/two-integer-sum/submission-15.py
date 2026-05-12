class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in seen:
                return [seen.get(delta), i]
            seen.update({
                nums[i]: i
            })
