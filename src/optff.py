from collections import defaultdict, deque

def optff(k, requests):
    cache = set()
    misses = 0

    positions = defaultdict(deque) # request -> queue with future occurences
    for i in range(len(requests)):
        positions[requests[i]].append(i)

    for i in range(len(requests)):
        r = requests[i]

        positions[r].popleft() #bc we just ssaw it so oldest needs to go

        if r not in cache: #we have a miss
            misses += 1
            if len(cache) == k:
                # We find the item that its first occurence is the most farthest aka in the queue its [0]
                farthest_item = None
                farthest_dist = -1
                
                for seq in cache:
                    if not positions[seq]:
                        #If there is no more future occurence, this is the best candidate bc we don't need it
                        farthest_item = seq
                        break
                    else:
                        next_pos = positions[seq][0]
                        if next_pos > farthest_dist:
                            farthest_dist = next_pos
                            farthest_item = seq
                            
                cache.remove(farthest_item)
            cache.add(r)
            
    return misses