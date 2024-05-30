from test_api.checks import run_test, skip_test, format_err_msg


def create_greeting_strings(names):
    greeting = []

    for name in names:
        greeting.append(f"Hello {name}!")

    return greeting


@run_test
def test_create_greeting_strings_return_empty_list():
    assert create_greeting_strings([]) == [], format_err_msg(
        "", create_greeting_strings([])
    )


@skip_test
def test_create_greeting_strings_greets_single_name_in_list():
    assert create_greeting_strings(["Danika"]) == [
        "Hello Danika!"
    ], format_err_msg("Hello Danika!", create_greeting_strings(["Danika"]))


@skip_test
def test_create_greeting_strings_greets_all_names_in_list():
    test_list = ["Paul", "Joe", "Cat", "Alex", "Chon", "Simon", "Kyle"]
    expected_result = [
        "Hello Paul!",
        "Hello Joe!",
        "Hello Cat!",
        "Hello Alex!",
        "Hello Chon!",
        "Hello Simon!",
        "Hello Kyle!",
    ]
    assert (
        create_greeting_strings(test_list) == expected_result
    ), format_err_msg(expected_result, create_greeting_strings(test_list))


def multiply_by_num(num_list, multiplier):
    multiplied_nums = []

    for num in num_list:
        multiplied_nums.append(num * multiplier)

    return multiplied_nums


@skip_test
def test_multiply_by_num_return_empty_list():
    assert multiply_by_num([], 1) == [], format_err_msg(
        [], multiply_by_num([], 1)
    )


@skip_test
def test_multiply_by_num_multiplies_single_element_in_list():
    assert multiply_by_num([5], 10) == [50], format_err_msg(
        [50], multiply_by_num([5], 10)
    )


@skip_test
def test_multiply_by_num_multiplies_all_list_elements():
    test_list = [1, 2, 3, 4, 5]
    test_multiplier = 5
    assert multiply_by_num(test_list, test_multiplier) == [
        5,
        10,
        15,
        20,
        25,
    ], format_err_msg(
        [5, 10, 15, 20, 25], multiply_by_num(test_list, test_multiplier)
    )


def find_github_admins(users):
    pass


@skip_test
def test_find_github_admins_return_empty_list():
    assert find_github_admins([]) == [], format_err_msg(
        [], find_github_admins([])
    )


@skip_test
def test_find_github_admins_includes_all_admins():
    test_users = [
        {
            "first_name": "Paul",
            "last_name": "Copley",
            "location": "Bolton",
            "age": 22,
            "favourite_language": "JavaScript",
            "github_admin": True,
        },
        {
            "first_name": "Joe",
            "last_name": "Mulvey",
            "location": "Liverpool-ish",
            "age": 21,
            "favourite_language": "Python",
            "github_admin": True,
        },
    ]
    expected_output = [
        {
            "first_name": "Paul",
            "last_name": "Copley",
            "location": "Bolton",
            "age": 22,
            "favourite_language": "JavaScript",
            "github_admin": True,
        },
        {
            "first_name": "Joe",
            "last_name": "Mulvey",
            "location": "Liverpool-ish",
            "age": 21,
            "favourite_language": "Python",
            "github_admin": True,
        },
    ]
    assert find_github_admins(test_users) == expected_output, format_err_msg(
        expected_output, find_github_admins(test_users)
    )


@skip_test
def test_find_github_admins_filters_out_non_admins():
    test_users = [
        {
            "first_name": "Danika",
            "last_name": "Crawley",
            "location": "Stockport",
            "age": 29,
            "favourite_language": "Bash",
            "github_admin": False,
        },
        {
            "first_name": "Alex",
            "last_name": "Swain",
            "location": "The South 🤮",
            "age": 73,
            "favourite_language": "C Sharp",
            "github_admin": False,
        },
        {
            "first_name": "Cat",
            "last_name": "Hoang",
            "location": "Greater Manchester",
            "age": 21,
            "favourite_language": "Python",
            "github_admin": False,
        },
    ]
    expected_output = []
    assert find_github_admins(test_users) == expected_output, format_err_msg(
        expected_output, find_github_admins(test_users)
    )


@skip_test
def test_find_github_admins_correctly_filters_mixed_list():
    test_users = [
        {
            "first_name": "Paul",
            "last_name": "Copley",
            "location": "Bolton",
            "age": 22,
            "favourite_language": "JavaScript",
            "github_admin": True,
        },
        {
            "first_name": "Kyle",
            "last_name": "McPhail",
            "location": "Manchester",
            "age": 21,
            "favourite_language": "Python",
            "github_admin": False,
        },
        {
            "first_name": "Chon",
            "last_name": "Lee",
            "location": "Manchester",
            "age": 21,
            "favourite_language": "Python",
            "github_admin": False,
        },
        {
            "first_name": "Joe",
            "last_name": "Mulvey",
            "location": "Liverpool-ish",
            "age": 21,
            "favourite_language": "Python",
            "github_admin": True,
        },
        {
            "first_name": "Simon",
            "last_name": "Jackson",
            "location": "Leeds",
            "age": 21,
            "favourite_language": "Python",
            "github_admin": False,
        },
    ]

    expected_output = [
        {
            "first_name": "Paul",
            "last_name": "Copley",
            "location": "Bolton",
            "age": 22,
            "favourite_language": "JavaScript",
            "github_admin": True,
        },
        {
            "first_name": "Joe",
            "last_name": "Mulvey",
            "location": "Liverpool-ish",
            "age": 21,
            "favourite_language": "Python",
            "github_admin": True,
        },
    ]
    assert find_github_admins(test_users) == expected_output, format_err_msg(
        expected_output, find_github_admins(test_users)
    )


