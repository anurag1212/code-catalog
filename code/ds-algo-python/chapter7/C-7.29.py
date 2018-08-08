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
    l._head = rev_ll(l._head)

def rev_ll(head):
    tail = head
    while tail.next:
        tail = tail.next
    newh=tail
    while head is not newh:
        temp = newh.next
        newh.next = head
        temp2 = head.next
        head.next = temp
        head = temp2
    return newh

l=ll()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.add(5)
print(l)
rev(l)
print(l)
