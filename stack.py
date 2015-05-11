#!/usr/bin/env python

'''Implementation of a simple stack data structure.
The stack has push, pop, and peek methods. Items in the stack have a value,
and next_item attribute. The stack has a top attribute.
'''


class Item(object):
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item

    def __str__(self):
        return self.value


class Stack(object):
    def __init__(self, top=None):
        self.top = top

    def push(self, value):
        self.item = Item(value)
        self.item.next_item = self.top
        self.top = self.item

    def pop(self):
        try:
            self.pop_item = self.top
            self.top = self.pop_item.next_item
            return self.pop_item.value
        except AttributeError:
            raise ValueError('No items in stack')

    def peek(self):
        try:
            return self.top.value
        except AttributeError:
            raise ValueError('No items in stack')
