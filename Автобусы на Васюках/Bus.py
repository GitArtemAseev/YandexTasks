import heapq
N = int(input())
d, v= map(int, input().split())
R = int(input())
graph = {i: [] for i in range(1, N + 1)}

for _ in range(R):
    a, time_arr, b, time_dep = map(int, input().split())
    graph[a].append((b, time_arr, time_dep))
    
def min_route(graph, start, end):
    dist = {i:float('inf') for i in range(1,len(graph)+1)}
    dist[start] = 0
    current_values = [(0,start)]    
   
    while len(current_values) != 0:
        current_time, current_node = heapq.heappop(current_values)
        for i in graph[current_node]:
            node, ar, dep = map(int, i)               
            if current_time <= ar:
                if dep < dist[node]:
                    dist[node] = dep
                    heapq.heappush(current_values,(dep, node))
    if dist[end] == float('inf'):
        print(-1)
    else:
        print(dist[end])
min_route(graph, d, v)