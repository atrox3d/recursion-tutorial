class Queue(list):
    ''' adds alias methods push and shift to list '''
    def push(self, *args, **kwargs):
        return self.append(*args, **kwargs)

    def shift(self):
        return self.pop(0)


class Stack(list):
    ''' adds alias method push to list '''
    def push(self, *args, **kwargs):
        return self.append(*args, **kwargs)


if __name__ == '__main__':
    print('test stack')
    stack = Stack()
    for i in range(5):
        print(f'push {i}')
        stack.push(i)
    
    while len(stack):
        i = stack.pop()
        print(f'pop {i}')
    
    print()

    print('test queue')
    queue = Queue()
    for i in range(5):
        print(f'push {i}')
        queue.push(i)
    
    while len(queue):
        i = queue.shift()
        print(f'shift {i}')
