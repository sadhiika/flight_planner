"""Demo of flight route planner."""
from src.data import create_sample_network


def main():
    print("=" * 60)
    print("FLIGHT ROUTE PLANNING SYSTEM")
    print("=" * 60)
    
    # Create network
    planner = create_sample_network()
    print(f"\nLoaded {len(planner.get_cities())} cities")
    print(f"Cities: {', '.join(planner.get_cities())}")
    
    # Demo routes
    demos = [
        ("Delhi", "Goa"),
        ("Kolkata", "Kochi"),
        ("Guwahati", "Goa"),
    ]
    
    for source, dest in demos:
        print("\n" + "=" * 60)
        print(f"ROUTE: {source} → {dest}")
        print("=" * 60)
        
        # Compare strategies
        comparison = planner.compare_routes(source, dest)
        
        print("\n📍 MINIMUM STOPS (BFS - O(V+E)):")
        print(planner.print_route(comparison["min_stops"]))
        
        print("\n💰 CHEAPEST FARE (Dijkstra - O(E log V)):")
        print(planner.print_route(comparison["cheapest"]))
        
        print("\n⚡ FASTEST DURATION (Dijkstra - O(E log V)):")
        print(planner.print_route(comparison["fastest"]))
    
    # Demo with constraints
    print("\n" + "=" * 60)
    print("ROUTE WITH CONSTRAINTS: Delhi → Kochi (max 1 stop)")
    print("=" * 60)
    
    result = planner.find_route("Delhi", "Kochi", strategy="cheapest", max_stops=1)
    if result:
        print(planner.print_route(result))
    else:
        print("No direct or 1-stop route available")
    
    result = planner.find_route("Delhi", "Kochi", strategy="cheapest", max_stops=2)
    print("\nWith max 2 stops:")
    print(planner.print_route(result))


if __name__ == "__main__":
    main()