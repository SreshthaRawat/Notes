# brute

""" 
so before all that we doing that k modulus thingy because if the rotation(k) is graeter
than the length then the prog will throw out of index error

now here we create a temp list, where we'll copy first k elements into the temp list

now after that we'll shift the ele by k towards left

 """


class Solution:
    # Function to rotate the array to the left by k positions
    def rotateArray(self, nums, k):
        n = len(nums)  # Size of array
        k = k % n  # To avoid unnecessary rotations

        temp = []

        # Store first k elements in a temporary array
        for i in range(k):
            temp.append(nums[i])

        # Shift n-k elements of given array to the front
        for i in range(k, n):
            nums[i - k] = nums[i]

        # Copy back the k elements at the end
        for i in range(k):
            nums[n - k + i] = temp[i]

# optimal

class Solution:
    # Function to reverse the array between start and end
    def reverseArray(self, nums, start, end):
        while start < end:
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start += 1
            end -= 1

    # Function to rotate the array to the left by k positions
    def rotateArray(self, nums, k):
        n = len(nums)  # Size of array
        k = k % n  # To avoid unnecessary rotations
        
        # Reverse the first k elements
        self.reverseArray(nums, 0, k - 1)

        # Reverse the last n-k elements
        self.reverseArray(nums, k, n - 1)

        # Reverse the entire array
        self.reverseArray(nums, 0, n - 1)