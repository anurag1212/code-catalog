Have last_touched attribute for nodes. Set tail at last element.
Every access moves element to front and sets last_touched=curr_time.
Curr_time increments for every access. For every access, check curr_time
minus tails last_touched (implement wraparound too to avoid large curr_times).
If > n, while tail.next if curr_time-tail.last_touched>n tail=tail.next.
