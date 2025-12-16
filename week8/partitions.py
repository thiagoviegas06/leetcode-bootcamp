class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if(sum(nums) %2):
            return False

        partitions = set()
        partitions.add(0)
        target = sum(nums) // 2 

        for i in range(len(nums) -1, -1,-1):
            next_partition = set()
            for t in partitions:
                if(t + nums[i] == target):
                    return True

                next_partition.add(t + nums[i])
                next_partition.add(t)

            partitions = next_partition
        return True if target in partitions else False