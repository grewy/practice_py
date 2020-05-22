def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        p1 = nums[0]
        p2 = slow

        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]

        return p1

print findDuplicate([1,3,3,4,5,6,2])
