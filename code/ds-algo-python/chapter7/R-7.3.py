def count_recursive(head):
    if head.next is None:
        return 1
    return 1 + count_recursive(head.next)
