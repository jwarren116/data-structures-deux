#!/usr/bin/env python

'''Implementation of a simple hash table.
The table has `hash`, `get` and `set` methods.
The hash function uses a very basic hash algorithm to insert the value
into the table.
'''


class HashItem(object):
    def __init__(self):
        pass


class Hash(object):
    def __init__(self, size=1024):
        self.table = []
        for i in range(size):
            self.table.append(list())

    def hash(self):
        pass

    def get(self):
        pass

    def set(self):
        pass
