"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        maxx = 0
        cur = 0
        i, j = 0, 0
        while i < len(intervals):
            if starts[i] < ends[j]:
                cur += 1
                maxx = max(maxx, cur)
                i+=1
            else:
                cur -= 1
                j+=1
        return maxx