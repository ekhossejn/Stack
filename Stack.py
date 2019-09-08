class MyStack():
    def __init__(self):
        self.__data = []
    def is_empty(self) -> bool:
        return (len(self.__data) == 0)
    def size(self) -> int:
        return len(self.__data)
    def top(self) -> int:
        if self.is_empty():
            raise IndexError
        return self.__data[-1]
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError
        return self.__data.pop(-1)
 
    def push(self, element: int) -> None:
        if type(element) is not int:
            raise TypeError
        self.__data.append(int(element))
 
    def __repr__(self):
        return 'MyStack({})'.format(', '.join(map(str, self.__data)))
 
    def get_data(self) -> list:
        return self.__data[:]
 
 
 
 
def test_is_empty():
    assert(a.is_empty() == True)
    a.push(3)
    assert(a.is_empty() == False)
    a.pop()
    assert(a.is_empty() == True)
 
def test_size():
    for i in range(10):
        a.push(i)
        assert(a.size() == i + 1)
    for i in range(10):
        a.pop()
        assert(a.size() == (9 - i))
 
def test_top():
    try:
        a.top()
    except IndexError:
        None
    else:
        raise Exception('Failed')
    for i in range(10):
        a.push(i)
        assert(a.top() == i)
    for i in range(10):
        assert(a.top() == (9 - i))
        a.pop()
 
def test_pop():
    try:
        a.pop()
    except IndexError:
        None
    else:
        raise Exception('Failed')
    for i in range(10):
        a.push(i)
    for i in range(10):
        assert(a.pop() == (9 - i))
 
def test_push():
    for i in range(5):
        try:
            a.push(str(i))
        except TypeError:
            None
        else:
            raise Exception('Failed')
    for i in range(5):
        try:
            a.push(i)
        except TypeError:
            raise Exception('Failed')
        else:
            None
    for i in range(5):
        a.pop()
def test_data():
    assert(a.get_data() == [])
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(2)
    assert(a.get_data() == [2, 3, 4, 2])
    a.pop()
    assert(a.get_data() == [2, 3, 4])
    arr = a.get_data()
    arr.pop(-1)
    assert(a.get_data() == [2, 3, 4])
    a.pop()
    a.pop()
    a.pop()

def test_repr():
    assert(a.__repr__() == 'MyStack()')
    a.push(2)
    a.push(3)
    a.push(4)
    a.push(2)
    assert(a.__repr__() == 'MyStack(2, 3, 4, 2)')
    a.pop()
    assert(a.__repr__() == 'MyStack(2, 3, 4)')
    arr = a.__repr__()
    arr = 'MyStack()'
    assert(a.__repr__() == 'MyStack(2, 3, 4)')
a = MyStack()
test_is_empty()
test_size()
test_top()
test_pop()
test_push()
test_data()
test_repr()
