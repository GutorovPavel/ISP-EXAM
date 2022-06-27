class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def delete_duplicates(head:Node) -> Node:
    while head.next is not None:
        if head.value == head.next.value:
            head.next = head.next.next
        else:
            head = head.next
    return head


def partition(head, x):
    less, big, less_head, big_head = None, None, None, None
    current = head
    while current is not None:
        if current.value < x:
            if less_head is None:
                less_head = current
                less = current
            else:
                less.next = current
                less = less.next
        else:
            if big_head is None:
                big_head = current
                big = current
            else:
                big.next = current
                big = big.next
        current = current.next
    if less_head is None:
        return big_head
    if big_head is None:
        return less_head
    less.next = big_head
    big.next = None
    return less_head


def flatten_generator(lst):
    for i in lst:
        if not isinstance(i, list):
            yield i
        else:
            yield from flatten_generator(i)


class FlattenIterator:
    def __iter__(self):
        return self

    def __init__(self, lst):
        self.a = 0
        self.data = []
        self.rec(lst)
        self.counter = 0

    def __next__(self):
        if not self.counter == self.a:
            self.counter += 1
            return self.data.pop(0)
        else:
            raise StopIteration

    def rec(self, lst):
        for i in lst:
            if not isinstance(i, list):
                self.data.append(i)
                self.a += 1
            else:
                self.rec(i)


def Print(head: Node):
    while head is not None:
        print(head.value, end=' ')
        head = head.next
    print()


