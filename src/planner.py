"""Flight route planner with multiple optimization strategies."""
from src.graph import FlightGraph
from src.algorithms import (
    bfs_min_stops, 
    dijkstra_cheapest, 
    dijkstra_fastest,
    find_all_routes
)


class FlightPlanner:
    """
    Flight route planning system with support for:
    - Minimum stops (BFS)
    - Cheapest fare (Dijkstra)
    - Fastest duration (Dijkstra)
    - Stop limits
    - Fare filters
    """
    
    def __init__(self):
        self.graph = FlightGraph()
    
    def add_flight(self, source: str, dest: str, fare: int, 
                   duration: int, departure: str = "00:00", airline: str = ""):
        """Add a flight to the network."""
        self.graph.add_flight(source, dest, fare, duration, departure, airline)
    
    def find_route(self, source: str, dest: str, 
                   strategy: str = "cheapest",
                   max_stops: int = 5,
                   max_fare: int = None) -> dict | None:
        """
        Find optimal route based on strategy.
        
        Args:
            source: Starting city
            dest: Destination city
            strategy: "cheapest", "fastest", or "min_stops"
            max_stops: Maximum number of stops allowed
            max_fare: Maximum total fare (optional filter)
        
        Returns:
            Route dict or None if no valid route exists
        """
        if source not in self.graph.cities:
            return {"error": f"City '{source}' not found"}
        if dest not in self.graph.cities:
            return {"error": f"City '{dest}' not found"}
        
        # Find route based on strategy
        if strategy == "min_stops":
            result = bfs_min_stops(self.graph, source, dest, max_stops)
        elif strategy == "fastest":
            result = dijkstra_fastest(self.graph, source, dest, max_stops)
        else:  # cheapest
            result = dijkstra_cheapest(self.graph, source, dest, max_stops)
        
        if result is None:
            return None
        
        # Apply fare filter
        if max_fare and result["total_fare"] > max_fare:
            return {"error": f"No route under ₹{max_fare}. Cheapest is ₹{result['total_fare']}"}
        
        return result
    
    def compare_routes(self, source: str, dest: str, max_stops: int = 5) -> dict:
        """Compare all optimization strategies."""
        return {
            "cheapest": self.find_route(source, dest, "cheapest", max_stops),
            "fastest": self.find_route(source, dest, "fastest", max_stops),
            "min_stops": self.find_route(source, dest, "min_stops", max_stops),
        }
    
    def get_all_routes(self, source: str, dest: str, max_stops: int = 3) -> list:
        """Get all possible routes (limited by max_stops for performance)."""
        return find_all_routes(self.graph, source, dest, max_stops)
    
    def get_cities(self) -> list[str]:
        """Get all cities in the network."""
        return sorted(self.graph.cities)
    
    def print_route(self, route: dict) -> str:
        """Format route for display."""
        if route is None:
            return "No route found"
        if "error" in route:
            return route["error"]
        
        lines = []
        lines.append(f"Route: {' → '.join(route['path'])}")
        lines.append(f"Stops: {route['stops']}")
        lines.append(f"Total Fare: ₹{route['total_fare']}")
        lines.append(f"Total Duration: {route['total_duration']} mins")
        lines.append("\nFlights:")
        for i, f in enumerate(route['flights'], 1):
            lines.append(f"  {i}. {f.source} → {f.destination}: ₹{f.fare}, {f.duration}min")
        return "\n".join(lines)