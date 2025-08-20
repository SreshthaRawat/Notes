

# optimal
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen={}  #dictionary

        for i,val in enumerate(nums):  #enum for key pair iteration

            diff=target-val    #we'll search diff in seen dict
            if diff in seen:

                return [seen[diff],i]  
            """ so whats happening in return is that 
            we're returning two values 

            one is, seen[diff], let's call it "x" for now
            x returns the index of diff value in seen

            second value is, i, let's call it "y" for now
            y returns the current index we're on

            so return statement can be simplified as
            return [x,y] so it returns two values only

                  """
            
            seen[val]=i
