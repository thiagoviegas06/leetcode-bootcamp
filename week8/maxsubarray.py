class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #find maximum subarray ending at i
        #maximum subarray that ends at i is either nums[i] or maxsubarray[i-1] + nums[i]

        maxsubarray = [nums[0]]
        curMax = maxsubarray[0]

        for i in range(1, len(nums)):
            current = nums[i]
            prev = maxsubarray[i-1]
            curSum = current + prev
            if(curSum > current):
                current = curSum
            if(current > curMax):
                curMax = current

            maxsubarray.append(current)

        return curMax
