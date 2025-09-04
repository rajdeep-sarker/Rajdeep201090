#!/usr/bin/env python3
"""
Simple tests for the flight search system
"""

import sys
import os

# Add current directory to path to import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flight_search import FlightSearchEngine, Flight

def test_flight_creation():
    """Test Flight class creation"""
    print("🧪 Testing Flight class creation...")
    
    flight = Flight(
        flight_id="TEST001",
        airline="Test Airlines",
        departure_time="10:00",
        arrival_time="11:30",
        price=5000.0,
        departure_city="Dhaka",
        arrival_city="Cox's Bazar",
        duration="1h 30m"
    )
    
    assert flight.flight_id == "TEST001"
    assert flight.price == 5000.0
    assert flight.departure_city == "Dhaka"
    print("✅ Flight creation test passed!")

def test_search_engine_initialization():
    """Test FlightSearchEngine initialization"""
    print("🧪 Testing FlightSearchEngine initialization...")
    
    engine = FlightSearchEngine()
    
    # Should have loaded mock data
    assert len(engine.flights) > 0
    print(f"✅ Search engine initialized with {len(engine.flights)} flights!")

def test_flight_search():
    """Test flight search functionality"""
    print("🧪 Testing flight search...")
    
    engine = FlightSearchEngine()
    
    # Test searching for Dhaka to Cox's Bazar
    flights = engine.search_flights("Dhaka", "Cox's Bazar")
    assert len(flights) > 0
    
    # Verify all flights are for the correct route
    for flight in flights:
        assert flight.departure_city.lower() == "dhaka"
        assert flight.arrival_city.lower() == "cox's bazar"
    
    print(f"✅ Found {len(flights)} flights for Dhaka → Cox's Bazar!")

def test_minimum_cost_search():
    """Test minimum cost flight search"""
    print("🧪 Testing minimum cost search...")
    
    engine = FlightSearchEngine()
    
    min_flight = engine.find_minimum_cost_flight("Dhaka", "Cox's Bazar")
    assert min_flight is not None
    
    # Verify it's actually the cheapest
    all_flights = engine.search_flights("Dhaka", "Cox's Bazar")
    cheapest_price = min(flight.price for flight in all_flights)
    
    assert min_flight.price == cheapest_price
    
    print(f"✅ Minimum cost flight found: {min_flight.flight_id} - ৳{min_flight.price:,.2f}")

def test_price_sorting():
    """Test flight sorting by price"""
    print("🧪 Testing price sorting...")
    
    engine = FlightSearchEngine()
    
    sorted_flights = engine.get_all_flights_sorted_by_price("Dhaka", "Cox's Bazar")
    
    # Verify sorting
    for i in range(len(sorted_flights) - 1):
        assert sorted_flights[i].price <= sorted_flights[i + 1].price
    
    print(f"✅ Flights properly sorted by price: ৳{sorted_flights[0].price:,.2f} to ৳{sorted_flights[-1].price:,.2f}")

def test_case_insensitive_search():
    """Test that search is case insensitive"""
    print("🧪 Testing case insensitive search...")
    
    engine = FlightSearchEngine()
    
    # Test different case variations
    flights1 = engine.search_flights("dhaka", "cox's bazar")
    flights2 = engine.search_flights("DHAKA", "COX'S BAZAR")
    flights3 = engine.search_flights("Dhaka", "Cox's Bazar")
    
    assert len(flights1) == len(flights2) == len(flights3)
    
    print("✅ Case insensitive search working correctly!")

def test_no_flights_found():
    """Test behavior when no flights are found"""
    print("🧪 Testing no flights found scenario...")
    
    engine = FlightSearchEngine()
    
    # Search for non-existent route
    flights = engine.search_flights("Dhaka", "Chittagong")
    assert len(flights) == 0
    
    min_flight = engine.find_minimum_cost_flight("Dhaka", "Chittagong")
    assert min_flight is None
    
    print("✅ No flights found scenario handled correctly!")

def run_all_tests():
    """Run all tests"""
    print("🚀 Starting Flight Search System Tests")
    print("=" * 50)
    
    try:
        test_flight_creation()
        test_search_engine_initialization()
        test_flight_search()
        test_minimum_cost_search()
        test_price_sorting()
        test_case_insensitive_search()
        test_no_flights_found()
        
        print("\n" + "=" * 50)
        print("🎉 ALL TESTS PASSED! ✅")
        print("Flight search system is working correctly!")
        print("=" * 50)
        
    except AssertionError as e:
        print(f"\n❌ TEST FAILED: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n💥 UNEXPECTED ERROR: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_all_tests()