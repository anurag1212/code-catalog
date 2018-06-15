def __init__(val):
    if isinstance(val, int):
        self._coords = [0]*val
    elif isinstance(val, list):
        self._coords = val
    else:
        raise TypeError()
