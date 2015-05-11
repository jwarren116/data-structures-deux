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


def test_multiple_stacks():
    stack1 = Stack()
    stack2 = Stack()
    stack1.push("1bacon")
    stack2.push("2bacon")
    stack2.push("2steak")
    stack1.push("1steak")
    assert stack2.pop() == "2steak"
    assert stack1.pop() == "1steak"
    stack2.push("2cheese")
    assert stack1.pop() == "1bacon"
