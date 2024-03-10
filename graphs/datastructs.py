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