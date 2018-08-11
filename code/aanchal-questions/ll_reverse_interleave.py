def ll_reverse_interleave(head):
    def _split_in_half(head):
        slow = fast = head
        while fast is not None:
            fast = fast.next.next
            slow = slow.next
        new_head = slow.next
        slow.next = None
        return new_head

    def _reverse(head):
        stk = []
        while head is not None:
            stk.append(head)
        new_head = stk[-1]
        while stk:
            k = stk.pop()
            k.next = stk[-1] if stk else None
        return new_head

    def _interleave(h1, h2):
        while(h2):
                h1.next, h2.next, h1, h2 = h2, h1.next, h1.next, h2.next

    head2 = _split_in_half(head)
    head2 = _reverse(head2)
    _interleave(h1, h2)
    return head
