class Stack():
    def __init__(self, items):
        self.items = items
    def __repr__(self) -> str:
        items = self.items
        items = [str(item) for item in items]
        return ", ".join(items)
    
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[len(self.items)-1]

