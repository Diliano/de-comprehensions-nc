from src.nested_comprehension_exercises import (
    flatten_list, create_square_matrix
)
import pytest


# ~~~~ flatten_list ~~~~

@pytest.mark.skip()
def test_flatten_list_empty_list():
    assert flatten_list([]) == []


@pytest.mark.skip()
def test_flatten_list_single_nested_list():
    assert flatten_list([[1, 2, 3]]) == [1, 2, 3]


@pytest.mark.skip()
def test_flatten_list_multiple_nested_single_element_lists():
    assert flatten_list([[1], [2], [3]]) == [1, 2, 3]


@pytest.mark.skip()
def test_flatten_list_multiple_nested_lists_of_same_length():
    assert flatten_list([[1, 2], [3, 4], [5, 6]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1, 2, 3, 4, 5, 6, 7, 8, 9]


@pytest.mark.skip()
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


# ~~~~ create_square_matrix ~~~~

@pytest.mark.skip()
def test_create_square_matrix_empty_matrix():
    assert create_square_matrix(0) == []


@pytest.mark.skip()
def test_create_square_matrix_1():
    assert create_square_matrix(1) == [[1]]


@pytest.mark.skip()
def test_create_square_matrix_larger_matrix():
    assert create_square_matrix(2) == [[1, 2], [1, 2]]
    assert create_square_matrix(3) == [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    assert create_square_matrix(4) == [
        [1, 2, 3, 4], [1, 2, 3, 4],
        [1, 2, 3, 4], [1, 2, 3, 4]]


@pytest.mark.skip()
def test_create_square_matrix_start_arg():
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
def test_create_square_matrix_step_arg():
    assert create_square_matrix(2, step=3) == [[1, 4], [1, 4]]
    assert create_square_matrix(3, step=5) == [
        [1, 6, 11], [1, 6, 11], [1, 6, 11]]
    assert create_square_matrix(4, step=8) == [
        [1, 9, 17, 25], [1, 9, 17, 25],
        [1, 9, 17, 25], [1, 9, 17, 25]]


@pytest.mark.skip()
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
