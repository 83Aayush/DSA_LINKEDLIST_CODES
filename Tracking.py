class TicketQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def isFull(self):
        return self.rear == self.capacity - 1

    def isEmpty(self):
        return self.front == -1 or self.front > self.rear

    def enqueue(self, ticket_id):
        if self.isFull():
            print("Queue is Full! Cannot add new ticket.")
            return
        if self.front == -1:
            self.front = 0
        self.rear += 1
        self.queue[self.rear] = ticket_id
        print(f"Ticket {ticket_id} added to the queue.")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is Empty! No ticket to process.")
            return
        ticket = self.queue[self.front]
        self.front += 1
        print(f"Ticket {ticket} has been processed.")
        if self.front > self.rear:
            self.front = self.rear = -1

    def size(self):
        if self.isEmpty():
            return 0
        return self.rear - self.front + 1

    def display(self):
        if self.isEmpty():
            print("Queue is Empty!")
        else:
            print("Current Tickets in Queue:")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()


q = TicketQueue(5)
q.enqueue(101)
q.enqueue(102)
q.enqueue(103)
q.display()
print("Current size:", q.size())
q.dequeue()
q.display()
print("Is queue full?", q.isFull())
