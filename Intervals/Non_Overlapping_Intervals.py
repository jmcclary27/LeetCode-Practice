class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])
        counter, length = 0, len(intervals)

        for i in range(length - 1, 0, -1):
            if intervals[i][0] < intervals[i-1][1]:
                intervals[i][0] = max(intervals[i-1][0], intervals[i][0])
                intervals.pop(i-1)
                counter += 1
        
        return counter