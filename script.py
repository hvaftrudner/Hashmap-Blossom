from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]
    
  def hash(self, key):
    hash_code = sum(key.encode())
    return hash_code
  
  def compress(self, hash_code):
    return hash_code % self.array_size
  
  def assign(self, key, value):
    new_hash = self.hash(key)
    array_index = self.compress(new_hash)
    #14
    payload = Node([key, value])
    list_at_array = self.array[array_index]
    for load in list_at_array:
      if load[0] == key:
        load[1] == value
    list_at_array.insert(payload)
    
  def retrieve(self, key):
    new_hash = self.hash(key)
    array_index = self.compress(new_hash)
    
    #19
    list_at_index = self.array[array_index]
    for load in list_at_index:
      if load[0] == key:
        return load[1]
      else: 
        return None
    #payload = self.array[array_index]
    
    if payload[0] == key:
      return payload[1]
  
    if payload is None or payload[0] != key:
      return None
    
blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])
  
print(blossom.retrieve('daisy'))  
  
