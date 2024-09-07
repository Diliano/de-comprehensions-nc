from test_api.checks import run_test, skip_test, format_err_msg


def get_unique_departments(employees):
    return {staff["department"] for staff in employees}


@run_test
def test_get_unique_departments():
    assert len(get_unique_departments([])) == 0, format_err_msg(
        [], get_unique_departments([])
    )


@run_test
def test_get_unique_departments_single():
    output = get_unique_departments([{"name": "Simon", "department": "HR"}])

    assert "HR" in output, format_err_msg(True, "HR" in output)
    assert len(output) == 1, format_err_msg(1, len(output))


@run_test
def test_get_unique_departments_multiple_employee_unique_departments():
    output = get_unique_departments(
        [
            {"name": "Simon", "department": "HR"},
            {"name": "Danika", "department": "IT Support"},
            {"name": "Cat", "department": "Marketing"},
        ]
    )

    assert all(
        el in output for el in ["HR", "IT Support", "Marketing"]
    ), format_err_msg(
        True, all(el in output for el in ["HR", "IT Support", "Marketing"])
    )
    assert len(output) == 3, format_err_msg(3, len(output))


@run_test
def test_get_unique_departments_multi_employee_single_department():
    output = get_unique_departments(
        [
            {"name": "Simon", "department": "HR"},
            {"name": "Danika", "department": "HR"},
            {"name": "Cat", "department": "HR"},
        ]
    )

    assert "HR" in output, format_err_msg(True, "HR" in output)
    assert len(output) == 1, format_err_msg(1, len(output))


@run_test
def test_get_unique_departments_multi_employee_multi_department():
    output = get_unique_departments(
        [
            {"name": "Simon", "department": "HR"},
            {"name": "Danika", "department": "IT Support"},
            {"name": "Cat", "department": "Marketing"},
            {"name": "Joe", "department": "Technology"},
            {"name": "Chon", "department": "HR"},
            {"name": "Kyle", "department": "IT Support"},
        ]
    )

    assert all(
        el in output for el in ["HR", "IT Support", "Marketing", "Technology"]
    ), format_err_msg(
        True,
        all(
            el in output
            for el in ["HR", "IT Support", "Marketing", "Technology"]
        ),
    )
    assert len(output) == 4, format_err_msg(4, len(output))


def get_unique_words(words):
    return {word.lower() for word in words}


@run_test
def test_get_unique_words_no_words():
    assert len(get_unique_words([])) == 0, format_err_msg(
        [], get_unique_words([])
    )


@run_test
def test_get_unique_words_single_word():
    output = get_unique_words(["hello"])

    assert "hello" in output, format_err_msg(True, "hello" in output)
    assert len(output) == 1, format_err_msg(1, len(output))


@run_test
def test_get_unique_words_multiple_unique_words():
    output = get_unique_words(["hello", "world", "goodbye"])

    assert all(
        el in output for el in ["hello", "world", "goodbye"]
    ), format_err_msg(
        True, all(el in output for el in ["hello", "world", "goodbye"])
    )
    assert len(output) == 3, format_err_msg(3, len(output))


@run_test
def test_get_unique_words_multiple_duplicate_words():
    output = get_unique_words(["hello", "world", "hello", "world"])

    assert "hello" in output, format_err_msg(True, "hello" in output)
    assert "world" in output, format_err_msg(True, "world" in output)
    assert len(output) == 2, format_err_msg(2, len(output))


@run_test
def test_get_unique_words_multiple_same_word_different_casing():
    output = get_unique_words(["Hello", "hello", "HELLO", "HeLLo"])

    assert "hello" in output, format_err_msg(True, "hello" in output)
    assert len(output) == 1, format_err_msg(1, len(output))


@run_test
def test_get_unique_words_multiple_mixed_words():
    output = get_unique_words(
        ["Hello", "hello", "HELLO", "HeLLo", "woRld", "goodbye", "GoOdbYe"]
    )

    assert all(
        el in output for el in ["hello", "world", "goodbye"]
    ), format_err_msg(
        True, all(el in output for el in ["hello", "world", "goodbye"])
    )
    assert len(output) == 3, format_err_msg(3, len(output))


if __name__ == "__main__":
    test_get_unique_departments()
    test_get_unique_departments_single()
    test_get_unique_departments_multiple_employee_unique_departments()
    test_get_unique_departments_multi_employee_single_department()
    test_get_unique_departments_multi_employee_multi_department()
    test_get_unique_words_no_words()
    test_get_unique_words_single_word()
    test_get_unique_words_multiple_unique_words()
    test_get_unique_words_multiple_duplicate_words()
    test_get_unique_words_multiple_same_word_different_casing()
    test_get_unique_words_multiple_mixed_words()
