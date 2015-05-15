#!/usr/bin/env python

'''Implementation of a simple queue data structure.
The queue has `enqueue`, `dequeue`, and `peek` methods.
Items in the queue have `value` and `behind` attributes.
The queue has `front` and `back` attributes.
'''


class Item(object):
    def __init__(self, value, behind=None):
        self.value = value
        self.behind = behind

    def __str__(self):
        return self.value


class Queue(object):
    def __init__(self, front=None, back=None):
        self.front = front
        self.back = back

    def enqueue(self, value):
        self.item = Item(value)
        self.back.behind = self.item
        self.back = self.item

    def dequeue(self):
        try:
            self.old_front = self.front
            self.front = self.front.behind
            return self.old_front.value
        except AttributeError:
            raise ValueError('No items in queue')

    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            raise ValueError('No items in queue')
