def shuffle(h1, h2):
    use_l1=True
    while i<len(l1)*2:
        if use_l1:
            t1=h1.next
            h1.next=h2
            h1=t1
        else:
            t2=h2.next
            h2.next=h1
            h2=t2
        use_l1!=use_l1
