"""Tests for graph algorithms."""
import sys
sys.path.insert(0, '.')

from src.graph import FlightGraph
from src.algorithms import bfs_min_stops, dijkstra_cheapest, dijkstra_fastest


def create_test_graph():
    """Create a simple test graph."""
    g = FlightGraph()
    # A --100,60--> B --200,30--> D
    # A --500,20--> D (direct but expensive)
    # A --50,40--> C --50,40--> D (cheap but more stops)
    g.add_flight("A", "B", 100, 60)
    g.add_flight("B", "D", 200, 30)
    g.add_flight("A", "D", 500, 20)
    g.add_flight("A", "C", 50, 40)
    g.add_flight("C", "D", 50, 40)
    return g


def test_bfs_min_stops():
    g = create_test_graph()
    result = bfs_min_stops(g, "A", "D")
    assert result is not None
    assert result["path"] == ["A", "D"]
    assert result["stops"] == 0
    print("✓ BFS min stops works")


def test_dijkstra_cheapest():
    g = create_test_graph()
    result = dijkstra_cheapest(g, "A", "D")
    assert result is not None
    assert result["path"] == ["A", "C", "D"]
    assert result["total_fare"] == 100
    print("✓ Dijkstra cheapest works")


def test_dijkstra_fastest():
    g = create_test_graph()
    result = dijkstra_fastest(g, "A", "D")
    assert result is not None
    assert result["path"] == ["A", "D"]
    assert result["total_duration"] == 20
    print("✓ Dijkstra fastest works")


def test_no_route():
    g = FlightGraph()
    g.add_flight("A", "B", 100, 60)
    result = bfs_min_stops(g, "A", "C")
    assert result is None
    print("✓ No route returns None")


def test_max_stops_constraint():
    g = create_test_graph()
    # With max 0 stops, only direct flight works
    result = dijkstra_cheapest(g, "A", "D", max_stops=0)
    assert result["path"] == ["A", "D"]
    assert result["total_fare"] == 500  # Direct is expensive
    print("✓ Max stops constraint works")


if __name__ == "__main__":
    test_bfs_min_stops()
    test_dijkstra_cheapest()
    test_dijkstra_fastest()
    test_no_route()
    test_max_stops_constraint()
    print("\n✅ All tests passed!")