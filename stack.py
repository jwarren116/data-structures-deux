#!/usr/bin/env python

'''Implementation of a simple stack data structure.
The stack has push, pop, and peek methods. Items in the stack have a value,
and next_item attribute. The stack has a top attribute.
'''


class Item(object):
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


class Stack(object):
    def __init__(self, top=None):
        self.top = top
