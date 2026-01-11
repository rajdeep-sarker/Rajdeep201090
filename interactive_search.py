#!/usr/bin/env python3
"""
Interactive Flight Search CLI
Interactive command-line interface for searching flight tickets
"""

import sys
from flight_search import FlightSearchEngine, Flight

def print_banner():
    """Print application banner"""
    print("\n" + "="*60)
    print("🛫 BANGLADESH FLIGHT SEARCH SYSTEM 🛬")
    print("   Find the cheapest flights across Bangladesh")
    print("="*60)

def print_menu():
    """Print main menu options"""
    print("\n📋 MENU OPTIONS:")
    print("1. Search Dhaka → Cox's Bazar (Minimum Cost)")
    print("2. Search Dhaka → Cox's Bazar (All Flights)")
    print("3. Search any route")
    print("4. View all available routes")
    print("5. Exit")
    print("-" * 40)

def display_flight_summary(flight: Flight, is_cheapest: bool = False):
    """Display a concise flight summary"""
    status = "⭐ CHEAPEST" if is_cheapest else ""
    print(f"✈️  {flight.flight_id} | {flight.airline}")
    print(f"    {flight.departure_time} → {flight.arrival_time} ({flight.duration})")
    print(f"    💰 ৳{flight.price:,.2f} {status}")

def search_dhaka_to_coxs_minimum():
    """Search for minimum cost flight from Dhaka to Cox's Bazar"""
    search_engine = FlightSearchEngine()
    
    print("\n🔍 Searching for cheapest flight: Dhaka → Cox's Bazar")
    print("-" * 50)
    
    min_flight = search_engine.find_minimum_cost_flight("Dhaka", "Cox's Bazar")
    
    if min_flight:
        print("💰 CHEAPEST FLIGHT FOUND:")
        print(min_flight)
        
        # Show savings compared to most expensive
        all_flights = search_engine.get_all_flights_sorted_by_price("Dhaka", "Cox's Bazar")
        if len(all_flights) > 1:
            most_expensive = all_flights[-1]
            savings = most_expensive.price - min_flight.price
            print(f"\n💡 You save ৳{savings:,.2f} compared to the most expensive option!")
    else:
        print("❌ No flights found.")

def search_dhaka_to_coxs_all():
    """Show all flights from Dhaka to Cox's Bazar"""
    search_engine = FlightSearchEngine()
    
    print("\n📋 All flights: Dhaka → Cox's Bazar (sorted by price)")
    print("-" * 55)
    
    flights = search_engine.get_all_flights_sorted_by_price("Dhaka", "Cox's Bazar")
    
    if flights:
        cheapest_id = flights[0].flight_id
        
        for i, flight in enumerate(flights, 1):
            print(f"\n{i}.")
            display_flight_summary(flight, flight.flight_id == cheapest_id)
        
        print(f"\n📊 Summary: {len(flights)} flights available")
        print(f"💰 Price range: ৳{flights[0].price:,.2f} - ৳{flights[-1].price:,.2f}")
    else:
        print("❌ No flights found.")

def search_custom_route():
    """Search for flights on a custom route"""
    search_engine = FlightSearchEngine()
    
    print("\n🗺️  Custom Route Search")
    print("-" * 30)
    
    from_city = input("From city: ").strip()
    to_city = input("To city: ").strip()
    
    if not from_city or not to_city:
        print("❌ Please enter valid city names.")
        return
    
    print(f"\n🔍 Searching: {from_city} → {to_city}")
    
    flights = search_engine.get_all_flights_sorted_by_price(from_city, to_city)
    
    if flights:
        print(f"✅ Found {len(flights)} flight(s):")
        cheapest_id = flights[0].flight_id
        
        for i, flight in enumerate(flights, 1):
            print(f"\n{i}.")
            display_flight_summary(flight, flight.flight_id == cheapest_id)
    else:
        print("❌ No flights found for this route.")
        print("💡 Currently available routes:")
        print("   • Dhaka → Cox's Bazar")

def show_available_routes():
    """Show all available routes"""
    print("\n🗺️  AVAILABLE FLIGHT ROUTES")
    print("-" * 35)
    print("Currently supported routes:")
    print("✈️  Dhaka → Cox's Bazar")
    print("   📍 6 daily flights available")
    print("   💰 Price range: ৳7,500 - ৳9,200")
    print("   ⏱️  Duration: ~1h 15-20m")
    print("\n💡 More routes coming soon!")

def main():
    """Main interactive CLI function"""
    print_banner()
    
    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                search_dhaka_to_coxs_minimum()
            elif choice == '2':
                search_dhaka_to_coxs_all()
            elif choice == '3':
                search_custom_route()
            elif choice == '4':
                show_available_routes()
            elif choice == '5':
                print("\n👋 Thank you for using Bangladesh Flight Search!")
                print("   Safe travels! ✈️")
                break
            else:
                print("❌ Invalid choice. Please enter 1-5.")
            
            input("\nPress Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()