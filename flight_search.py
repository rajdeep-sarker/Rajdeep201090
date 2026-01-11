#!/usr/bin/env python3
"""
Flight Ticket Search System
Search for flight tickets from Dhaka to Cox's Bazar at minimum cost
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json

class Flight:
    """Represents a flight with details"""
    
    def __init__(self, flight_id: str, airline: str, departure_time: str, 
                 arrival_time: str, price: float, departure_city: str, 
                 arrival_city: str, duration: str):
        self.flight_id = flight_id
        self.airline = airline
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.price = price
        self.departure_city = departure_city
        self.arrival_city = arrival_city
        self.duration = duration
    
    def __str__(self):
        return (f"Flight {self.flight_id} - {self.airline}\n"
                f"Route: {self.departure_city} → {self.arrival_city}\n"
                f"Departure: {self.departure_time}\n"
                f"Arrival: {self.arrival_time}\n"
                f"Duration: {self.duration}\n"
                f"Price: ৳{self.price:,.2f}")
    
    def to_dict(self):
        """Convert flight to dictionary"""
        return {
            'flight_id': self.flight_id,
            'airline': self.airline,
            'departure_time': self.departure_time,
            'arrival_time': self.arrival_time,
            'price': self.price,
            'departure_city': self.departure_city,
            'arrival_city': self.arrival_city,
            'duration': self.duration
        }

class FlightSearchEngine:
    """Flight search engine to find flights and optimize for minimum cost"""
    
    def __init__(self):
        self.flights = []
        self._initialize_flight_data()
    
    def _initialize_flight_data(self):
        """Initialize mock flight data from Dhaka to Cox's Bazar"""
        
        # Mock flight data - in real implementation, this would come from airline APIs
        flight_data = [
            {
                'flight_id': 'BG101',
                'airline': 'Biman Bangladesh Airlines',
                'departure_time': '08:00',
                'arrival_time': '09:15',
                'price': 8500.0,
                'departure_city': 'Dhaka',
                'arrival_city': "Cox's Bazar",
                'duration': '1h 15m'
            },
            {
                'flight_id': 'BG103',
                'airline': 'Biman Bangladesh Airlines',
                'departure_time': '14:30',
                'arrival_time': '15:45',
                'price': 9200.0,
                'departure_city': 'Dhaka',
                'arrival_city': "Cox's Bazar",
                'duration': '1h 15m'
            },
            {
                'flight_id': 'US101',
                'airline': 'US-Bangla Airlines',
                'departure_time': '07:30',
                'arrival_time': '08:50',
                'price': 7800.0,
                'departure_city': 'Dhaka',
                'arrival_city': "Cox's Bazar",
                'duration': '1h 20m'
            },
            {
                'flight_id': 'US103',
                'airline': 'US-Bangla Airlines',
                'departure_time': '16:00',
                'arrival_time': '17:20',
                'price': 8100.0,
                'departure_city': 'Dhaka',
                'arrival_city': "Cox's Bazar",
                'duration': '1h 20m'
            },
            {
                'flight_id': 'NS201',
                'airline': 'Novoair',
                'departure_time': '09:45',
                'arrival_time': '11:00',
                'price': 7500.0,
                'departure_city': 'Dhaka',
                'arrival_city': "Cox's Bazar",
                'duration': '1h 15m'
            },
            {
                'flight_id': 'NS203',
                'airline': 'Novoair',
                'departure_time': '15:15',
                'arrival_time': '16:30',
                'price': 7900.0,
                'departure_city': 'Dhaka',
                'arrival_city': "Cox's Bazar",
                'duration': '1h 15m'
            }
        ]
        
        # Create Flight objects from data
        for data in flight_data:
            flight = Flight(**data)
            self.flights.append(flight)
    
    def search_flights(self, from_city: str, to_city: str) -> List[Flight]:
        """Search for flights between two cities"""
        
        matching_flights = []
        for flight in self.flights:
            if (flight.departure_city.lower() == from_city.lower() and 
                flight.arrival_city.lower() == to_city.lower()):
                matching_flights.append(flight)
        
        return matching_flights
    
    def find_minimum_cost_flight(self, from_city: str, to_city: str) -> Optional[Flight]:
        """Find the flight with minimum cost between two cities"""
        
        flights = self.search_flights(from_city, to_city)
        
        if not flights:
            return None
        
        # Find flight with minimum price
        min_cost_flight = min(flights, key=lambda f: f.price)
        return min_cost_flight
    
    def get_all_flights_sorted_by_price(self, from_city: str, to_city: str) -> List[Flight]:
        """Get all flights sorted by price (ascending)"""
        
        flights = self.search_flights(from_city, to_city)
        return sorted(flights, key=lambda f: f.price)

def main():
    """Main function to demonstrate flight search"""
    
    print("🛫 Flight Ticket Search System")
    print("=" * 50)
    print("Searching for flights from Dhaka to Cox's Bazar...")
    print()
    
    # Initialize search engine
    search_engine = FlightSearchEngine()
    
    # Search for minimum cost flight
    min_cost_flight = search_engine.find_minimum_cost_flight("Dhaka", "Cox's Bazar")
    
    if min_cost_flight:
        print("💰 MINIMUM COST FLIGHT FOUND:")
        print("-" * 30)
        print(min_cost_flight)
        print()
    else:
        print("❌ No flights found for the specified route.")
        return
    
    # Show all available flights sorted by price
    print("📋 ALL AVAILABLE FLIGHTS (sorted by price):")
    print("-" * 50)
    
    all_flights = search_engine.get_all_flights_sorted_by_price("Dhaka", "Cox's Bazar")
    
    for i, flight in enumerate(all_flights, 1):
        print(f"{i}. {flight}")
        if min_cost_flight.flight_id == flight.flight_id:
            print("   ⭐ CHEAPEST OPTION")
        print()
    
    # Show savings information
    if len(all_flights) > 1:
        most_expensive = max(all_flights, key=lambda f: f.price)
        savings = most_expensive.price - min_cost_flight.price
        savings_percentage = (savings / most_expensive.price) * 100
        
        print(f"💡 Cost Analysis:")
        print(f"   Cheapest: ৳{min_cost_flight.price:,.2f}")
        print(f"   Most Expensive: ৳{most_expensive.price:,.2f}")
        print(f"   You save: ৳{savings:,.2f} ({savings_percentage:.1f}%) by choosing the cheapest option!")

if __name__ == "__main__":
    main()