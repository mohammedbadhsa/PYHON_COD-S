
class my_queue_dsa:

    def __init__(self):
        self.item = []

    def isemty(self):
        return self.item == []

    def enqueue(self,item):
        self.item.append(0,item)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)

ob1 = my_queue_dsa()

print(ob1.enqueue())
print(ob1.size())