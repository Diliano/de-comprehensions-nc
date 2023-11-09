from src.nested_comprehension_exercises import (
    flatten_list, create_square_matrix
)
import pytest


@pytest.mark.it((
    "flatten_list: when called with empty list, function returns empty list"))
def test_flatten_list_empty_list():
    assert flatten_list([]) == []


# @pytest.mark.skip()
@pytest.mark.it((
    "flatten_list: when called with list containing single list, function "
    "returns flattened list"))
def test_flatten_list_single_nested_list():
    assert flatten_list([[1, 2, 3]]) == [1, 2, 3]


# @pytest.mark.skip()
@pytest.mark.it((
    "flatten_list: when called with list containing multiple single element "
    "lists, function returns flattened list"))
def test_flatten_list_multiple_nested_single_element_lists():
    assert flatten_list([[1], [2], [3]]) == [1, 2, 3]


# @pytest.mark.skip()
@pytest.mark.it((
    "flatten_list: when called with list containing multiple nested lists "
    "of the same length, function returns flattened list"))
def test_flatten_list_multiple_nested_lists_of_same_length():
    assert flatten_list([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9]


# @pytest.mark.skip()
@pytest.mark.it((
    "flatten_list: when called with list containing multiple nested lists of"
    " different lengths, function returns flattened list"))
def test_flatten_list_multiple_nested_lists_of_different_length():
    def test_flatten_list_multiple_nested_lists_of_different_length():
        assert flatten_list([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [
            1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert flatten_list([[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]) == [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert flatten_list([
            [1, 2, 3, 4], [5, 6, 7], [8, 9, 10, 11, 12]]) == [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        assert flatten_list([
            [1, 2, 3, 4, 5], [6, 7, 8], [9, 10, 11, 12, 13, 14]]) == [
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


@pytest.mark.skip()
@pytest.mark.it((
    "create_square_matrix: when called with 0, function returns empty list"))
def test_create_square_matrix_empty_matrix():
    assert create_square_matrix(0) == []


@pytest.mark.skip()
@pytest.mark.it((
    "create_square_matrix: when called with a 1, function returns matrix of length 1"
))
def test_create_square_matrix_1():
    assert create_square_matrix(1) == [[1]]


@pytest.mark.skip()
@pytest.mark.it((
    "create_square_matrix: when called with a number >= 2, function returns matrix "
    "of appropriate length"))
def test_create_square_matrix_larger_matrix():
    assert create_square_matrix(2) == [[1, 2], [1, 2]]
    assert create_square_matrix(3) == [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    assert create_square_matrix(4) == [
        [1, 2, 3, 4], [1, 2, 3, 4],
        [1, 2, 3, 4], [1, 2, 3, 4]]


@pytest.mark.skip()
@pytest.mark.it((
    "create_square_matrix: function should be able to accept an optional argument "
    "specifying the number to start from"))
def test_create_square_matrix_start_from():
    assert create_square_matrix(2, start=3) == [[3, 4], [3, 4]]
    assert create_square_matrix(3, start=5) == [
        [5, 6, 7], [5, 6, 7], [5, 6, 7]]
    assert create_square_matrix(4, start=8) == [
        [8, 9, 10, 11], [8, 9, 10, 11],
        [8, 9, 10, 11], [8, 9, 10, 11]]
    assert create_square_matrix(5, start=12) == [
        [12, 13, 14, 15, 16], [12, 13, 14, 15, 16],
        [12, 13, 14, 15, 16], [12, 13, 14, 15, 16],
        [12, 13, 14, 15, 16]]


@pytest.mark.skip()
@pytest.mark.it((
    "create_square_matrix: function should be able to accept an optional argument "
    "specifying the number to increment by"))
def test_create_square_matrix_increment_by():
    assert create_square_matrix(2, step=3) == [[1, 4], [1, 4]]
    assert create_square_matrix(3, step=5) == [
        [1, 6, 11], [1, 6, 11], [1, 6, 11]]
    assert create_square_matrix(4, step=8) == [
        [1, 9, 17, 25], [1, 9, 17, 25],
        [1, 9, 17, 25], [1, 9, 17, 25]]


@pytest.mark.skip()
@pytest.mark.it((
    "create_square_matrix: function should be able to accept multiple optional "
    "arguments specifying the number to start from and increment by"))
def test_create_square_matrix_multiple_optional_arguments():
    assert create_square_matrix(2, start=3, step=2) == [[3, 5], [3, 5]]
    assert create_square_matrix(3, start=5, step=3) == [
        [5, 8, 11], [5, 8, 11], [5, 8, 11]]
    assert create_square_matrix(4, start=8, step=4) == [
        [8, 12, 16, 20], [8, 12, 16, 20],
        [8, 12, 16, 20], [8, 12, 16, 20]]
    assert create_square_matrix(5, start=12, step=5) == [
        [12, 17, 22, 27, 32], [12, 17, 22, 27, 32],
        [12, 17, 22, 27, 32], [12, 17, 22, 27, 32],
        [12, 17, 22, 27, 32]]
