class Stack:
    def __init__(self, s=[]):
        self.s = list(s)
    def push(self, element):
        self.s.append(element)
    def pop(self):
        self.s.pop()
    def peek(self):
        return self.s[0]
    def isEmpty(self):
        return len(self.s)==0




if __name__ == '__main__':
    s = '()[]{}'
    stack = Stack(s)
    stack.pop()
