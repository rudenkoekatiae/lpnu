from collections import deque
from menu import MENU


class Order:
    def __init__(self, description, execution_time):
        self.description = description
        self.execution_time = execution_time
        self.status = "Pending"

    def __str__(self):
        return f"'{self.description}' (Execution time: {self.execution_time} min, Status: {self.status})"


class RestaurantOrders:
    def __init__(self):
        self.orders = deque()
        self.completed_orders = []
        self.current_order = None
        self.time_elapsed = 0

    def add_order(self, item_ids):
        items = []
        max_time = 0
        for item_id in item_ids:
            item = MENU.get(item_id)
            if item:
                items.append(item["name"])
                max_time = max(max_time, item["time"])
            else:
                print(f"Item with ID {item_id} not found in the menu. Skipping.")
        
        if not items:
            print("No valid items selected. Order not added.")
            return

        order_description = ", ".join(items)
        order = Order(order_description, max_time)
        self.orders.append(order)
        print(f"Order '{order_description}' added to the queue with execution time {max_time} minutes.")

    def process_order(self, minutes=0):
        self.time_elapsed += minutes
        print(f"{minutes} minutes have passed. Processing orders...")

        while minutes > 0 and (self.current_order or self.orders):
            if self.current_order is None:
                self.current_order = self.orders.popleft()
                self.current_order.status = "In Process"

                if self.current_order.execution_time > minutes:
                    print(f"The order '{self.current_order.description}' is now being processed.")

            if self.current_order.execution_time <= minutes:
                minutes -= self.current_order.execution_time
                self.current_order.execution_time = 0
                self.current_order.status = "Done"
                self.completed_orders.append(self.current_order)
                print(f"The order '{self.current_order.description}' is completed.")
                self.current_order = None
            else:
                self.current_order.execution_time -= minutes
                minutes = 0

    def show_orders(self):
        print("\nCurrent status of orders:")
        if self.current_order:
            print(f"Order in process: {self.current_order}")
        else:
            print("No order is currently in process.")
        if self.orders:
            print("Pending orders in queue:")
            for order in self.orders:
                print(f"- {order}")
        else:
            print("No pending orders in the queue.")
        if self.completed_orders:
            print("Completed orders:")
            for order in self.completed_orders:
                print(f"- {order}")
        else:
            print("No completed orders yet.")

    def is_empty(self):
        return not self.orders and not self.current_order


def show_menu():
    print("\nMenu:")
    for item_id, item in MENU.items():
        print(f"{item_id}. {item['name']} (Execution time: {item['time']} min)")


restaurant = RestaurantOrders()
print("\nRestaurant ordering system")
print("Commands: 'add', 'process', 'show', 'menu', 'quit'")
print("Use 'process' like 'process 10' to pass 10 minutes.")

while True:
    command = input("\nEnter command: ").strip().lower()
    if command == "menu":
        show_menu()
    elif command.startswith("add"):
        try:
            item_ids = list(map(int, input("Enter item IDs separated by spaces: ").split()))
            restaurant.add_order(item_ids)
        except ValueError:
            print("Please enter valid item IDs.")
    elif command.startswith("process"):
        try:
            minutes = int(command.split()[1])
            restaurant.process_order(minutes)
        except (IndexError, ValueError):
            print("Please specify the minutes, e.g., 'process 10'.")
    elif command == "show":
        restaurant.show_orders()
    elif command == "quit":
        print("Goodbye!")
        break
    else:
        print("Unknown command. Available commands: 'add', 'process', 'show', 'menu', 'quit'.")