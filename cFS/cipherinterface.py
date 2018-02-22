"""
cFS cipher interface:
all ciphers cFS uses should implement this
"""

__package__ = "cfs"

class CipherInterface:
  def __init__(self, key):
    self.key = key
  
  def decipher(self, s):
    raise NotImplementedError()
  
  def encipher(self, s):
    raise NotImplementedError()
