#!/usr/bin/env python

'''Implementation of a simple queue data structure.
The queue has `enqueue`, `dequeue`, and `peek` methods.
Items in the queue have `value` and `behind` attributes.
The queue has `front` and `end` attributes.
'''


class Item(object):
    def __init__(self, value, behind=None):
        self.value = value
        self.behind = behind

    def __str__(self):
        return self.value
