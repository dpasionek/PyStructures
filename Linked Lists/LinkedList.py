class Node(object):
    def __init__(self, value: object) -> None:
        self.next: Node = None  # type: ignore
        self.value: str = str(value)
    def __str__(self) -> str:
        return f"Node Value: {self.value}"


# Search, Insert, Delete
class LinkedList(object):
    def __init__(self, node: Node = None) -> None: # type: ignore
        self.head: Node = node
        self.tail: Node = node
    def __str__(self):
        node = self.head
        nodeList = " "
        while(node != None):
            nodeList = nodeList + f"{node.value} -> "
            node = node.next
        nodeList += "END"
        return nodeList
    def Append(self, node: Node) -> None:
        currentTail = self.tail
        self.tail = node
        if(currentTail != None):
            currentTail.next = node
        if(self.head == None):
            self.head = node
    def Prepend(self, node: Node) -> None:
        currentHead = self.head
        self.head = node
        if(self.head != None):
            self.head.next = currentHead
        if(self.tail == None):
            self.tail = currentHead
    def Insert(self, nodeToInsert: Node, nodeIndex: Node, append: bool = False) -> None: # True to append, false to Prepend
        (prevNode, node) = self.SearchByValue(nodeIndex.value)
        if(node == None):
            self.Append(nodeToInsert)
            return
        if(append):
            nextNode = node.next
            node.next = nodeToInsert
            nodeToInsert.next = nextNode
        else:
            nextNode = node
            prevNode.next = nodeToInsert
            nodeToInsert.next = nextNode

    def DeleteByValue(self, nodeToDelete) -> None:
        (prevNode, node) = self.SearchByValue(nodeToDelete)
        if(node == None):
            print(f"No node with value '{node}' exists!")
            return
        if(node.next == None and prevNode == None):
            self.head = None
            self.tail = None
            return
        if(node.next == None):
            self.tail = prevNode
            prevNode.next = None # type: ignore
            return
        if(prevNode == None):
            self.head = node.next
            return
        else:
            prevNode.next = node.next
            node = None
            

    def SearchByValue(self, nodeValue) -> tuple[Node, Node]: # type: ignore
        print(f"Searching for node with value: {nodeValue}")
        currentNode = self.head
        prevNode = None
        while(currentNode != None):
            if(currentNode.value == nodeValue and currentNode.next == None):
                return(None, currentNode)
            if(currentNode.next != None and currentNode.next.value == nodeValue):
                prevNode = currentNode
                currentNode = currentNode.next
                break
            currentNode = currentNode.next
        if(currentNode == None):
            return (None, None)
        else:
            return(prevNode, currentNode)
        
            
    def Search(self, node: Node) -> tuple[Node, Node]: # type: ignore
        currentNode = self.head
        prevNode = None
        while(currentNode != node or currentNode != None):
            if(currentNode == None):
                return(None, None)
            if(currentNode.next == node):
                prevNode = currentNode
            currentNode = currentNode.next
        if(currentNode != node):
            return (None, None) # type: ignore
        else:
            return (prevNode, currentNode)

head = input("Value of Head: ")

l = LinkedList(Node(head))

cmd = None
while(cmd != "exit"):
    cmd = input("Command: ")
    match cmd:
        case "i":
            l.Append(Node(input("\tAppend Value: ")))
        case "I":
            l.Insert(Node(input("Insert Value")), Node(input("\tAt Value: ")))
        case "p":
            l.Prepend(Node(input("\tPrepend Value: ")))
        case "d":
            l.DeleteByValue(input("\tDelete Value: "))
        case "P":
            print(l)
        case "exit":
            break
