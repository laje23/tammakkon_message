class _Container:

    def __init__(self):
        self._dependencies = {}

    def register(self, interface, implementation):
        self._dependencies[interface] = implementation

    def resolve(self, interface):
        return self._dependencies[interface]
    
container = _Container()