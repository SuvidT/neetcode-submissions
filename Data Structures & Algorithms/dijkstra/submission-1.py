class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        import heapq
    
        dists = {src: 0}
        queue = []
        heapq.heappush(queue, (0, src))
    
        while queue:
            dist, node = heapq.heappop(queue)
    
            if dist > dists[node]:
                continue
    
            for s, e, d in edges:
                if s == node:
                    if e in dists:
                        if dists[e] > (dist + d):
                            dists[e] = dist + d
                            heapq.heappush(queue, (dist + d, e))
                    else:
                        dists[e] = dist + d
                        heapq.heappush(queue, (dist + d, e))
    
        return dists
 
 