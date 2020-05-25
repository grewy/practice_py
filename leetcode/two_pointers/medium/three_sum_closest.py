class Solution(object):
    def threeSumClosest(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num.sort()
        result = sum(num[:3])

        for i in range(len(num) - 2):

            if i > 0 and num[i] == num[i-1]:
                continue

            j, k = i+1, len(num) - 1
            while j < k:
                sm = num[i] + num[j] + num[k]
                if sm == target:
                    return sm

                if abs(sm - target) < abs(result - target):
                    result = sm

                if sm < target:
                    j += 1
                elif sm > target:
                    k -= 1

        return result

