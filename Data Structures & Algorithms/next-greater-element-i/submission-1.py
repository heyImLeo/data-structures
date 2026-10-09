class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        stack = []

        for index, val in enumerate(nums2):
            while stack and stack[-1] < val:
                node = stack.pop()
                freq[node] = val
            stack.append(val)
        
        return [freq[x] if x in freq else -1 for x in nums1]

