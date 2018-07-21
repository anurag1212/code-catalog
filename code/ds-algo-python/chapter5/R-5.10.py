def __init__(self, shift):
    self._forward = "".join([chr((k + shift) % 26 + ord("A")) for k in range(26)])
    self._backward = "".join([chr((k - shift) % 26 + ord("A")) for k in range(26)])
