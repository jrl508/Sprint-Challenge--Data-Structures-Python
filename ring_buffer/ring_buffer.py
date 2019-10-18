class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #using current as a counter and an index to set the appended item
    self.storage[self.current] =  item

    self.current += 1

    # check capacity after appending to reset
    if self.current == self.capacity:
      self.current = 0

  def get(self):
    # return self.storage RETURNS ['a', 'b', 'c', 'd', None]
    # iterate through storage and return whatever is not None
    return [x for x in self.storage if x is not None]