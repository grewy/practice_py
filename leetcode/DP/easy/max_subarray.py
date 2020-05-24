def maxSubArray(numbers):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(numbers) == 1:
            return numbers[0]

        best_sum = -99999999
        #neg value to consider neg values in numbers
        current_sum = 0
        for x in numbers:
            current_sum = max(x, current_sum + x)
            best_sum = max(best_sum, current_sum)
        return best_sum
