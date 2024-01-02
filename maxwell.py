class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node=Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        
        iter = self.head
        while iter.next:
            iter=iter.next
        iter.next = Node(data,None)

    def getlength(self):
        count=0
        iter=self.head
        while iter:
            iter=iter.next
            count+=1
        return count
    
    def inseart_at_index(self, index, data):
        if index < 0 or index >= self.getlength():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        iter = self.head
        while iter:
            if count == index-1:
                node = Node(data, iter.next)
                iter.next = node
                break
            iter = iter.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.getlength():
            raise Exception ("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        iter = self.head
        while iter:
            if count == index -1:
                iter.next = iter.next.next
                break
            iter = iter.next
            count += 1


    def printing(self):
        if self.head is None:
            print("linked list is empty nigga")
            return
        
        iter=self.head
        llst=''
        while iter:
            llst+=str(iter.data)+'-->'
            iter=iter.next
        print(llst)
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begining(19)
    ll.insert_at_begining(13)
    ll.insert_at_begining(24)
    ll.insert_at_begining(78)
    ll.insert_at_end(77)
    ll.remove_at(3)
    ll.inseart_at_index(2,89)
    ll.printing()
    print(ll.getlength())
        