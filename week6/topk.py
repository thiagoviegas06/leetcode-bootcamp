class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        count = {}
        frequency = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n,0)
        for n, c in count.items():
            frequency[c].append(n)

        res = []
        for i in range(len(frequency) - 1, -1, -1):
            for n in frequency[i]:
                res.append(n)
                if len(res) == k:
                    return res
        