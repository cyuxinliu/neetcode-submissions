class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        ATTEMPT 1
        # go through the list, o(n)
        # have 2 pointers
        # first point is the current index, second 
        # pointer is seeing if it is equal of not
        # first loop for first pointer, loop through each item

        # any diff simply using the list name
        for n in range(len(nums)):
            if n != len(nums) - 1:
                for j in range(n + 1, len(nums)):
                    if nums[j] == nums[n]: return True

        return False    
        """

        seen = set()

        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False        

        
        