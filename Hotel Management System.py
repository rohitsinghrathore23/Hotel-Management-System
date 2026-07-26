class Hotel:
    def __init__(self, name, available_rooms, location, rating, price_per_room):
        self.name = name
        self.available_rooms = available_rooms
        self.location = location
        self.rating = rating
        self.price_per_room = price_per_room

    def display(self):
        print(f"""
Hotel Name       : {self.name}
Available Rooms  : {self.available_rooms}
Location         : {self.location}
Rating           : {self.rating}
Price Per Room   : ₹{self.price_per_room}
------------------------------------------
""")


class Customer:
    def __init__(self, customer_name, customer_id, booking_cost):
        self.customer_name = customer_name
        self.customer_id = customer_id
        self.booking_cost = booking_cost

    def display(self):
        print(f"""
Customer Name : {self.customer_name}
Customer ID   : {self.customer_id}
Booking Cost  : ₹{self.booking_cost}
""")


class HotelManagementSystem:

    def __init__(self):
        self.hotels = []
        self.customers = []

    # -------------------------
    # Add Sample Data
    # -------------------------
    def load_sample_data(self):

        self.hotels = [
            Hotel("H1", 4, "Bangalore", 5, 100),
            Hotel("H2", 5, "Bangalore", 5, 200),
            Hotel("H3", 6, "Mumbai", 3, 100)
        ]

        self.customers = [
            Customer("U1", 2, 1000),
            Customer("U2", 3, 1200),
            Customer("U3", 4, 1100)
        ]

    # -------------------------
    # Display Hotels
    # -------------------------
    def display_hotels(self):

        if not self.hotels:
            print("No hotels available.\n")
            return

        print("\n------ HOTEL DETAILS ------")

        for hotel in self.hotels:
            hotel.display()

    # -------------------------
    # Sort By Name
    # -------------------------
    def sort_by_name(self):

        self.hotels.sort(key=lambda hotel: hotel.name)

        print("\nHotels Sorted By Name")
        self.display_hotels()

    # -------------------------
    # Sort By Rating
    # -------------------------
    def sort_by_rating(self):

        self.hotels.sort(
            key=lambda hotel: hotel.rating,
            reverse=True
        )

        print("\nHotels Sorted By Rating")
        self.display_hotels()

    # -------------------------
    # Sort By Available Rooms
    # -------------------------
    def sort_by_rooms(self):

        self.hotels.sort(
            key=lambda hotel: hotel.available_rooms,
            reverse=True
        )

        print("\nHotels Sorted By Available Rooms")
        self.display_hotels()

    # -------------------------
    # Search By City
    # -------------------------
    def search_by_city(self):

        city = input("Enter city name : ").strip()

        found = False

        print(f"\nHotels Available in {city}\n")

        for hotel in self.hotels:

            if hotel.location.lower() == city.lower():
                hotel.display()
                found = True

        if not found:
            print("No hotels found in this city.\n")

    # -------------------------
    # Display Customer Bookings
    # -------------------------
    def display_customers(self):

        print("\n------ CUSTOMER BOOKINGS ------")

        for customer, hotel in zip(self.customers, self.hotels):

            customer.display()

            print("Booked Hotel :", hotel.name)
            print("--------------------------------")

    # -------------------------
    # Menu
    # -------------------------
    def menu(self):

        while True:

            print("""
=========== HOTEL MANAGEMENT SYSTEM ===========

1. Display Hotels
2. Sort Hotels by Name
3. Sort Hotels by Rating
4. Sort Hotels by Available Rooms
5. Search Hotels by City
6. Display Customer Bookings
7. Exit

===============================================
""")

            try:

                choice = int(input("Enter your choice : "))

                if choice == 1:
                    self.display_hotels()

                elif choice == 2:
                    self.sort_by_name()

                elif choice == 3:
                    self.sort_by_rating()

                elif choice == 4:
                    self.sort_by_rooms()

                elif choice == 5:
                    self.search_by_city()

                elif choice == 6:
                    self.display_customers()

                elif choice == 7:
                    print("\nThank you for using Hotel Management System.")
                    break

                else:
                    print("Invalid choice. Please try again.")

            except ValueError:
                print("Please enter only numeric values.")


# -------------------------
# Driver Code
# -------------------------

if __name__ == "__main__":

    system = HotelManagementSystem()

    system.load_sample_data()

    system.menu()