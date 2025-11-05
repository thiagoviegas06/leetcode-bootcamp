class MyQueue(object):

    def __init__(self):
        self.stack_in = []   # For enqueue
        self.stack_out = []  # For dequeue

    def push(self, x):
        """Push element x to the back of queue."""
        self.stack_in.append(x)

    def pop(self):
        """Removes the element from in front of queue and returns it."""
        self.move()
        return self.stack_out.pop()

    def peek(self):
        """Get the front element."""
        self.move()
        return self.stack_out[-1]

    def empty(self):
        """Return whether the queue is empty."""
        return not self.stack_in and not self.stack_out

    def move(self):
        """Move elements only when stack_out is empty."""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
