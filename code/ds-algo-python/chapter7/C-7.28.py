class ll:
    class _Node(object):
        __slots__ = "val", "next"
        def __init__(self,e):
            self.val = e
            self.next = None
    def __init__(self):
        self._head = self._Node(None)
        self._tail = None
        self._n = 0
    def add(self, e):
        if self._tail:
            self._tail.next = self._Node(e)
            self._tail = self._tail.next
        else:
            self._head.next = self._Node(e)
            self._tail = self._head.next
        self._n += 1
    def __str__(self):
        t=self._head
        string=[]
        while t is not None:
            string.append(t.val)
            t = t.next
        string=list(map(str, string))
        return " -> ".join(string)

def rev(l):
    newh=reverse_ll(l._head)
    l._head = newh

def reverse_ll(head, prev=None):
    if head.next is None:
        head.next = prev
        return head
    newhead=reverse_ll(head.next, head)
    head.next = prev
    return newhead

l=ll()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
print(l)
rev(l)
print(l)
