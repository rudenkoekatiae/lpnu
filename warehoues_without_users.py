class Warehouse:
    def __init__(self):
        self.stack = []
        
    def push(self, box):
        self.stack.append(box)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "The warehouse is empty, there are no boxes to remove."
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "The warehouse is empty, there are no boxes to view."
    
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
warehouse.push("Box 4")
warehouse.push("Box 5")


for box in warehouse:
    print("Box in warehouse:", box)

print("\nProcessing warehouse stack:")
while not warehouse.is_empty():
    print("Top box:", warehouse.peek())
    print("Deleted box:", warehouse.pop())
    print("The top box after deleting:", warehouse.peek() if not warehouse.is_empty() else "No boxes left")
    print("The quantity of boxes:", warehouse.size())