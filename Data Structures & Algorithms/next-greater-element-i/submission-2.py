class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        stack = []

        for index, val in enumerate(nums2):
            while stack and stack[-1] < val:
                node = stack.pop()
                freq[node] = val
            stack.append(val)
        
        return [-1 if x not in freq else freq[x] for x in nums1]
