class PriorityQueue:
    def __init__(self):
        self.queue = []

    def addElem(self, value):
        self.queue.append(value)
        self.queue.sort(reverse=False)

    def pop(self):
        return self.queue.pop(0)
