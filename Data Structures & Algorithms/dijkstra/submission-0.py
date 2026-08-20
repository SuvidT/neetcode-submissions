class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        import heapq

        dists = {src: 0}
        queue = [(0, src)]
        heapq.heapify(queue)
    
        while queue:
            dist, node = heapq.heappop(queue)
            for s, e, d in edges:
                if s == node:
                    heapq.heappush(queue, (dist + d, e))
                    if e in dists:
                        if dists[e] > (dist + d):
                            dists[e] = dist + d
                    else:
                        dists[e] = dist + d
    
        return dists
 