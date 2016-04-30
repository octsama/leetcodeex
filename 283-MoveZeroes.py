class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zero_index = 0
        for n in range(len(nums)):
            if nums[n]:
                nums[n], nums[zero_index] = nums[zero_index], nums[n]
                zero_index += 1


test = Solution()
nums = [0,1,0,3,12]
test.moveZeroes(nums)

print(nums)
