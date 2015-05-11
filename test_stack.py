from stack import Stack
import pytest


def test_stack_push():
    stack = Stack()
    stack.push("bacon")
    assert stack.top.value == "bacon"
    assert stack.peek() == "bacon"


def test_stack_push_multi():
    stack = Stack()
    stack.push("bacon")
    stack.push("steak")
    stack.push("grilled cheese")
    assert stack.pop() == "grilled cheese"
    assert stack.pop() == "steak"
    assert stack.pop() == "bacon"


def test_empty_stack_pop():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.pop()


def test_empty_stack_peek():
    stack = Stack()
    with pytest.raises(ValueError):
        stack.peek()
