from typing import TypeVar, Generic, Any

T = TypeVar('T', None, Any)

class Stack(Generic[T]):
    def __init__(self) -> None:
        self.stack: list[T] = []
    def __len__(self) -> int:
        return len(self.stack)
    def __str__(self) -> str:
        return str(self.stack)

    def IsEmpty(self) -> bool:
        return len(self) == 0

    def Push(self, item: T) -> None:
        if(type(item) is not self.__orig_class__.__args__[0]):  # type: ignore
            return
        self.stack = self.stack + [item]

    def Pop(self) -> T:
        if(not self.IsEmpty()):
            item = self.stack[len(self) - 1]
            self.stack = self.stack[:-1]
            return item
        return None  # type: ignore

stack = Stack[int]()
stack.Push(1)
stack.Push(2)
stack.Push(3)
stack.Push("Test")
print(stack)

assert(stack.Pop() == 3)
assert(stack.Pop() == 2)
assert(stack.Pop() == 1)
assert(stack.Pop() == None)

