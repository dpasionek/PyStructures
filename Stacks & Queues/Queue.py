from typing import TypeVar, Generic, Any

T = TypeVar('T', None, Any)

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.queue: list[T] = []
    def __len__(self) -> int:
        return len(self.queue)
    def __str__(self) -> str:
        return str(self.queue)

    def IsEmpty(self) -> bool:
        return len(self) == 0

    def Enqueue(self, item: T) -> None:
        if(type(item) is not self.__orig_class__.__args__[0]):  # type: ignore
            return
        self.queue = self.queue + [item]

    def Dequeue(self) -> T:
        if(not self.IsEmpty()):
            item = self.queue[0]
            self.queue = self.queue[1::]
            return item
        return None  # type: ignore

stack = Queue[int]()
stack.Enqueue(1)
stack.Enqueue(2)
stack.Enqueue(3)
stack.Enqueue("Test")
print(stack)

assert(stack.Dequeue() == 1)
assert(stack.Dequeue() == 2)
assert(stack.Dequeue() == 3)
assert(stack.Dequeue() == None)

