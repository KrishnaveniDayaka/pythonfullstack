
"""
PROJECT: Hyderabad Metro Ticket Booking & Fare Management System
------------------------------------------------------------------
A CLI-based Python project that simulates real Hyderabad Metro (Red Line)
ticket booking. Users book tickets between actual HMRL stations, fare is
calculated based on distance/segment and age category, discounts are
applied, and a formatted ticket receipt is generated.

Concepts covered:
Introduction, Data Types, Comments, Operators, Keywords, Variables,
Input/Output Formatting, Decision Statements, Lists, Tuple, Set,
String, Dictionary
"""

# ---------------------------------------------------------
# FIXED DATA (Tuple + Dictionary)
# ---------------------------------------------------------

# Tuple -> immutable, since Hyderabad Metro Red Line stations (in order) never change
RED_LINE_STATIONS = (
    "Miyapur", "JNTU College", "KPHB Colony", "Kukatpally",
    "Balanagar", "Moosapet", "Bharatnagar", "Erragadda",
    "ESI Hospital", "S.R Nagar", "Ameerpet", "Punjagutta",
    "Irrum Manzil", "Khairatabad", "Lakdikapul", "Assembly",
    "Nampally", "Gandhi Bhavan", "Osmania Medical College",
    "MG Bus Station", "Malakpet", "New Market", "Musarambagh",
    "Dilsukhnagar", "Chaitanyapuri", "Victoria Memorial", "LB Nagar",
)

# Dictionary -> fare slab chart based on NUMBER OF STATIONS traveled
# (mirrors real HMRL pricing, where fare rises in steps with distance,
#  not a flat per-station rate). Key = max stations in that slab, Value = fare.
FARE_SLABS = {
    2: 10,     # 1-2 stations
    4: 15,     # 3-4 stations
    8: 20,     # 5-8 stations
    12: 25,    # 9-12 stations
    18: 30,    # 13-18 stations
    24: 35,    # 19-24 stations
    26: 40,    # 25+ stations (max possible on this line)
}

# List -> stores dictionaries of all booked passengers (mutable, ordered)
booked_passengers = []

# Set -> stores unique stations visited (auto removes duplicates)
unique_stations_visited = set()

# Variable -> keeps count of tickets booked (int data type)
ticket_counter = 0

# Boolean data type example -> tracks whether booking is still open
booking_open = True

print("=" * 60)
print("     HYDERABAD METRO - TICKET BOOKING SYSTEM (Red Line)")
print("=" * 60)

# ---------------------------------------------------------
# MAIN LOOP -> keeps booking tickets until user says no
# ---------------------------------------------------------
while booking_open:

    # ---- INPUT SECTION ----
    name = input("\nEnter passenger name: ").strip().title()   # string method
    age = int(input("Enter passenger age: "))                  # type conversion -> int

    print("\nAvailable Stations (Red Line):")
    print(", ".join(RED_LINE_STATIONS))                        # string join

    source_input = input("\nEnter source station: ").strip()
    destination_input = input("Enter destination station: ").strip()

    # Dictionary -> maps lowercase station name to its correctly-cased official name
    # (avoids .title() mangling acronyms like JNTU, ESI, MG, LB, S.R)
    station_lookup = {station.lower(): station for station in RED_LINE_STATIONS}

    # ---- DECISION STATEMENT: validate stations exist on the line ----
    if source_input.lower() not in station_lookup or destination_input.lower() not in station_lookup:
        print(" Invalid station name! Please check spelling and try again.")
        continue   # keyword -> skip to next loop iteration

    source = station_lookup[source_input.lower()]         # normalized to official casing
    destination = station_lookup[destination_input.lower()]

    # ---- DECISION STATEMENT: same source and destination is not a valid trip ----
    if source == destination:
        print(" Source and destination cannot be the same station.")
        continue

    # ---- Calculate distance using station positions in the tuple ----
    source_index = RED_LINE_STATIONS.index(source)        # tuple method
    destination_index = RED_LINE_STATIONS.index(destination)
    stations_traveled = abs(destination_index - source_index)   # operator: abs difference

    # ---- DECISION STATEMENTS: find the correct fare slab ----
    # Loops through slab boundaries in order and picks the first one that fits
    base_fare = None
    for max_stations in sorted(FARE_SLABS):    # sorted() -> list of slab keys in order
        if stations_traveled <= max_stations:
            base_fare = FARE_SLABS[max_stations]   # dictionary lookup
            break

    # ---- DECISION STATEMENTS: fare discount rules ----
    if age < 12:
        discount = 0.5          # 50% discount for children
        category = "Child"
    elif age >= 60:
        discount = 0.4          # 40% discount for senior citizens
        category = "Senior Citizen"
    elif 12 <= age < 18:
        discount = 0.2          # 20% discount for students/teenagers
        category = "Teenager"
    else:
        discount = 0.0          # no discount for adults
        category = "Adult"

    # ---- OPERATORS: arithmetic + logical ----
    final_fare = base_fare - (base_fare * discount)   # arithmetic operators
    is_interchange_trip = (source == "Ameerpet" or destination == "Ameerpet")  # logical operator

    if is_interchange_trip:
        print(" Note: Ameerpet is an interchange station (Red Line <-> Blue Line).")

    # ---- Generate Ticket ID using STRING slicing/concatenation ----
    ticket_counter += 1
    ticket_id = "HM" + name[:3].upper() + str(ticket_counter).zfill(3)

    # ---- Store data in List (dictionary inside list) ----
    passenger_record = {
        "ticket_id": ticket_id,
        "name": name,
        "age": age,
        "category": category,
        "source": source,
        "destination": destination,
        "fare": final_fare,
    }
    booked_passengers.append(passenger_record)   # list method

    # ---- Update Set with visited stations ----
    unique_stations_visited.add(source)
    unique_stations_visited.add(destination)

    # ---- OUTPUT: formatted ticket receipt ----
    print("\n" + "-" * 42)
    print(f"     HYDERABAD METRO TICKET - {ticket_id}")
    print("-" * 42)
    print(f"Name       : {name}")
    print(f"Age        : {age} ({category})")
    print(f"Route      : {source} -> {destination}")
    print(f"Fare       : Rs. {final_fare:.2f}")
    print("-" * 42)

    # ---- Ask to continue booking ----
    choice = input("\nBook another ticket? (yes/no): ").strip().lower()
    if choice != "yes":
        booking_open = False   # ends the while loop

# ---------------------------------------------------------
# FINAL SUMMARY REPORT
# ---------------------------------------------------------
print("\n" + "=" * 60)
print("                  BOOKING SUMMARY REPORT")
print("=" * 60)

print(f"\nTotal Tickets Booked: {len(booked_passengers)}")   # list length

print("\nAll Passengers:")
for passenger in booked_passengers:                          # loop through list of dicts
    print(f" - {passenger['ticket_id']} | {passenger['name']} "
          f"| {passenger['category']} | {passenger['source']} -> "
          f"{passenger['destination']} | Rs.{passenger['fare']:.2f}")

print("\nUnique Stations Visited Today:")
print(unique_stations_visited)   # set -> no duplicate stations

total_revenue = sum(p["fare"] for p in booked_passengers)     # generator + sum
print(f"\nTotal Revenue Collected: Rs. {total_revenue:.2f}")

print("\nThank you for traveling with Hyderabad Metro!")
print("=" * 60)
