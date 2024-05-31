from test_api.checks import run_test, skip_test, format_err_msg


def flatten_list(nested_list):
    flattened_list = []

    for sub_list in nested_list:
        for el in sub_list:
            flattened_list.append(el)

    return flattened_list


@run_test
def test_flatten_list_empty_list():
    assert flatten_list([]) == [], format_err_msg([], flatten_list([]))


@skip_test
def test_flatten_list_single_nested_list():
    assert flatten_list([[1, 2, 3]]) == [1, 2, 3], format_err_msg(
        [1, 2, 3], flatten_list([[1, 2, 3]])
    )


@skip_test
def test_flatten_list_multiple_nested_single_element_lists():
    assert flatten_list([[1], [2], [3]]) == [1, 2, 3], format_err_msg(
        [1, 2, 3], flatten_list([[1], [2], [3]])
    )


@skip_test
def test_flatten_list_multiple_nested_lists_of_same_length():
    assert flatten_list([[1, 2], [3, 4], [5, 6]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
    ], format_err_msg(
        [1, 2, 3, 4, 5, 6], flatten_list([[1, 2], [3, 4], [5, 6]])
    )
    assert flatten_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ], format_err_msg(
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        flatten_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    )


@skip_test
def test_flatten_list_multiple_nested_lists_of_different_length():
    assert flatten_list([[1, 2], [3, 4, 5], [6, 7, 8, 9]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
    ], format_err_msg(
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        flatten_list([[1, 2], [3, 4, 5], [6, 7, 8, 9]]),
    )
    assert flatten_list([[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
    ], format_err_msg(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        flatten_list([[1, 2, 3], [4, 5], [6, 7, 8, 9, 10]]),
    )
    assert flatten_list([[1, 2, 3, 4], [5, 6, 7], [8, 9, 10, 11, 12]]) == [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
    ], format_err_msg(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        flatten_list([[1, 2, 3, 4], [5, 6, 7], [8, 9, 10, 11, 12]]),
    )
    assert flatten_list(
        [[1, 2, 3, 4, 5], [6, 7, 8], [9, 10, 11, 12, 13, 14]]
    ) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], format_err_msg(
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        flatten_list([[1, 2, 3, 4, 5], [6, 7, 8], [9, 10, 11, 12, 13, 14]]),
    )


def create_square_matrix(num):
    pass


@run_test
def test_create_square_matrix_empty_matrix():
    assert create_square_matrix(0) == [], format_err_msg(
        [], create_square_matrix(0)
    )


@skip_test
def test_create_square_matrix_1():
    assert create_square_matrix(1) == [[1]], format_err_msg(
        [[1]], create_square_matrix(1)
    )


@skip_test
def test_create_square_matrix_larger_matrix():
    assert create_square_matrix(2) == [[1, 2], [1, 2]], format_err_msg(
        [[1, 2], [1, 2]], create_square_matrix(2)
    )
    assert create_square_matrix(3) == [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3],
    ], format_err_msg(
        [[1, 2, 3], [1, 2, 3], [1, 2, 3]], create_square_matrix(3)
    )
    assert create_square_matrix(4) == [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4],
    ], format_err_msg(
        [[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]],
        create_square_matrix(4),
    )


