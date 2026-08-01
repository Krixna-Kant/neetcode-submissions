class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Brute Force Approach
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True
        # return False 

        #2nd Approach
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        #3rd Approach
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False 
        