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

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        n=len(nums)
        
        nums.sort()

        for i in range(1,n): #edge case of nums=[0] 

            if nums[i]==nums[i-1]:
                return True
        return False
    

# with o of n we have 2 approaches hashset and hashset length 

#hashset
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
# hashset length
# here the approach is if the length of nums in set is not equal to 
# length of nums then we return false because set doesnt contain duplicate 
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        return len(set(nums))!=len(nums)


        




