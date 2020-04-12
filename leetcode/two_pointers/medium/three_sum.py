class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums:
            return res

        nums.sort()
        if nums[0] > 0:
            return res

        for idx in xrange(len(nums)-2):

            if idx > 0 and nums[idx] == nums[idx-1]:
                continue
            i, j = idx+1, len(nums)-1
            #[-4,-1,-1,0,1,2]
            while i < j:
                sm = nums[idx] + nums[i] + nums[j]

                if sm == 0:
                    res.append([nums[idx], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i+1]:
                        i += 1
                    while i < j and nums[j] == nums[j-1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif sm > 0:
                    j -= 1
                else:
                    i += 1

        return res
