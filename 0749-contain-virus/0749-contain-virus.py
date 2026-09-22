class Solution:
    def containVirus(self, isInfected):
        m = len(isInfected)
        n = len(isInfected[0])
        total_walls = 0

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while True:
            regions = []
            visited = [[False] * n for _ in range(m)]

            # Find all infected regions
            for r in range(m):
                for c in range(n):

                    if isInfected[r][c] == 1 and not visited[r][c]:

                        cells = []
                        frontier = set()
                        walls = 0

                        stack = [(r, c)]
                        visited[r][c] = True

                        while stack:
                            x, y = stack.pop()
                            cells.append((x, y))

                            for dx, dy in directions:
                                nx = x + dx
                                ny = y + dy

                                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                                    continue

                                if isInfected[nx][ny] == 0:
                                    frontier.add((nx, ny))
                                    walls += 1

                                elif (isInfected[nx][ny] == 1
                                      and not visited[nx][ny]):
                                    visited[nx][ny] = True
                                    stack.append((nx, ny))

                        regions.append((cells, frontier, walls))

            # No regions found
            if not regions:
                break

            # Find the region threatening the most cells
            target = -1
            max_threat = 0

            for i in range(len(regions)):
                frontier = regions[i][1]

                if len(frontier) > max_threat:
                    max_threat = len(frontier)
                    target = i

            # Nobody can spread anymore
            if target == -1 or max_threat == 0:
                break

            # Quarantine the most dangerous region
            cells, frontier, walls = regions[target]

            total_walls += walls

            for x, y in cells:
                isInfected[x][y] = 2

            # Spread all other regions
            for i in range(len(regions)):
                if i == target:
                    continue

                _, frontier, _ = regions[i]

                for x, y in frontier:
                    isInfected[x][y] = 1

        return total_walls