import copy


class Result:
    def __init__(self, value, error):
        self.value = value
        self.error = error

    def __str__(self):
        return str(self.value) + " " + str(self.error)


class Stack:
    def __init__(self):
        self.items = []
        self.start = 0
        self.end = 0

    def push(self, item):
        self.items.append(copy.deepcopy(item))
        self.end += 1

    def pop(self):
        if self.end == self.start:
            return Result(None, "Stack is empty")
        else:
            self.end -= 1
            return Result(self.items[self.end], "No error")

    def peek(self):
        if self.end == self.start:
            return Result(None, "Stack is empty")
        else:
            return Result(self.items[self.end - 1], "No error")

    def __str__(self):
        return str(self.items[self.start:self.end])


print('-*-' * 5 + 'Stack' + '-*-' * 5)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(None)
print(stack)
print(stack.peek())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.peek())
print(stack.pop())
print(stack.pop())


class Queue:
    def __init__(self):
        self.items = []
        self.start = 0
        self.end = 0

    def enqueue(self, item):
        self.items.append(copy.deepcopy(item))
        self.end += 1

    def dequeue(self):
        if self.end == self.start:
            return Result(None, "Queue is empty")
        else:
            self.start += 1
            return Result(self.items[self.start - 1], "No error")

    def peek(self):
        if self.end == self.start:
            return Result(None, "Queue is empty")
        else:
            return Result(self.items[self.start], "No error")

    def __str__(self):
        return str(self.items[self.start:self.end])


print('-*-' * 5 + 'Queue' + '-*-' * 5)
queue = Queue()
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(None)
print(queue)
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())
queue.dequeue()
print(queue.peek())


class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0] * m for i in range(n)]

    def get_element(self, i, j):
        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            return None
        return self.matrix[i][j]

    def set_element(self, i, j, value):
        if i < 0 or i >= self.n or j < 0 or j >= self.m:
            return None
        self.matrix[i][j] = value

    @staticmethod
    def transpose(m):
        return [[row[i] for row in m] for i in range(len(m[0]))]

    @staticmethod
    def multiply(matrix1, matrix2):
        if len(matrix1[0]) != len(matrix2):
            return None
        result = [[0] * len(matrix2[0]) for i in range(len(matrix1))]
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
        return result

    def map(self, func):
        mat = copy.deepcopy(self.matrix)
        for i in range(self.n):
            for j in range(self.m):
                if issubclass(type(func(self.matrix[i][j])), Exception):
                    return
                mat = func(self.matrix[i][j])
        self.matrix = mat

    def __str__(self):
        return str(self.matrix)


print('-*-' * 5 + 'Matrix' + '-*-' * 5)
matrix = Matrix(2, 3)
print(matrix)
matrix.set_element(0, 0, 1)
matrix.set_element(0, 1, 2)
matrix.set_element(0, 2, 3)
matrix.set_element(1, 0, 4)
matrix.set_element(1, 1, 5)
matrix.set_element(1, 2, 6)
print(matrix)
print(matrix.get_element(0, 0))
print(matrix.get_element(0, 1))
m1 = Matrix.transpose([[1, 2, 3], [4, 5, 6]])
print("Transpose:\n ", m1)
print("Multiply:\n ", Matrix.multiply(matrix.matrix, m1))
try:
    matrix.map(lambda x: x / 0)
except Exception as e:
    print(e)
print("Map:\n ", matrix)

