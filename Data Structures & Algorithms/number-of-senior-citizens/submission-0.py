class Solution:
    def countSeniors(self, details: List[str]) -> int:
        senior = 0
        for det in details:
            age = int(det[11:13])
            senior += 1 if age > 60 else 0
        return senior