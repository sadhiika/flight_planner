"""Sample flight data for Indian cities."""
from src.planner import FlightPlanner


def create_sample_network() -> FlightPlanner:
    """Create a sample flight network with Indian cities."""
    planner = FlightPlanner()
    
    # Flights data: (source, dest, fare, duration_mins)
    flights = [
        # From Delhi
        ("Delhi", "Mumbai", 4500, 120, "06:00", "IndiGo"),
        ("Delhi", "Mumbai", 5200, 130, "14:00", "Air India"),
        ("Delhi", "Bangalore", 5500, 150, "08:00", "IndiGo"),
        ("Delhi", "Kolkata", 4800, 120, "07:00", "SpiceJet"),
        ("Delhi", "Chennai", 6000, 165, "09:00", "Vistara"),
        ("Delhi", "Hyderabad", 4200, 110, "10:00", "IndiGo"),
        ("Delhi", "Jaipur", 2500, 45, "11:00", "SpiceJet"),
        
        # From Mumbai
        ("Mumbai", "Delhi", 4600, 125, "07:00", "IndiGo"),
        ("Mumbai", "Bangalore", 3500, 90, "08:00", "IndiGo"),
        ("Mumbai", "Chennai", 4200, 110, "09:00", "Air India"),
        ("Mumbai", "Kolkata", 5500, 150, "10:00", "Vistara"),
        ("Mumbai", "Hyderabad", 3200, 75, "11:00", "SpiceJet"),
        ("Mumbai", "Goa", 2800, 55, "12:00", "IndiGo"),
        
        # From Bangalore
        ("Bangalore", "Delhi", 5600, 155, "06:00", "Vistara"),
        ("Bangalore", "Mumbai", 3600, 95, "07:00", "IndiGo"),
        ("Bangalore", "Chennai", 2200, 45, "08:00", "IndiGo"),
        ("Bangalore", "Hyderabad", 2800, 60, "09:00", "SpiceJet"),
        ("Bangalore", "Kolkata", 5800, 160, "10:00", "Air India"),
        ("Bangalore", "Kochi", 2500, 50, "11:00", "IndiGo"),
        
        # From Chennai
        ("Chennai", "Delhi", 6100, 170, "07:00", "Air India"),
        ("Chennai", "Mumbai", 4300, 115, "08:00", "IndiGo"),
        ("Chennai", "Bangalore", 2100, 40, "09:00", "SpiceJet"),
        ("Chennai", "Hyderabad", 3000, 70, "10:00", "IndiGo"),
        ("Chennai", "Kolkata", 5200, 140, "11:00", "Vistara"),
        
        # From Hyderabad
        ("Hyderabad", "Delhi", 4300, 115, "06:00", "IndiGo"),
        ("Hyderabad", "Mumbai", 3300, 80, "07:00", "SpiceJet"),
        ("Hyderabad", "Bangalore", 2900, 65, "08:00", "IndiGo"),
        ("Hyderabad", "Chennai", 3100, 75, "09:00", "Air India"),
        ("Hyderabad", "Kolkata", 5000, 135, "10:00", "Vistara"),
        
        # From Kolkata
        ("Kolkata", "Delhi", 4900, 125, "06:00", "IndiGo"),
        ("Kolkata", "Mumbai", 5600, 155, "07:00", "Air India"),
        ("Kolkata", "Bangalore", 5900, 165, "08:00", "Vistara"),
        ("Kolkata", "Chennai", 5300, 145, "09:00", "SpiceJet"),
        ("Kolkata", "Guwahati", 3200, 70, "10:00", "IndiGo"),
        
        # From smaller cities
        ("Jaipur", "Mumbai", 4000, 100, "08:00", "SpiceJet"),
        ("Jaipur", "Delhi", 2400, 40, "09:00", "IndiGo"),
        ("Goa", "Mumbai", 2900, 60, "10:00", "IndiGo"),
        ("Goa", "Bangalore", 3200, 70, "11:00", "SpiceJet"),
        ("Kochi", "Mumbai", 4500, 120, "07:00", "Air India"),
        ("Kochi", "Bangalore", 2600, 55, "08:00", "IndiGo"),
        ("Kochi", "Chennai", 3000, 65, "09:00", "SpiceJet"),
        ("Guwahati", "Delhi", 5500, 150, "06:00", "IndiGo"),
        ("Guwahati", "Kolkata", 3100, 65, "07:00", "SpiceJet"),
    ]
    
    for flight in flights:
        planner.add_flight(*flight)
    
    return planner