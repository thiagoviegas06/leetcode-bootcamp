class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = [1]
        post = 1
        pre  = 1

        for i in range(1, len(nums)):
            pre = pre*nums[i-1]
            output.append(pre)

        for i in range(len(nums)-2, -1, -1):
            post = post * nums[i+1]
            output[i] = output[i] * post
            
        return output

   