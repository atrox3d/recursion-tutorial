def idk(total: int, slots: int):
    store = [0 for _ in range(slots)]

    store[0] = total    
    print(store)
    for i in range(1, slots):
        while store[i] < total:
            store[i-1] -= 1
            store[i] += 1
            print(store)
        print()

def wtf(total: int, slots: int):
    store = [0 for _ in range(slots)]
    
    store[0] = total
    while store[-1] <= total:
        print(store)
        for i in range(1, slots):
            pass


# idk(5, 4)

wtf(5, 4)