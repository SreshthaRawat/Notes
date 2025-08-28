class Solution:
    def moveZeroes(self, nums):
        # j points to the position where next non-zero should go
        j = 0

        # Loop through each element in the array
        for i in range(len(nums)):
            # If current element is non-zero
            if nums[i] != 0:
                # Swap with the element at index j
                nums[i], nums[j] = nums[j], nums[i]

                # Move j forward
                j += 1

# Driver code
if __name__ == "__main__":
    # Input array
    arr = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]

    # Create Solution instance and move zeroes
    sol = Solution()
    sol.moveZeroes(arr)

    # Print updated array
    print(" ".join(map(str, arr)))
