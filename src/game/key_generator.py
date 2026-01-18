import random

class KeyGenerator:
  def __init__(self, keys, length):
    self.keys = keys
    self.length = length

  def generate(self):
    return random.choices(self.keys, k=self.length)
