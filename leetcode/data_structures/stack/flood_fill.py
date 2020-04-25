class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def is_safe(x, y):
            return (x>=0 and x < len(image)) and (y>=0 and y < len(image[0])) and image[x][y] == val

        def DFS(i, j):
            rx = [-1,1,0,0]
            cy = [0,0,-1,1]
            if not is_safe(i, j):
                return
            image[i][j] = newColor
            for k in range(len(rx)):
                    DFS(i+rx[k], j+cy[k])

        idx, idy = sr, sc
        val = image[sr][sc]
        if val != newColor:
            DFS(idx, idy)
        return image