@skip_test
def test_create_square_matrix_start_arg():
    assert create_square_matrix(2, start=3) == [
        [3, 4],
        [3, 4],
    ], format_err_msg([[3, 4], [3, 4]], create_square_matrix(2, start=3))
    assert create_square_matrix(3, start=5) == [
        [5, 6, 7],
        [5, 6, 7],
        [5, 6, 7],
    ], format_err_msg(
        [[5, 6, 7], [5, 6, 7], [5, 6, 7]], create_square_matrix(3, start=5)
    )
    assert create_square_matrix(4, start=8) == [
        [8, 9, 10, 11],
        [8, 9, 10, 11],
        [8, 9, 10, 11],
        [8, 9, 10, 11],
    ], format_err_msg(
        [[8, 9, 10, 11], [8, 9, 10, 11], [8, 9, 10, 11], [8, 9, 10, 11]],
        create_square_matrix(4, start=8),
    )
    assert create_square_matrix(5, start=12) == [
        [12, 13, 14, 15, 16],
        [12, 13, 14, 15, 16],
        [12, 13, 14, 15, 16],
        [12, 13, 14, 15, 16],
        [12, 13, 14, 15, 16],
    ], format_err_msg(
        [
            [12, 13, 14, 15, 16],
            [12, 13, 14, 15, 16],
            [12, 13, 14, 15, 16],
            [12, 13, 14, 15, 16],
            [12, 13, 14, 15, 16],
        ],
        create_square_matrix(5, start=12),
    )


@skip_test
def test_create_square_matrix_step_arg():
    assert create_square_matrix(2, step=3) == [[1, 4], [1, 4]], format_err_msg(
        [[1, 4], [1, 4]], create_square_matrix(2, step=3)
    )
    assert create_square_matrix(3, step=5) == [
        [1, 6, 11],
        [1, 6, 11],
        [1, 6, 11],
    ], format_err_msg(
        [[1, 6, 11], [1, 6, 11], [1, 6, 11]], create_square_matrix(3, step=5)
    )
    assert create_square_matrix(4, step=8) == [
        [1, 9, 17, 25],
        [1, 9, 17, 25],
        [1, 9, 17, 25],
        [1, 9, 17, 25],
    ], format_err_msg(
        [[1, 9, 17, 25], [1, 9, 17, 25], [1, 9, 17, 25], [1, 9, 17, 25]],
        create_square_matrix(4, step=8),
    )


@skip_test
def test_create_square_matrix_multiple_optional_arguments():
    assert create_square_matrix(2, start=3, step=2) == [
        [3, 5],
        [3, 5],
    ], format_err_msg(
        [[3, 5], [3, 5]], create_square_matrix(2, start=3, step=2)
    )
    assert create_square_matrix(3, start=5, step=3) == [
        [5, 8, 11],
        [5, 8, 11],
        [5, 8, 11],
    ], format_err_msg(
        [[5, 8, 11], [5, 8, 11], [5, 8, 11]],
        create_square_matrix(3, start=5, step=3),
    )
    assert create_square_matrix(4, start=8, step=4) == [
        [8, 12, 16, 20],
        [8, 12, 16, 20],
        [8, 12, 16, 20],
        [8, 12, 16, 20],
    ], format_err_msg(
        [[8, 12, 16, 20], [8, 12, 16, 20], [8, 12, 16, 20], [8, 12, 16, 20]],
        create_square_matrix(4, start=8, step=4),
    )
    assert create_square_matrix(5, start=12, step=5) == [
        [12, 17, 22, 27, 32],
        [12, 17, 22, 27, 32],
        [12, 17, 22, 27, 32],
        [12, 17, 22, 27, 32],
        [12, 17, 22, 27, 32],
    ], format_err_msg(
        [
            [12, 17, 22, 27, 32],
            [12, 17, 22, 27, 32],
            [12, 17, 22, 27, 32],
            [12, 17, 22, 27, 32],
            [12, 17, 22, 27, 32],
        ],
        create_square_matrix(5, start=12, step=5),
    )


if __name__ == "__main__":
    test_flatten_list_empty_list()
    test_flatten_list_single_nested_list()
    test_flatten_list_multiple_nested_single_element_lists()
    test_flatten_list_multiple_nested_lists_of_same_length()
    test_flatten_list_multiple_nested_lists_of_different_length()
    test_create_square_matrix_empty_matrix()
    test_create_square_matrix_1()
    test_create_square_matrix_larger_matrix()
    test_create_square_matrix_start_arg()
    test_create_square_matrix_step_arg()
    test_create_square_matrix_multiple_optional_arguments()
