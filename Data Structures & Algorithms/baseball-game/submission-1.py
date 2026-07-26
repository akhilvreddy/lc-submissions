class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        count = 0

        for op in operations:
            if op == "+":
                count += res[-1]+res[-2]
                res.append(res[-1]+res[-2])

            elif op == "D":
                count += 2*res[-1]
                res.append(2*res[-1])
            elif op == "C":
                count -= res.pop()
            else:
                res.append(int(op))
                count += int(op)
        
        return count

        