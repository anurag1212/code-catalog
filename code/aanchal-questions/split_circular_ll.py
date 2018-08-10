def split(head):

    def _headcheck(node):
        return node is head or node.next is head

    def _break(n1, n2):
        while n1.next is not n2:
            n1 = n1.next
        n1.next = None

    slow = fast = head

    while not _headcheck(fast):
        fast = fast.next.next
        slow = slow.next

    h1 = slow.next
    _break(slow, h1)

    h2 = fast if fast is head else fast.next
    _break(fast, h2)

    return h1,h2
