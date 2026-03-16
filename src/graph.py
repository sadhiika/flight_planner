"""Graph data structure for flight network."""
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Flight:
    source: str
    destination: str
    fare: int
    duration: int  # in minutes
    departure: str  # e.g., "09:00"
    airline: str


class FlightGraph:
    """Directed weighted graph representing flight network."""
    
    def __init__(self):
        self.adjacency: dict[str, list[Flight]] = defaultdict(list)
        self.cities: set[str] = set()
    
    def add_flight(self, source: str, dest: str, fare: int, 
                   duration: int, departure: str = "00:00", airline: str = ""):
        """Add a flight (directed edge) to the graph."""
        flight = Flight(source, dest, fare, duration, departure, airline)
        self.adjacency[source].append(flight)
        self.cities.add(source)
        self.cities.add(dest)
    
    def get_flights(self, city: str) -> list[Flight]:
        """Get all outgoing flights from a city."""
        return self.adjacency.get(city, [])
    
    def get_neighbors(self, city: str) -> list[str]:
        """Get all direct destinations from a city."""
        return [f.destination for f in self.adjacency[city]]
    
    def __repr__(self):
        return f"FlightGraph({len(self.cities)} cities, {sum(len(v) for v in self.adjacency.values())} flights)"