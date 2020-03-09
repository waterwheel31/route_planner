import math 
import heapq


def distance(M, point1, point2):
                
    return math.sqrt((M.intersections[point1][0] - M.intersections[point2][0])**2 + (M.intersections[point1][1] - M.intersections[point2][1])**2)


def shortest_path(M,start,goal):
    #print("shortest path called")
    
    print('\nstart:', start, 'goal:', goal)
    
    sg_distance = distance(M, start, goal)
     
    intersections = list(M.intersections.keys())
    
    f_values = {}
    g_values = {}
    h_values = {}
    routes = {}
    
    explored = set()
    frontier = []
    goal_min = math.inf
    frontier_min = math.inf
    path = []
    
    current_node = start
    
    route = [start]
    g = 0
    h = sg_distance
    f = g + h
    
    g_values[current_node] = g
    h_values[current_node] = h
    f_values[current_node] = f
    routes[current_node] = route
    
    # Explore 
    explored.add(current_node)
    
    # Search 
    while goal_min >= frontier_min :
        
        if current_node == goal: 
            if f < goal_min: 
                goal_min = f
                path = routes[current_node]
                     
        adjacent = M.roads[current_node]
        for adj in adjacent: 

            g = g_values[current_node] + distance(M, current_node, adj) 
            h = distance(M, adj, goal) 
            f = g + h     

            if adj not in f_values.keys() or f < f_values[adj]: 

                route = routes[current_node].copy()
                route.append(adj)            

                g_values[adj] = g
                h_values[adj] = h
                f_values[adj] = f
                routes[adj] = route 

            if adj not in explored: 
                if adj not in frontier: 
                    heapq.heappush(frontier, (f, adj))

        # Extend 
      
        f, current_node = heapq.heappop(frontier)
        explored.add(current_node)
                
        if len(frontier) <= 0: break
            
        frontier_min = frontier[0][0]
  
        
    return path