'''
https://leetcode.com/problems/lru-cache/

Write a program for Least Recently Used (LRU) cache.

1. LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
2. get(int key) return the value of the key if the key exists, otherwise return -1.
3. put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. 

If the number of keys exceeds the capacity from this operation, evict the least recently used key.

For Example:
lRUCache = LRUCache(2)
lRUCache.put(1, 1) # cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
lRUCache.get(1)    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)    # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)    # return -1 (not found)
lRUCache.get(3)    # return 3
lRUCache.get(4)    # return 4


Task 2:
We have a program which is implementation of Least Recently Used (LRU) cache.
Please add clear method to clear all keys/values from cache or reset the cache.


Task 3:
We have a program which is implementation of Least Recently Used (LRU) cache.
Please modify this program to backup the least recently key/values into a physical json file before removing from cache.
'''

import json
import os

class LRUCache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.tm = 0
        self.cache = {}
        self.lru = {}

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        return -1

    def put(self, key, value):
        if len(self.cache) >= self.capacity:
            # find the LRU entry
            old_key = min(self.lru.keys(), key=lambda k:self.lru[k])
            self.__dump(old_key)
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        self.cache[key] = value
        self.lru[key] = self.tm
        self.tm += 1

    def __dump(self, key):
        dump_file_name = "dump.json"
        data = { }
        if os.path.exists(dump_file_name):
            with open(dump_file_name, mode='r', encoding='utf-8') as file:
                text = file.read()
                if text != "": data = json.loads(text)
        
        data[str(key)] = self.cache[key]
        with open(dump_file_name, mode='w', encoding='utf-8') as file:
            json.dump(data, file)


    def clear(self):
        self.tm = 0
        self.cache = {}
        self.lru = {}


lRUCache = LRUCache(2)
print(lRUCache.put(1, 1)) # cache is {1=1}
print(lRUCache.put(2, 2)) # cache is {1=1, 2=2}
print(lRUCache.get(1))    # return 1
print(lRUCache.put(3, 3)) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
#print(lRUCache.get(2))    # returns -1 (not found)
#print(lRUCache.put(4, 4)) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
#print(lRUCache.get(1))    # return -1 (not found)
#print(lRUCache.get(3))    # return 3
#print(lRUCache.get(4))    # return 4


