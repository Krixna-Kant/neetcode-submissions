class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        HashMap = defaultdict(int)

        for n in nums:
            HashMap[n] += 1

        sorted_item = sorted(HashMap.items(), key = lambda item:item[1], reverse=True)
        top_k_item = sorted_item[:k]

        return [item[0] for item in top_k_item]
        