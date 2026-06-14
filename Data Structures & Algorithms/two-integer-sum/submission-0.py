class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        two pointer
        lh and rh
        lh starts at the first index
        rh goes and gets added. if it equals target return true
        doesnt, then move lh up
        """

        indices = []

        for rh in range(len(nums)):
            for lh in range(rh+1, len(nums)):
                if nums[rh] + nums[lh] == target: 
                    indices.append(rh)  
                    indices.append(lh)
                       

        return indices 