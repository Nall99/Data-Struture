class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    def __repr__(self) -> str:
        return self.data

class LinkedList:
    def __init__(self,nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
    def __repr__(self) -> str:
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        nodes = [str(node) for node in nodes]
        return " -> ".join(nodes)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next
    
    def add_first(self, node):
        node.next = self.head
        self.head = node
    
    def add_last(self, node):
        if self.head is None:
            self.head = node
        for current_node in self:
            pass
        current_node.next = node
    
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f"Node with data '{target_node_data}' not found")
    
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            return self.add_first(new_node)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception(f"Node with data '{target_node_data}' not found")
    
    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")
        if self.head.data == target_node_data:
            self.head = self.head.next
            return
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception(f"Node with data '{target_node_data}' not found")
    
    def insert_node(self, new_node):
        if self.head == None or self.head.data >= new_node.data:
            return self.add_first(new_node)
        current = self.head
        while current.next != None and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        return 
    
    def insert_sort(self):
        current = self.head
        while current:
            next = current.next
            self.remove_node(current.data)
            self.insert_node(current)
            current = next
        return
   
    def frontBackSplit(self):
        if self.head == None or self.head.next == None:
            return self.head, None
        (slow, fast) = (self.head, self.head.next)

        while fast:
            fast = fast.next
            if fast:
                slow = slow.next
                fast = fast.next
        ret = (self.head, slow.next)
        slow.next = None
        return ret
    
    def sortedMerge(self, Node1, Node2):
        if Node1 == None:
            return Node2
        elif Node2 == None:
            return Node1
        elif Node1.data <= Node2.data:
            result = Node1
            result.next = self.sortedMerge(Node1.next, Node2)
        else:
            result = Node2
            result.next = self.sortedMerge(Node1, Node2.next)
        return result
    
    def mergesort(self, head=None):
        head = self.head
        if head == None or head.next == None:
            return head
        front, back = self.frontBackSplit()

        front = self.mergesort(front)
        back = self.mergesort(back)
        return self.sortedMerge(front, back)
        

