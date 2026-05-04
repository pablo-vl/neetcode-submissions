class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) != len(nums) else False



        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
