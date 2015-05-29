from hash_table import HashTable
import io
import pytest


words = []

with io.open('/usr/share/dict/words', 'r') as word_file:
    words = word_file.readlines()


def test_init():
    ht = HashTable()
    assert len(ht.table) == 1024
    ht2 = HashTable(10000)
    assert len(ht2.table) == 10000


def test_hash():
    ht = HashTable()
    ht.set('coffee', 'coffee')
    assert ht.get('coffee') == 'coffee'


def test_duplicate_hash_val():
    ht = HashTable()
    ht.set('bob', 'bob')
    ht.set('obb', 'obb')
    assert ht.get('bob') == 'bob'
    assert ht.get('obb') == 'obb'


def test_word_file():
    ht = HashTable()
    for word in words:
        ht.set(word, word)
    assert ht.get(words[654]) == words[654]
    assert ht.get(words[3541]) == words[3541]
    assert ht.get(words[6541]) == words[6541]


def test_non_item():
    ht = HashTable()
    ht.set('coffee', 'coffee')
    with pytest.raises(KeyError):
        ht.get('milk')


def test_non_bucket():
    ht = HashTable()
    with pytest.raises(IndexError):
        ht.table[1025]


def test_non_string():
    ht = HashTable()
    with pytest.raises(TypeError):
        ht.set(13, 13)


def test_multiple_tables():
    ht1 = HashTable()
    ht2 = HashTable()
    ht1.set('coffee', 'coffee')
    ht1.set('eggs', 'eggs')
    ht2.set('bacon', 'bacon')
    with pytest.raises(KeyError):
        ht1.get('bacon')
    with pytest.raises(KeyError):
        ht2.get('coffee')
