class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        ans = []

        for num in nums:
            freq[num] += 1
        
        for i in range(k):
            max_key = max(freq, key=freq.get)
            ans.append(max_key)
            del freq[max_key]
        
        return ans
