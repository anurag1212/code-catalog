def concat(l_head, m_head):
    t = l_head
    while t.next is not None:
        t = t.next
    t.next = m_head
    return l_head
