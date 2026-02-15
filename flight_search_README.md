# 🛫 Bangladesh Flight Search System

A Python-based flight ticket search system that helps you find the cheapest flights from Dhaka to Cox's Bazar and other routes across Bangladesh.

## ✨ Features

- 🔍 **Smart Search**: Find flights between cities with minimum cost optimization
- 💰 **Cost Analysis**: Compare prices and find the best deals
- 📊 **Multiple Options**: View all available flights sorted by price
- 🎯 **Focused on Bangladesh**: Specializes in domestic flight routes
- 💻 **CLI Interface**: Easy-to-use command-line interface
- 🧪 **Tested**: Comprehensive test suite included

## 🚀 Quick Start

### Basic Usage

```bash
# Run the simple flight search
python3 flight_search.py

# Run the interactive CLI
python3 interactive_search.py

# Run tests
python3 test_flight_search.py
```

### Example Output

```
🛫 Flight Ticket Search System
==================================================
Searching for flights from Dhaka to Cox's Bazar...

💰 MINIMUM COST FLIGHT FOUND:
------------------------------
Flight NS201 - Novoair
Route: Dhaka → Cox's Bazar
Departure: 09:45
Arrival: 11:00
Duration: 1h 15m
Price: ৳7,500.00

💡 Cost Analysis:
   Cheapest: ৳7,500.00
   Most Expensive: ৳9,200.00
   You save: ৳1,700.00 (18.5%) by choosing the cheapest option!
```

## 📋 Available Routes

Currently supported routes:
- **Dhaka → Cox's Bazar** (6 daily flights)
  - Airlines: Biman Bangladesh, US-Bangla, Novoair
  - Price range: ৳7,500 - ৳9,200
  - Duration: ~1h 15-20m

## 🏗️ Project Structure

```
├── flight_search.py       # Main flight search engine
├── interactive_search.py  # Interactive CLI interface
├── test_flight_search.py  # Test suite
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🧪 Testing

The project includes comprehensive tests to ensure reliability:

```bash
python3 test_flight_search.py
```

Tests cover:
- Flight object creation
- Search engine initialization
- Flight search functionality
- Minimum cost optimization
- Price sorting
- Case-insensitive search
- Error handling

## 💻 API Usage

You can also use the flight search engine programmatically:

```python
from flight_search import FlightSearchEngine

# Initialize the search engine
search_engine = FlightSearchEngine()

# Find the cheapest flight
min_flight = search_engine.find_minimum_cost_flight("Dhaka", "Cox's Bazar")
print(f"Cheapest flight: {min_flight.airline} - ৳{min_flight.price}")

# Get all flights sorted by price
all_flights = search_engine.get_all_flights_sorted_by_price("Dhaka", "Cox's Bazar")
for flight in all_flights:
    print(f"{flight.flight_id}: ৳{flight.price}")
```

## 🔧 Technical Details

- **Language**: Python 3.x
- **Dependencies**: None (uses only standard library)
- **Data**: Mock flight data (easily extensible to real APIs)
- **Architecture**: Object-oriented design with clean separation of concerns

## 🛣️ Future Enhancements

Potential improvements for the future:
- Integration with real airline APIs
- More routes across Bangladesh and international
- Date-based search
- Web interface using Flask
- Database integration
- Booking functionality
- Price alerts and notifications

## 👨‍💻 Author

**Rajdeep Sarker**
- 🎓 Student & Aspiring Programmer
- 🐍 Learning Python
- 📧 Contact: sarkerrajdeep8@gmail.com

## 📄 License

This project is open source and available under the MIT License.

---

*Built with ❤️ for travelers in Bangladesh*