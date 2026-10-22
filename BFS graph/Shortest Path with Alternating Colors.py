class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        ans = [-1] * n
        ans[0] = 0

        queue = [(0, 0, "red"), (0, 0, "blue")]
        visited = {(0, "red"), (0, "blue")}
        front = 0

        while front < len(queue):
            node, distance, lstcolor = queue[front]
            front += 1

            if lstcolor == "red":
                for u, v in blueEdges:
                    if u == node:
                        if ans[v] == -1:
                            ans[v] = distance + 1

                        if (v, "blue") not in visited:
                            visited.add((v, "blue"))
                            queue.append((v, distance + 1, "blue"))

            else:
                for u, v in redEdges:
                    if u == node:
                        if ans[v] == -1:
                            ans[v] = distance + 1

                        if (v, "red") not in visited:
                            visited.add((v, "red"))
                            queue.append((v, distance + 1, "red"))

        return ans
