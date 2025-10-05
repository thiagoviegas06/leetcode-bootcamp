class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while (l < r):
            current_sum = numbers[r] + numbers[l]
            if target == current_sum:
                break
            elif target < current_sum:
                r = r - 1
            else:
                l = l + 1
        return [l+1,r+1] 