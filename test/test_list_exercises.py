from src.list_exercises import (
    create_greeting_strings, multiply_by_num, find_github_admins,
    increment_even_numbers, find_greater_than_ten_divisible_by_three,
    find_numbers_containing_digit
)
import pytest


@pytest.mark.it(
    ("create_greeting_strings: when called with an empty list, function "
     "should return empty list"))
def test_create_greeting_strings_return_empty_list():
    assert create_greeting_strings([]) == []


@pytest.mark.it(
    ("create_greeting_strings: Function should create greeting for "
     "single name in list"))
def test_create_greeting_strings_greets_single_name_in_list():
    assert create_greeting_strings(['Danika']) == ['Hello Danika!']


@pytest.mark.it(
    ("create_greeting_strings: Function should create greetings for "
     "all list elements"))
def test_create_greeting_strings_greets_all_names_in_list():
    test_list = ['Paul', 'Joe', 'Cat', 'Alex', 'Chon', 'Simon', 'Kyle']
    expected_result = [
        'Hello Paul!', 'Hello Joe!', 'Hello Cat!', 'Hello Alex!',
        'Hello Chon!', 'Hello Simon!', 'Hello Kyle!',
    ]
    assert create_greeting_strings(test_list) == expected_result


@pytest.mark.it(
    ("multiply_by_num: when called with an empty list, function should "
     "return empty list"))
def test_multiply_by_num_return_empty_list():
    assert multiply_by_num([], 1) == []


@pytest.mark.it(
    "multiply_by_num: Function should correctly multiply element in list")
def test_multiply_by_num_multiplies_single_element_in_list():
    assert multiply_by_num([5], 10) == [50]


@pytest.mark.it(
    "multiply_by_num: Function should correctly multiply all list elements")
def test_multiply_by_num_multiplies_all_list_elements():
    test_list = [1, 2, 3, 4, 5]
    test_multiplier = 5
    assert multiply_by_num(test_list, test_multiplier) == [5, 10, 15, 20, 25]


@pytest.mark.skip()
@pytest.mark.it(
    ("find_github_admins: when called with an empty list, function should "
     "return empty list"))
def test_find_github_admins_return_empty_list():
    assert find_github_admins([]) == []


@pytest.mark.skip()
@pytest.mark.it(
    "find_github_admins: Function should return all github admins")
def test_find_github_admins_includes_all_admins():
    test_users = [{"first_name": 'Paul',
                   "last_name": 'Copley',
                   "location": 'Bolton',
                   "age": 22,
                   'favourite_language': 'JavaScript',
                   "github_admin": True},
                  {"first_name": 'Joe',
                   "last_name": 'Mulvey',
                   "location": 'Liverpool-ish',
                   "age": 21,
                   'favourite_language': 'Python',
                   "github_admin": True}]
    expected_output = [{"first_name": 'Paul',
                        "last_name": 'Copley',
                        "location": 'Bolton',
                        "age": 22,
                        'favourite_language': 'JavaScript',
                        "github_admin": True},
                       {"first_name": 'Joe',
                        "last_name": 'Mulvey',
                        "location": 'Liverpool-ish',
                        "age": 21,
                        'favourite_language': 'Python',
                        "github_admin": True}]
    assert find_github_admins(test_users) == expected_output


@pytest.mark.skip()
@pytest.mark.it(
    "find_github_admins: Function should filter out non-admins")
def test_find_github_admins_filters_out_non_admins():
    test_users = [{"first_name": 'Danika',
                   "last_name": 'Crawley',
                   "location": 'Stockport',
                   "age": 29,
                   'favourite_language': 'Bash',
                   "github_admin": False},
                  {"first_name": 'Alex',
                   "last_name": 'Swain',
                   "location": 'The South 🤮',
                   "age": 73,
                   'favourite_language': 'C Sharp',
                   "github_admin": False},
                  {"first_name": 'Cat',
                   "last_name": 'Hoang',
                   "location": 'Greater Manchester',
                   "age": 21,
                   'favourite_language': 'Python',
                   "github_admin": False}]
    expected_output = []
    assert find_github_admins(test_users) == expected_output


@pytest.mark.skip()
@pytest.mark.it(
    ("find_github_admins: Function correctly filters mixed list of admins "
     "and non-admins"))
