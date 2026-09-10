class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        start_color = image[sr][sc]

        if image[sr][sc] == newColor:
            return image
        
        image[sr][sc] = newColor
        queue = deque([(sr, sc)])

        while queue:
            row, col = queue.popleft()

            for u, v in directions:
                nr, nc = row+u, col+v
                if 0<=nr<rows and 0<=nc<cols and image[nr][nc] == start_color:
                    queue.append((nr, nc))
                    image[nr][nc] = newColor
        
        return image