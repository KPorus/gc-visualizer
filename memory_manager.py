import gc

class GCManager:
    """A simple memory manager to create objects and force deletion."""
    def __init__(self,name):
        self.name = name
        self.ref = None

def create_objects(create_cycle):
    a = GCManager("A")
    b = GCManager("B")
    a.ref = b
    if create_cycle:
        b.ref = a
    return a, b

def force_delete(a, b):
    del a
    del b
    gc.collect()