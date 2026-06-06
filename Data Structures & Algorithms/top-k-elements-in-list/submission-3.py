class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        top_k = list(count.values())
        top_k_sorted = sorted(top_k)
        top_k_needed = top_k_sorted[-k:]

        print(top_k_sorted)

        return [k for k, v in count.items() if v in top_k_needed]
        