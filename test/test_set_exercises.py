from src.set_exercises import (
    get_unique_departments, get_unique_words
)
import pytest


@pytest.mark.it(
    "get_unique_departments: given empty list of employees, "
    "function should return empty collection")
def test_get_unique_departments():
    assert len(get_unique_departments([])) == 0


@pytest.mark.it((
    "get_unique_departments: given list containing single employee, function "
    "returns collection containing single element"))
def test_get_unique_departments_single():
    output = get_unique_departments([
        {
            "name": "Simon",
            "department": "HR"
        }
    ])

    assert 'HR' in output
    assert len(output) == 1


@pytest.mark.it((
    "get_unique_departments: given list containing multiple employees "
    "belonging to different departments, function returns collection with "
    "multiple unique elements"))
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


@pytest.mark.it((
    "get_unique_departments: given list containing multiple employees "
    "belonging to the same department, function returns collection with "
    "single element"))
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


@pytest.mark.it((
    "get_unique_departments: given list containing multiple employees "
    "belonging to the multiple departments, function returns collection with "
    "unique departments only"))
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


@pytest.mark.skip()
@pytest.mark.it(
    ("get_unique_words: given empty list of words, function should return "
     "empty collection"))
def test_get_unique_words():
    assert len(get_unique_words([])) == 0


@pytest.mark.skip()
@pytest.mark.it((
    "get_unique_words: given list containing single word, function returns "
    "collection with single element"))
def test_get_unique_words_single_word():
    output = get_unique_words(["hello"])

    assert 'hello' in output
    assert len(output) == 1


@pytest.mark.skip()
@pytest.mark.it((
    "get_unique_words: given list containing multiple unique words, function "
    "returns collection with multiple unique elements"))
def test_get_unique_words_multiple_unique_words():
    output = get_unique_words(["hello", "world", "goodbye"])

    assert all(el in output for el in ["hello", "world", "goodbye"])
    assert len(output) == 3


@pytest.mark.skip()
@pytest.mark.it((
    "get_unique_words: given list containing multiple duplicate words, "
    "function returns collection with single element"))
def test_get_unique_words_multiple_duplicate_words():
    output = get_unique_words(["hello", "world", "hello", "world"])

    assert 'hello' in output
    assert 'world' in output
    assert len(output) == 2


@pytest.mark.skip()
@pytest.mark.it((
    "get_unique_words: given list containing multiple of the same word with "
    "different casing, function should return a single word in lowercase"))
def test_get_unique_words_multiple_same_word_different_casing():
    output = get_unique_words(["Hello", "hello", "HELLO", "HeLLo"])

    assert 'hello' in output
    assert len(output) == 1


@pytest.mark.skip()
@pytest.mark.it((
    "get_unique_words: given list containing mixture of words - some unique, "
    "some the same with different casing, function should return collection "
    "containing only unique words in lowercase"))
def test_get_unique_words_multiple_mixed_words():
    output = get_unique_words(
        ["Hello", "hello", "HELLO", "HeLLo", "woRld", "goodbye", "GoOdbYe"])

    assert all(el in output for el in ["hello", "world", "goodbye"])
    assert len(output) == 3
