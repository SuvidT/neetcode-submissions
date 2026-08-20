class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        import heapq
        from collections import defaultdict
    
        adj = defaultdict(list)
        for s, e, d in edges:
            adj[s].append((e, d))
    
        dists = {src: 0}
        queue = [(0, src)]
    
        while queue:
            dist, node = heapq.heappop(queue)
    
            if dist > dists[node]:
                continue
    
            for neighbor, weight in adj[node]:
                new_dist = dist + weight
    
                if neighbor not in dists or new_dist < dists[neighbor]:
                    dists[neighbor] = new_dist
                    heapq.heappush(queue, (new_dist, neighbor))
    
        for i in range(n):
            if i not in dists:
                dists[i] = -1
                
        return dists
    