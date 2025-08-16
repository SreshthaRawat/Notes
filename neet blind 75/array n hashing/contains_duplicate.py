#brute force
# not much to add just plain brute force
# with n2 TC so typical TLE error 

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
#sort approach
# we first sort there
