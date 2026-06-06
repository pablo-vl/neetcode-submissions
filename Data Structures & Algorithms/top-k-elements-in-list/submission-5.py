class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        top_k = sorted(list(count.values()))[-k:]

        return [k for k, v in count.items() if v in top_k]
        