class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        s, e, tmp, curSum = 0, 0, 0, 0

        for i, n in enumerate(nums):
            if curSum < 0:
                curSum = 0
                tmp = i
            curSum += n
            if curSum > maxSum:
                maxSum = curSum
                s = tmp
                e = i
        return maxSum