def bubble(head,l):
    for i in range(l):
        h1=head
        for j in range(l-i):
            if h1.next:
                h2=h1.next
                if h1.val>h2.val:
                    h1.next,h1.prev,h2.next,h2.prev=h2.next,h2.prev,h1.next,h1.prev
                h1=h1.next
