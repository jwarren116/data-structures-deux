from queue import Queue
import pytest


def test_enqueue_front():
    queue = Queue()
    queue.enqueue("Bacon")
    assert queue.back.value == "Bacon"


def test_enqueue_multi_back():
    queue = Queue()
    queue.enqueue("Bacon")
    queue.enqueue("Steak")
    queue.enqueue("Beer")
    assert queue.back.value == "Beer"


def test_dequeue_empty():
    queue = Queue()
    with pytest.raises(ValueError):
        queue.dequeue()


def test_dequeue():
    queue = Queue()
    queue.enqueue("Bacon")
    assert queue.dequeue() == "Bacon"
    with pytest.raises(ValueError):
        queue.peek()


def test_dequeue_multi():
    queue = Queue()
    queue.enqueue("Bacon")
    queue.enqueue("Beer")
    assert queue.dequeue() == "Bacon"
    assert queue.front.value == "Beer"


def test_size_with_remove():
    queue = Queue()
    queue.enqueue("Bacon")
    queue.enqueue("Beer")
    queue.enqueue("Cow")
    queue.enqueue("Whiskey")
    assert queue.dequeue() == "Bacon"
    assert queue.peek() == "Beer"
