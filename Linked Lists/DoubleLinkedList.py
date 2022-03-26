

class Node(object):
    def __init__(self, data = None) -> None:
        self.prev = None
        self.next = None
        self.data = data

class DoubleLinkedList(object):
    def __init__(self, head = None, tail = None) -> None:
        self.head = head
        self.tail = head
    
    def __str__(self):
        currentNode = self.head
        output = ""
        while(currentNode != None):
            output += f" [{currentNode.prev.data if currentNode.prev != None else 'None'}]~{currentNode.data}~[{currentNode.next.data if currentNode.next != None else 'None'}]  <->  "
            currentNode = currentNode.next
          
        return output + "END"
    
    def Insert(self, node, nodeToInsertAt = None, append = False) -> None:
        if(self.head == self.tail == None):
            self.head = node
            self.tail = node
            return
        if(nodeToInsertAt == None):
            currentTail = self.tail
            self.tail = node
            node.prev = currentTail
            currentTail.next = node
            return
        else:
            nodeSearch = self.Search(nodeToInsertAt)
            currentPrev, currentNext = nodeSearch.prev, nodeSearch.next
            if(append and nodeSearch != None):
                nodeSearch.next = node
                node.prev = nodeSearch
                node.next = currentNext
                if(currentNext != None):
                    currentNext.prev = node
            elif(not append and nodeSearch != None):
                node.next = nodeSearch
                nodeSearch.prev = node
                node.prev = currentPrev
                if(currentPrev != None):
                    currentPrev.next = node
                else:
                    self.head = node
    
    def Delete(self, node) -> None:
        existingNode = self.Search(node)
        if(existingNode != None):
            prev, next = existingNode.prev, existingNode.next
            if(prev != None):
                prev.next = next
            else:
                self.head = next
            if(next != None):
                next.prev = prev
            else:
                self.tail = prev


    def Search(self, node) -> Node:
        currentNode = self.head
        while(currentNode != None):
            if(currentNode.data == node.data):
                break
            currentNode = currentNode.next
        return currentNode

l = DoubleLinkedList(Node(10))
l.Insert(Node(5))
l.Insert(Node(7))
l.Insert(Node(6), Node(5), True)
l.Insert(Node(4), Node(5), False)
l.Insert(Node(8), Node(7), True)
l.Insert(Node(1), Node(10), False)
print(l)
l.Delete(Node(4))

print(l)
l.Delete(Node(8))
print(l)
l.Delete(Node(1))
print(l)
l.Delete(Node(10))
print(l)
l.Delete(Node(5))
print(l)
l.Delete(Node(6))
print(l)
l.Delete(Node(7))
print(l)
l.Insert(Node(1))
print(l)
l.Insert(Node(2))
print(l)
l.Insert(Node(0), Node(1))
print(l)