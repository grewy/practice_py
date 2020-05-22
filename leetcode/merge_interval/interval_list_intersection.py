
def intervalIntersection(A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        i = j =0

        while i < len(A) and j < len(B):
            #get left/right points of possible overlap
            lt = max(A[i][0], B[j][0])
            rt = min(A[i][1], B[j][1])
            #check if overlap
            if lt <= rt:
                ans.append([lt, rt])

            #discard interval considered completely
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans
