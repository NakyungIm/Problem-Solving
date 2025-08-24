# https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start = image[sr][sc]
        if start == color:
            return image

        rows, cols = len(image), len(image[0])
        marked = [[False]*cols for _ in range(rows)]

        def isValid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def neighbors(r, c):
            indices = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            return [(nr, nc) for nr, nc in indices if isValid(nr, nc) and image[nr][nc] == start]

        queue = [(sr, sc)]
        while queue:
            r, c = queue.pop(0)
            if marked[r][c]:
                continue
            marked[r][c] = True
            image[r][c] = color
            for nr, nc in neighbors(r, c):
                if not marked[nr][nc]:
                    queue.append((nr, nc))

        return image
