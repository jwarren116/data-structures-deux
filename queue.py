#!/usr/bin/env python

'''Implementation of a simple queue data structure.
The queue has `enqueue`, `dequeue`, and `peek` methods.
Items in the queue have `value` and `behind` attributes.
The queue has a `front` attribute.
'''


class Item(object):
    def __init__(self, value, behind=None):
        self.value = value
        self.behind = behind

    def __str__(self):
        return self.value


class Queue(object):
    def __init__(self, front=None):
        pass

    def enqueue(self, value):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass
