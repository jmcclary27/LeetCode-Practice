class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = False
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                idx = i
                intervals.insert(idx, newInterval)
                inserted = True
                break
        
        if not inserted:
            intervals.append(newInterval)
            idx = len(intervals) - 1

        while idx > 0 and intervals[idx][0] <= intervals[idx-1][1]:
            intervals[idx-1][1] = max(intervals[idx][1], intervals[idx-1][1])
            intervals.pop(idx)
            idx -= 1
        
        while idx < len(intervals) - 1 and intervals[idx][1] >= intervals[idx+1][0]:
            intervals[idx][1] = max(intervals[idx+1][1], intervals[idx][1])
            intervals.pop(idx+1)
        
        return intervals