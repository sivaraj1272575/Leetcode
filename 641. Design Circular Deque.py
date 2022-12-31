class MyCircularDeque:

    def __init__(self, k: int):
        self.front = -1
        self.rear = -1
        self.queue = [-1]*k
        self.k = k

    def insertFront(self, value: int) -> bool:
        if(self.isFull() == False):
            if(self.front == -1):
                self.front = 0
                self.rear = 0
            else:
                self.front = (self.front-1)%self.k
            self.queue[self.front] = value
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if(self.isFull() == False):
            self.rear = (self.rear + 1) % self.k
            self.queue[self.rear] = value
            if(self.front == -1):
                self.front = 0
            return True
        return False
            
        

    def deleteFront(self) -> bool:
        if(self.isEmpty() == False):
            if(self.front == self.rear):
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1)%self.k
            return True
        return False

    def deleteLast(self) -> bool:
        if(self.isEmpty() == False):
            if(self.front == self.rear):
                self.front = self.rear = -1
            else:
                self.rear = (self.rear-1) % self.k
            return True
        return False

    def getFront(self) -> int:
        if(self.isEmpty() == False):
            return self.queue[self.front]
        return -1

    def getRear(self) -> int:
        if(self.isEmpty() == False):
            return self.queue[self.rear]
        return -1

    def isEmpty(self) -> bool:
        if self.front == -1 and self.rear == -1:
            return True
        return False

    def isFull(self) -> bool:
        if((self.rear+1)%self.k == self.front):
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
