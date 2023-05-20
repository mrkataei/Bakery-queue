class CircularQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * self.max_size
        self.front = 0
        self.rear = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, item):
        if not self.is_full():
            self.queue[self.rear] = item
            self.rear = (self.rear + 1) % self.max_size
            self.size += 1
        else:
            print("Queue is full. Cannot enqueue item.")

    def dequeue(self):
        if not self.is_empty():
            item = self.queue[self.front]
            self.queue[self.front] = None
            self.front = (self.front + 1) % self.max_size
            self.size -= 1
            return item
        else:
            print("Queue is empty. Cannot dequeue item.")

    def __iter__(self):
        index = self.front
        count = 0
        while count < self.size:
            yield self.queue[index]
            index = (index + 1) % self.max_size
            count += 1

    def __str__(self):
        return '\n'.join(str(item) for item in self)
