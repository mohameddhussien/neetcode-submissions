class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum, minSum = nums[0], nums[0]
        total, curMax, curMin = 0, 0, 0

        for num in nums:
            curMax = max(curMax, 0) + num
            curMin = min(curMin, 0) + num
            total += num
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)

        return max(maxSum, total - minSum) if maxSum > 0 else maxSum