class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c: i for i, c in enumerate(s)}
        last_point, start = 0, 0
        result = []
        for i, c in enumerate(s):
            last_point = last_point if last_point > last[c] else last[c]
            if last_point == i:
                result.append(last_point - start + 1)
                last_point += 1
                start = last_point
        return result