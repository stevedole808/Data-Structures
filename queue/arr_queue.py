class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []
    
    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)

    def dequeue(self):
        if len(self.storage) == 0:
            return None
        return self.storage.pop(0)