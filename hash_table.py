#!/usr/bin/env python

'''Implementation of a simple hash table.
The table has `hash`, `get` and `set` methods.
The hash function uses a very basic hash algorithm to insert the value
into the table.
'''


class HashItem(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self, size=1024):
        self.table = []
        for i in range(size):
            self.table.append(list())

    def hash(self, key):
        hash_value = 0
        try:
            for i in key:
                hash_value += ord(i)
            return hash_value % len(self.table)
        except TypeError:
            raise TypeError('Please input a valid string for `key`')

    def get(self, key):
        hashed_key = self.hash(key)
        for k in self.table[hashed_key]:
            if k[0] == key:
                return k[1]
        else:
            raise KeyError('Value not found')

    def set(self, key, val):
        hashed_key = self.hash(key)
        for k in self.table[hashed_key]:
            if k[0] == key:
                self.table[hashed_key][k] = (key, val)
        else:
            self.table[hashed_key].append((key, val))
