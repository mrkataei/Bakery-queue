class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.stack = [None] * max_size
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1

    def push(self, item):
        if self.is_full():
            print("Stack is full. Cannot push item.")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop item.")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            for i in range(self.top, -1, -1):
                print(self.stack[i])

    def __iter__(self):
        return iter(self.stack)

    def __str__(self):
        return '\n'.join(str(item) for item in self.stack)
  