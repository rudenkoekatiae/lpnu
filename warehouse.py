class Warehouse:
    def __init__(self):
        self.stack = []
        
    def push(self, box):
        self.stack.append(box)
    
    def pop(self):
        if self.is_empty():
            raise ValueError("The warehouse is empty, there are no boxes to remove.")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise ValueError("The warehouse is empty, there are no boxes to view.")
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def __iter__(self):
        return iter(reversed(self.stack))


warehouse = Warehouse()
warehouse.push("Box 1")
warehouse.push("Box 2")
warehouse.push("Box 3")

print("Current warehouse stack:")
for box in warehouse:
    print("Box in warehouse:", box)

print("\nType 'delete' to remove the top box, 'add' to add a new box, or 'quit' to stop:")
while True:
    try:
        user_input = input("Enter command: ").strip().lower()
        
        if user_input == 'delete':
            print("\nProcessing warehouse stack:")
            print("Top box:", warehouse.peek())
            print("Deleted box:", warehouse.pop())
            print("The top box after deleting:", warehouse.peek() if not warehouse.is_empty() else "No boxes left")
            print("The quantity of boxes:", warehouse.size())
        
        elif user_input == 'add':
            new_box = input("Enter the name of the box to add: ").strip()
            warehouse.push(new_box)
            print("\nProcessing warehouse stack:")
            print("Added box:", new_box)
            print("The top box after adding:", warehouse.peek())
            print("The quantity of boxes:", warehouse.size())
        
        elif user_input == 'quit':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid command. Type 'delete', 'add', or 'quit'.")
    
    except ValueError:
        print("\nThe warehouse is now empty. You cannot delete more boxes.")