def increment_even_numbers(number_list):
    pass


@skip_test
def test_increment_even_numbers_return_empty_list():
    assert increment_even_numbers([]) == [], format_err_msg(
        [], increment_even_numbers([])
    )


@skip_test
def test_increment_even_numbers_increments_even_numbers():
    assert increment_even_numbers([2, 4, 6]) == [3, 5, 7], format_err_msg(
        [3, 5, 7], increment_even_numbers([2, 4, 6])
    )


@skip_test
def test_increment_even_numbers_ignores_odd_numbers():
    assert increment_even_numbers([1, 3, 5]) == [1, 3, 5], format_err_msg(
        [1, 3, 5], increment_even_numbers([1, 3, 5])
    )


@skip_test
def test_increment_even_numbers_mixed_even_and_odd():
    assert increment_even_numbers([1, 2, 3, 4, 5]) == [
        1,
        3,
        3,
        5,
        5,
    ], format_err_msg([1, 3, 3, 5, 5], increment_even_numbers([1, 2, 3, 4, 5]))


def find_greater_than_ten_divisible_by_three(number_list):
    pass


@skip_test
def test_find_greater_than_ten_divisible_by_three_empty_list():
    assert find_greater_than_ten_divisible_by_three([]) == [], format_err_msg(
        [], find_greater_than_ten_divisible_by_three([])
    )


@skip_test
def test_find_greater_than_ten_divisible_by_three_non_matching_criteria():
    assert (
        find_greater_than_ten_divisible_by_three([1, 5, 9, 16, 22, 100]) == []
    ), format_err_msg(
        [], find_greater_than_ten_divisible_by_three([1, 5, 9, 16, 22, 100])
    )


@skip_test
def test_find_greater_than_ten_divisible_by_three_all_matching_criteria():
    assert find_greater_than_ten_divisible_by_three([15, 21, 60, 120]) == [
        15,
        21,
        60,
        120,
    ], format_err_msg(
        [15, 21, 60, 120],
        find_greater_than_ten_divisible_by_three([15, 21, 60, 120]),
    )


@skip_test
def test_find_greater_than_ten_divisible_by_three_mixed_list():
    test_list = [1, 45, 87, 3, 150, 276, 7155, 230, 1000, 7]
    expected_result = [45, 87, 150, 276, 7155]
    assert (
        find_greater_than_ten_divisible_by_three(test_list) == expected_result
    ), format_err_msg(
        expected_result, find_greater_than_ten_divisible_by_three(test_list)
    )


def find_numbers_containing_digit(number_list, digit):
    pass


@skip_test
def test_find_numbers_containing_digit_empty_list():
    assert find_numbers_containing_digit([], 1) == [], format_err_msg(
        [], find_numbers_containing_digit([], 1)
    )


@skip_test
def test_find_numbers_containing_digit_non_matching_criteria():
    assert (
        find_numbers_containing_digit([123, 231, 312], 5) == []
    ), format_err_msg([], find_numbers_containing_digit([123, 231, 312], 5))


@skip_test
def test_find_numbers_containing_digit_all_matching_criteria():
    assert find_numbers_containing_digit([15, 50, 555], 5) == [
        15,
        50,
        555,
    ], format_err_msg(
        [15, 50, 555], find_numbers_containing_digit([15, 50, 555], 5)
    )


@skip_test
def test_find_numbers_containing_digit_mixed_list():
    test_list = [13, 72, 932, 127, 7052, 1926, 1027426, 920198382]
    expected_result = [72, 127, 7052, 1027426]
    assert (
        find_numbers_containing_digit(test_list, 7) == expected_result
    ), format_err_msg(
        expected_result, find_numbers_containing_digit(test_list, 7)
    )


if __name__ == "__main__":
    test_create_greeting_strings_return_empty_list()
    test_create_greeting_strings_greets_single_name_in_list()
    test_create_greeting_strings_greets_all_names_in_list()
    test_multiply_by_num_return_empty_list()
    test_multiply_by_num_multiplies_single_element_in_list()
    test_multiply_by_num_multiplies_all_list_elements()
    test_find_github_admins_return_empty_list()
    test_find_github_admins_includes_all_admins()
    test_find_github_admins_filters_out_non_admins()
    test_find_github_admins_correctly_filters_mixed_list()
    test_increment_even_numbers_return_empty_list()
    test_increment_even_numbers_increments_even_numbers()
    test_increment_even_numbers_ignores_odd_numbers()
    test_increment_even_numbers_mixed_even_and_odd()
    test_find_greater_than_ten_divisible_by_three_empty_list()
    test_find_greater_than_ten_divisible_by_three_non_matching_criteria()
    test_find_greater_than_ten_divisible_by_three_all_matching_criteria()
    test_find_greater_than_ten_divisible_by_three_mixed_list()
    test_find_numbers_containing_digit_empty_list()
    test_find_numbers_containing_digit_non_matching_criteria()
    test_find_numbers_containing_digit_all_matching_criteria()
    test_find_numbers_containing_digit_mixed_list()
