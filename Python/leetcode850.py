class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        # rectangles[i] = [x1, y1, x2, y2]
        start = list(rectangles)
        end = list(rectangles)
        start.sort(key=lambda r: r[0])
        end.sort(key=lambda r: r[2])

        activeSet = []
        N = len(rectangles)

        totalArea = 0
        cur = start[0][0]
        nxt = 0
        i = 0
        j = 0
        while j < N:
            while i < N and start[i][0] == cur:
                self.insert(activeSet, start[i])
                i += 1
            while j < N and end[j][2] == cur:
                self.remove(activeSet, end[j])
                j += 1
            if i < N and j < N:
                if start[i][0] <= end[j][2]:
                    nxt = start[i][0]
                else:
                    nxt = end[j][2]
            elif j < N:
                nxt = end[j][2]
            horiz = nxt - cur
            vert = self.vertDist(activeSet)
            totalArea += vert * horiz
            cur = nxt
        return totalArea

    def vertDist(self, activeSet):
        n = len(activeSet)
        totalLen = 0
        start = 0
        end = 0
        i = 0
        while i < n:
            start = activeSet[i][1]
            end = activeSet[i][3]
            while i < n and activeSet[i][1] <= end:
                if activeSet[i][3] > end:
                    end = activeSet[i][3]
                i += 1
            totalLen += end - start
        return totalLen


    def insert(self, array, rect):
        if len(array) == 0:
            array.append(rect)
        i = self.bs(array, 0, len(array), rect)
        array.insert(i, rect)

    def remove(self, array, rect):
        i = self.bs(array, 0, len(array), rect)
        array.remove(i) 


    def bs(self, array, left, right, rect):
        mid = (left + right) / 2
        if (array[mid][1] == rect[1]):
            if (array[mid][3] == rect[3]):
                return array[mid]        
            elif (array[mid][3] < rect[3]):
                if mid == right:
                    return array[mid + 1]
                return self.bs(array, mid + 1, right, rect)
            else:
                if mid == left:
                    return array[mid]
                return self.bs(array, left, mid - 1, rect) 
        elif (array[mid][1] < rect[1]):
            if mid == right:
                return array[mid + 1]
            return self.bs(array, mid + 1, right, rect)
        else:
            if mid == left:
                return array[mid]
            return self.bs(array, left, mid - 1, rect)
            
        
        


