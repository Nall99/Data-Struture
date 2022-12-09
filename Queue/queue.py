class Queue():
    def __init__(self, items=list):
        self.items = items
    def __repr__(self) -> str:
        items = self.items
        items = [str(item) for item in items]
        return ", ".join(items)
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items[0]

