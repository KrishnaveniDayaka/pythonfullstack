
# Python Project

This folder contains hands-on Python projects built while learning core programming fundamentals.



## Hyderabad Metro Ticket Booking & Fare Management System

**File:** `hyd_metro_station_Ticket_booking_system.py`

A command-line Python project that simulates the Hyderabad Metro (Red Line) ticket booking process — calculating fares based on real station distances, applying age-based discounts, and generating a formatted ticket receipt.

### Features
- Real Hyderabad Metro Red Line stations (Miyapur to LB Nagar, 27 stations)
- Distance-based fare calculation using station position (mirrors real HMRL pricing slabs)
- Age-based discount system:
  - Child (under 12): 50% off
  - Teenager (12–17): 20% off
  - Adult (18–59): no discount
  - Senior Citizen (60+): 40% off
- Auto-detects interchange station (Ameerpet) between Red Line and Blue Line
- Generates a unique ticket ID for every booking
- Tracks all bookings and prints a full summary report at the end
- Case-insensitive station name matching (handles acronyms like JNTU, ESI, MG, LB correctly)

### Python Concepts Used
Data types, comments, operators, keywords, variables, input/output formatting, decision statements, lists, tuples, sets, strings, and dictionaries.

### How to Run
```bash
python hyd_metro_station_Ticket_booking_system.py
```
Then follow the prompts: enter passenger name, age, source station, and destination station.

### Sample Output
```
Enter passenger name: Krishnaveni
Enter passenger age: 22

Enter source station: Miyapur
Enter destination station: Ameerpet
 Note: Ameerpet is an interchange station (Red Line <-> Blue Line).

------------------------------------------
     HYDERABAD METRO TICKET - HMKRI001
------------------------------------------
Name       : Krishnaveni
Age        : 22 (Adult)
Route      : Miyapur -> Ameerpet
Fare       : Rs. 25.00
------------------------------------------


```

### Possible Future Improvements
- Add file/database storage so bookings persist between runs
- Refactor into functions for better code organization
- Add input validation for non-numeric input
- Extend to Blue Line and Green Line stations
