class Foo:

    def __init__(self):
        self._x = None  

    def set(self, value):
        self._x = value

    def get(self):
        return self._x
    

f = Foo()
f.set(5)
print(f'x: {f.get()}')