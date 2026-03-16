"""BFS and Dijkstra implementations for flight routing."""
from collections import deque
import heapq
from src.graph import FlightGraph, Flight


def bfs_min_stops(graph: FlightGraph, source: str, dest: str, 
                  max_stops: int = float('inf')) -> dict | None:
    """
    Find route with minimum number of stops using BFS.
    
    Time Complexity: O(V + E) where V = cities, E = flights
    Space Complexity: O(V)
    
    Args:
        graph: Flight network
        source: Starting city
        dest: Destination city
        max_stops: Maximum allowed stops (excluding source)
    
    Returns:
        Dict with path, stops, and flights or None if no route exists
    """
    if source == dest:
        return {"path": [source], "stops": 0, "flights": []}
    
    # Queue: (current_city, path, flights_taken, stops)
    queue = deque([(source, [source], [], 0)])
    visited = {source: 0}  # city -> min stops to reach
    
    while queue:
        city, path, flights, stops = queue.popleft()
        
        if stops > max_stops:
            continue
        
        for flight in graph.get_flights(city):
            next_city = flight.destination
            next_stops = stops + 1
            
            # Found destination
            if next_city == dest:
                return {
                    "path": path + [next_city],
                    "stops": stops,  # stops between source and dest
                    "flights": flights + [flight],
                    "total_fare": sum(f.fare for f in flights + [flight]),
                    "total_duration": sum(f.duration for f in flights + [flight])
                }
            
            # Visit if not seen or found shorter path
            if next_city not in visited or visited[next_city] > next_stops:
                visited[next_city] = next_stops
                queue.append((next_city, path + [next_city], flights + [flight], next_stops))
    
    return None


def dijkstra_cheapest(graph: FlightGraph, source: str, dest: str,
                      max_stops: int = float('inf')) -> dict | None:
    """
    Find cheapest route using Dijkstra's algorithm.
    
    Time Complexity: O(E log V) where V = cities, E = flights
    Space Complexity: O(V)
    
    Args:
        graph: Flight network
        source: Starting city
        dest: Destination city  
        max_stops: Maximum allowed stops
    
    Returns:
        Dict with path, total_fare, flights or None if no route exists
    """
    # Min heap: (total_fare, stops, city, path, flights)
    heap = [(0, 0, source, [source], [])]
    
    # Best fare to reach (city, stops) - allows revisiting with fewer stops
    best = {}
    
    while heap:
        fare, stops, city, path, flights = heapq.heappop(heap)
        
        # Found destination
        if city == dest:
            return {
                "path": path,
                "stops": stops - 1 if stops > 0 else 0,
                "flights": flights,
                "total_fare": fare,
                "total_duration": sum(f.duration for f in flights)
            }
        
        # Skip if we've found better
        state = (city, stops)
        if state in best and best[state] <= fare:
            continue
        best[state] = fare
        
        if stops > max_stops:
            continue
        
        # Explore neighbors
        for flight in graph.get_flights(city):
            next_city = flight.destination
            next_fare = fare + flight.fare
            next_stops = stops + 1
            
            next_state = (next_city, next_stops)
            if next_state not in best or best[next_state] > next_fare:
                heapq.heappush(heap, (
                    next_fare, 
                    next_stops, 
                    next_city, 
                    path + [next_city],
                    flights + [flight]
                ))
    
    return None


def dijkstra_fastest(graph: FlightGraph, source: str, dest: str,
                     max_stops: int = float('inf')) -> dict | None:
    """
    Find fastest route (minimum total duration) using Dijkstra's algorithm.
    
    Time Complexity: O(E log V)
    Space Complexity: O(V)
    """
    # Min heap: (total_duration, stops, city, path, flights)
    heap = [(0, 0, source, [source], [])]
    best = {}
    
    while heap:
        duration, stops, city, path, flights = heapq.heappop(heap)
        
        if city == dest:
            return {
                "path": path,
                "stops": stops - 1 if stops > 0 else 0,
                "flights": flights,
                "total_duration": duration,
                "total_fare": sum(f.fare for f in flights)
            }
        
        state = (city, stops)
        if state in best and best[state] <= duration:
            continue
        best[state] = duration
        
        if stops > max_stops:
            continue
        
        for flight in graph.get_flights(city):
            next_city = flight.destination
            next_duration = duration + flight.duration
            next_stops = stops + 1
            
            next_state = (next_city, next_stops)
            if next_state not in best or best[next_state] > next_duration:
                heapq.heappush(heap, (
                    next_duration,
                    next_stops,
                    next_city,
                    path + [next_city],
                    flights + [flight]
                ))
    
    return None


def find_all_routes(graph: FlightGraph, source: str, dest: str,
                    max_stops: int = 3) -> list[dict]:
    """
    Find all possible routes using DFS (for comparison).
    
    Time Complexity: O(V!) worst case (all permutations)
    Space Complexity: O(V) for recursion stack
    """
    routes = []
    
    def dfs(city: str, path: list, flights: list, visited: set):
        if len(path) - 1 > max_stops + 1:
            return
        
        if city == dest:
            routes.append({
                "path": path.copy(),
                "stops": len(path) - 2,
                "flights": flights.copy(),
                "total_fare": sum(f.fare for f in flights),
                "total_duration": sum(f.duration for f in flights)
            })
            return
        
        for flight in graph.get_flights(city):
            next_city = flight.destination
            if next_city not in visited:
                visited.add(next_city)
                path.append(next_city)
                flights.append(flight)
                
                dfs(next_city, path, flights, visited)
                
                flights.pop()
                path.pop()
                visited.remove(next_city)
    
    dfs(source, [source], [], {source})
    return sorted(routes, key=lambda x: x["total_fare"])