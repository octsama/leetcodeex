class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i in range(len(nums)):
            if(target - nums[i] in hash_map):
                return [hash_map[target - nums[i]], i]
            hash_map[nums[i]] = i

solution = Solution()
print(solution.twoSum([0,4,3,0],0))
