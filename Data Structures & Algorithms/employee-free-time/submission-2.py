"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        newschedule = []
        for employee in schedule:
            for interval in employee:
                newschedule.append(interval)

        newschedule.sort(key = lambda x : (x.start, x.end))
        
        for i in newschedule:
            print(i.start, i.end)

        disjoint = [newschedule[0]]

        for curr in newschedule[1:]:
            if curr.start <= disjoint[-1].end:
                disjoint[-1].end = max(disjoint[-1].end, curr.end)
            else:
                disjoint.append(Interval(curr.start, curr.end))

        
        res = []
        for i in range(len(disjoint)-1):
            res.append(Interval(disjoint[i].end, disjoint[i+1].start))

        return res
