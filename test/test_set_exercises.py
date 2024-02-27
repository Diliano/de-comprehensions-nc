from src.set_exercises import (
    get_unique_departments, get_unique_words
)
import pytest


# ~~~~ get_unique_departments ~~~~

def test_get_unique_departments():
    assert len(get_unique_departments([])) == 0


def test_get_unique_departments_single():
    output = get_unique_departments([
        {
            "name": "Simon",
            "department": "HR"
        }
    ])

    assert 'HR' in output
    assert len(output) == 1


def test_get_unique_departments_multiple_employee_unique_departments():
    output = get_unique_departments([
        {
            "name": "Simon",
            "department": "HR"
        },
        {
            "name": "Danika",
            "department": "IT Support"
        },
        {
            "name": "Cat",
            "department": "Marketing"
        }
    ])

    assert all(el in output for el in ["HR", "IT Support", "Marketing"])
    assert len(output) == 3


def test_get_unique_departments_multi_employee_single_department():
    output = get_unique_departments([
        {
            "name": "Simon",
            "department": "HR"
        },
        {
            "name": "Danika",
            "department": "HR"
        },
        {
            "name": "Cat",
            "department": "HR"
        }
    ])

    assert 'HR' in output
    assert len(output) == 1


def test_get_unique_departments_multi_employee_multi_department():
    output = get_unique_departments([
        {
            "name": "Simon",
            "department": "HR"
        },
        {
            "name": "Danika",
            "department": "IT Support"
        },
        {
            "name": "Cat",
            "department": "Marketing"
        },
        {
            "name": "Joe",
            "department": "Technology"
        },
        {
            "name": "Chon",
            "department": "HR"
        },
        {
            "name": "Kyle",
            "department": "IT Support"
        }
    ])

    assert all(el in output for el in [
               "HR", "IT Support", "Marketing", "Technology"])
    assert len(output) == 4


# ~~~~ get_unique_words ~~~~

@pytest.mark.skip()
def test_get_unique_words_no_words():
    assert len(get_unique_words([])) == 0


@pytest.mark.skip()
def test_get_unique_words_single_word():
    output = get_unique_words(["hello"])

    assert 'hello' in output
    assert len(output) == 1


@pytest.mark.skip()
def test_get_unique_words_multiple_unique_words():
    output = get_unique_words(["hello", "world", "goodbye"])

    assert all(el in output for el in ["hello", "world", "goodbye"])
    assert len(output) == 3


@pytest.mark.skip()
def test_get_unique_words_multiple_duplicate_words():
    output = get_unique_words(["hello", "world", "hello", "world"])

    assert 'hello' in output
    assert 'world' in output
    assert len(output) == 2


@pytest.mark.skip()
def test_get_unique_words_multiple_same_word_different_casing():
    output = get_unique_words(["Hello", "hello", "HELLO", "HeLLo"])

    assert 'hello' in output
    assert len(output) == 1


@pytest.mark.skip()
def test_get_unique_words_multiple_mixed_words():
    output = get_unique_words(
        ["Hello", "hello", "HELLO", "HeLLo", "woRld", "goodbye", "GoOdbYe"])

    assert all(el in output for el in ["hello", "world", "goodbye"])
    assert len(output) == 3
