from collections import deque

#ids --> list of sequences
def fifo(ids, max_cap):
    q = deque()
    cache = set()
    misses = 0

    for seq in ids:
        if seq not in cache:
            misses += 1
            if len(cache) == max_cap:
                cache.remove(q.popleft())
            q.append(seq)
            cache.add(seq)
    return misses


if __name__ == "__main__":
    ids1 = [1,2,2,4]
    print(fifo(ids1, 2))