def test_find_github_admins_correctly_filters_mixed_list():
    test_users = [{"first_name": 'Paul',
                   "last_name": 'Copley',
                   "location": 'Bolton',
                   "age": 22,
                   'favourite_language': 'JavaScript',
                   "github_admin": True},
                  {"first_name": 'Kyle',
                   "last_name": 'McPhail',
                   "location": 'Manchester',
                   "age": 21,
                   'favourite_language': 'Python',
                   "github_admin": False},
                  {"first_name": 'Chon',
                   "last_name": 'Lee',
                   "location": 'Manchester',
                   "age": 21,
                   'favourite_language': 'Python',
                   "github_admin": False},
                  {"first_name": 'Joe',
                   "last_name": 'Mulvey',
                   "location": 'Liverpool-ish',
                   "age": 21,
                   'favourite_language': 'Python',
                   "github_admin": True},
                  {"first_name": 'Simon',
                   "last_name": 'Jackson',
                   "location": 'Leeds',
                   "age": 21,
                   'favourite_language': 'Python',
                   "github_admin": False}]

    expected_output = [{"first_name": 'Paul',
                        "last_name": 'Copley',
                        "location": 'Bolton',
                        "age": 22,
                        'favourite_language': 'JavaScript',
                        "github_admin": True},
                       {"first_name": 'Joe',
                        "last_name": 'Mulvey',
                        "location": 'Liverpool-ish',
                        "age": 21,
                        'favourite_language': 'Python',
                        "github_admin": True}]
    assert find_github_admins(test_users) == expected_output


@pytest.mark.skip()
@pytest.mark.it(
    ("increment_even_numbers: when called with an empty list, function "
     "should return empty list"))
def test_increment_even_numbers_return_empty_list():
    assert increment_even_numbers([]) == []


@pytest.mark.skip()
@pytest.mark.it(
    ("increment_even_numbers: Function should increment list of even numbers"))
def test_increment_even_numbers_increments_even_numbers():
    assert increment_even_numbers([2, 4, 6]) == [3, 5, 7]


@pytest.mark.skip()
@pytest.mark.it("increment_even_numbers: Function should ignore odd numbers")
def test_increment_even_numbers_ignores_odd_numbers():
    assert increment_even_numbers([1, 3, 5]) == [1, 3, 5]


@pytest.mark.skip()
@pytest.mark.it(
    ("increment_even_numbers: Function correctly applies "
        "incrementation to even numbers in mixed list"))
def test_increment_even_numbers_mixed_even_and_odd():
    assert increment_even_numbers([1, 2, 3, 4, 5]) == [1, 3, 3, 5, 5]


@pytest.mark.skip()
@pytest.mark.it(
    ("find_greater_than_ten_divisible_by_three: when called with an "
        " empty list, function should return empty list"))
def test_find_greater_than_ten_divisible_by_three_empty_list():
    assert find_greater_than_ten_divisible_by_three([]) == []


@pytest.mark.skip()
@pytest.mark.it(
    ("find_greater_than_ten_divisible_by_three: Function filters out numbers "
        "that don't meet the criteria"))
def test_find_greater_than_ten_divisible_by_three_non_matching_criteria():
    assert find_greater_than_ten_divisible_by_three(
        [1, 5, 9, 16, 22, 100]) == []


@pytest.mark.skip()
@pytest.mark.it(
    ("find_greater_than_ten_divisible_by_three: Function should return numbers"
        " that meet the criteria"))
def test_find_greater_than_ten_divisible_by_three_all_matching_criteria():
    assert find_greater_than_ten_divisible_by_three([15, 21, 60, 120]) == [
        15, 21, 60, 120]


@pytest.mark.skip()
@pytest.mark.it(
    ("find_greater_than_ten_divisible_by_three: Function correctly filters "
        "a mixed list of numbers"))
def test_find_greater_than_ten_divisible_by_three_mixed_list():
    test_list = [1, 45, 87, 3, 150, 276, 7155, 230, 1000, 7]
    expected_result = [45, 87, 150, 276, 7155]
    assert find_greater_than_ten_divisible_by_three(
        test_list) == expected_result


@pytest.mark.skip()
@pytest.mark.it(
    ("find_numbers_containing_digit: when called with an empty list, function "
        "should return empty list"))
def test_find_numbers_containing_digit_empty_list():
    assert find_numbers_containing_digit([], 1) == []


@pytest.mark.skip()
@pytest.mark.it(
    ("find_numbers_containing_digit: Function filters out numbers that don't "
        "contain the given digit"))
def test_find_numbers_containing_digit_non_matching_criteria():
    assert find_numbers_containing_digit([123, 231, 312], 5) == []


@pytest.mark.skip()
@pytest.mark.it(
    ("find_numbers_containing_digit: Function should return numbers that meet "
        "the criteria"))
def test_find_numbers_containing_digit_all_matching_criteria():
    assert find_numbers_containing_digit([15, 50, 555], 5) == [15, 50, 555]


@pytest.mark.skip()
@pytest.mark.it(
    ("find_numbers_containing_digit: Function correctly filters "
        "a mixed list of numbers"))
def test_find_numbers_containing_digit_mixed_list():
    test_list = [13, 72, 932, 127, 7052, 1926, 1027426, 920198382]
    expected_result = [72, 127, 7052, 1027426]
    assert find_numbers_containing_digit(test_list, 7) == expected_result
