""" 
so the baasic idea here is that, we create a temp list in which we'll store non zero element
then we transfer that non zero element to nums
the in last loop from count to n we transfer zero at the end of the list
 """
# brute force

class Solution:
    # Function to move zeroes to the end
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)

        """Create a temporary array 
        to store non-zero elements"""
        temp = [0] * n
        count = 0

        # Copy non-zero elements to temp
        for i in range(n):
            if nums[i] != 0:
                temp[count] = nums[i]
                count += 1

        # Copy non-zero elements back to nums
        for i in range(count):
            nums[i] = temp[i]

        # Fill the rest with zeroes
        for i in range(count, n):
            nums[i] = 0

""" 

 """

# optimal 