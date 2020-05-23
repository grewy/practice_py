def subsets_bitmap(arr):
    n = len(arr)
    ans = []

    for i in range(2**n, 2**(n+1)):
        bitmask = bin(i)[3:]
        ans.append([arr[j] for j in range(n) if bitmask[j] == '1'])
    return ans

def subsets(arr):
    ans = [[]]
    for ch in arr:
        ans += [cur + [ch] for cur in ans]
    return ans


def subsetsWithDup(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for ch in sorted(nums):
         ans += [cur + [ch] for cur in ans if cur + [ch] not in ans]
        return ans

def subsetsWithDup_1(nums):
        """
        Add if not added already - previous element is not same.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res

#print subsets([1,3,5])
#print subsets_bitmap([1,3,5])
print subsetsWithDup([4,4,4,1,4])
