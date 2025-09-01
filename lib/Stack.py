class Stack:

    def __init__(self, items=[], limit=100):
        self.items = items.copy()
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            raise ValueError("Stack is full")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise ValueError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for i in range(len(self.items) - 1, -1, -1):
            if self.items[i] == target:
                return len(self.items) - 1 - i
        return -1
