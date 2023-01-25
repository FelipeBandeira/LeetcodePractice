class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        RUNTIME: beats 40%
        MEMORY: beats 10%
        """

        for num1 in range(len(nums)):
            for num2 in range(num1+1, len(nums)):
                if nums[num1] + nums[num2] == target:
                    return [num1, num2]