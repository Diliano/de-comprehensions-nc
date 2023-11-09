from src.dict_exercises import (
    find_word_lengths, switch_name_and_id, create_multiplication_table,
    square_numbers, find_average_games
)
import pytest


@pytest.mark.it(
    ("find_word_lengths: when called with empty list, function should "
     "return empty dict"))
def test_find_word_lengths_returns_empty_dict():
    assert find_word_lengths([]) == {}


@pytest.mark.it(
    ("find_word_lengths: when called with list with single word, function "
     "should return dict with single key and value of word length"))
def test_find_word_lengths_returns_dict_with_single_key():
    assert find_word_lengths(["hello"]) == {"hello": 5}
    assert find_word_lengths(["goodbye"]) == {"goodbye": 7}
    assert find_word_lengths(["hi"]) == {"hi": 2}


@pytest.mark.it(
    ("find_word_lengths: when called with list with multiple words, "
     "function should return dict with keys of words and values of "
     "word lengths"))
def test_find_word_lengths_returns_dict_with_keys_and_values():
    assert find_word_lengths(["hello", "goodbye"]) == {
        "hello": 5, "goodbye": 7}
    assert find_word_lengths(["hi", "there"]) == {"hi": 2, "there": 5}
    assert find_word_lengths(["hey", "there", "you"]) == {
        "hey": 3, "there": 5, "you": 3}
    assert find_word_lengths(["hey", "there", "you", "are"]) == {
        "hey": 3, "there": 5, "you": 3, "are": 3}
    assert find_word_lengths(["hey", "there", "you", "are", "awesome"]) == {
        "hey": 3, "there": 5, "you": 3, "are": 3, "awesome": 7}
    assert find_word_lengths(["hey", "there", "you", "are", "awesome",
                              "and", "cool"]) == {
        "hey": 3, "there": 5, "you": 3, "are": 3, "awesome": 7, "and": 3,
        "cool": 4}


@pytest.mark.it(
    ("switch_name_and_id: when called with empty dictionary, function should "
     "return empty dictionary"))
def test_switch_name_and_id_returns_empty_dict():
    assert switch_name_and_id({}) == {}


@pytest.mark.it(
    ("switch_name_and_id: when called with dictionary with single key and "
     "value, function should return dictionary with value and key "
     "swapped around"))
def test_switch_name_and_id_returns_dict_with_single_swapped_key_and_value():
    assert switch_name_and_id({"Alex": "a7d29w"}) == {"a7d29w": "Alex"}
    assert switch_name_and_id({"Chon": "z2r51e"}) == {"z2r51e": "Chon"}
    assert switch_name_and_id({"Cat": "p3f44m"}) == {"p3f44m": "Cat"}


@pytest.mark.it(
    ("switch_name_and_id: when called with dictionary with multiple keys "
     "and values, function should return dictionary with keys and values "
     "swapped around"))
def test_switch_name_and_id_returns_dict_with_swapped_keys_and_values():
    assert switch_name_and_id({"Alex": "a7d29w", "Chon": "z2r51e"}) == {
        "a7d29w": "Alex", "z2r51e": "Chon"}
    assert switch_name_and_id(
        {"Simon": "a7d29w", "Joe": "z2r51e", "Paul": "p3f44m"}) == {
        "a7d29w": "Simon", "z2r51e": "Joe", "p3f44m": "Paul"}
    assert switch_name_and_id(
        {"Kyle": "a7d29w",
         "Danika": "z2r51e",
         "Liam": "p3f44m",
         "Cat": "q4r55t"}) == {
        "a7d29w": "Kyle",
        "z2r51e": "Danika",
        "p3f44m": "Liam",
        "q4r55t": "Cat"}


@pytest.mark.skip()
@pytest.mark.it(
    ("create_multiplication_table: when called with any number and a limit "
     "of 0, function should return empty dict"))
def test_create_multiplication_table_returns_empty_dict():
    assert create_multiplication_table(1, 0) == {}
    assert create_multiplication_table(5, 0) == {}
    assert create_multiplication_table(10, 0) == {}


@pytest.mark.skip()
@pytest.mark.it(
    ("create_multiplication_table: when called with any number and a limit "
     "of 1, function should return dict with single key and the value of "
     "given number"))
def test_create_multiplication_table_returns_dict_with_single_key():
    assert create_multiplication_table(1, 1) == {1: 1}
    assert create_multiplication_table(5, 1) == {1: 5}
    assert create_multiplication_table(10, 1) == {1: 10}


@pytest.mark.skip()
@pytest.mark.it(
    ("create_multiplication_table: when called with any number and a limit "
     "of greater than 1, function should return dict with keys from 1 to "
     "limit and values of multiplication of given number and keys"))
def test_create_multiplication_table_returns_dict_with_keys_from_1_to_limit():
    assert create_multiplication_table(1, 2) == {1: 1, 2: 2}
    assert create_multiplication_table(
        5, 5) == {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}
    assert create_multiplication_table(10, 10) == {
        1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90, 10: 100}


@pytest.mark.skip()
@pytest.mark.it(
    ("square_numbers: when called with empty list, function should return "
     "empty dictionary"))
def test_square_numbers_returns_empty_dict():
    assert square_numbers([]) == {}


@pytest.mark.skip()
@pytest.mark.it(
    ("square_numbers: when called with list with even numbers, function "
     "should return dictionary with keys and values of squared numbers"))
def test_square_numbers_returns_dict_with_single_key():
    assert square_numbers([10]) == {10: 100}
    assert square_numbers([10, 20]) == {10: 100, 20: 400}


@pytest.mark.skip()
@pytest.mark.it(
    ("square_numbers: when called with a list of odd numbers, function should "
     "return empty dict"))
def test_square_numbers_returns_empty_dict_when_invoked_with_odd_numbers():
    assert square_numbers([1]) == {}
    assert square_numbers([1, 3, 5, 7, 9]) == {}
    assert square_numbers([11, 13, 15, 17, 19]) == {}


@pytest.mark.skip()
@pytest.mark.it(
    ("square_numbers: when called with list with mixed list of odd and even "
     "number, function should only return squares of the even numbers"))
def test_square_numbers_mixed_list_of_odds_and_evens():
    assert square_numbers([1, 2, 3, 4, 5]) == {2: 4, 4: 16}
    assert square_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == {
        2: 4, 4: 16, 6: 36, 8: 64}


@pytest.mark.skip()
@pytest.mark.it(
    ("find_average_games: when called with empty list, function should "
     "return empty dictionary"))
def test_find_average_games_returns_empty_dict():
    assert find_average_games([]) == {}


@pytest.mark.skip()
@pytest.mark.it(
    ("find_average_games: when called with list with average games, "
     "function should return dictionary with keys and values of "
     "average games"))
def test_find_average_games_returns_dict_with_average_games():
    assert find_average_games([["Minecraft", 67]]) == {
        "Minecraft": 67}
    assert find_average_games(
        [["The Sims 2", 50], ["World of Warcraft", 33]]) == {
        "The Sims 2": 50, "World of Warcraft": 33}


@pytest.mark.skip()
@pytest.mark.it(
    ("find_average_games: when called with a list with only highly rated "
     "games, function should return empty dictionary"))
def test_find_average_games_returns_empty_dict_when_only_highly_rated_games():
    assert find_average_games([["Old School Runescape", 100]]) == {}
    assert find_average_games(
        [["Terraria", 89], ["Age of Empires 2", 95]]) == {}
    assert find_average_games([
        ["The Elder Scrolls IV: Oblivion", 82], ["Halo 3", 79],
        ["Tony Hawk's Pro Skater 2", 99]]) == {}


@pytest.mark.skip()
@pytest.mark.it(
    ("find_average_games: when called with a list with only poorly rated "
     "games, function should return empty dictionary"))
def test_find_average_games_returns_empty_dict_when_only_poorly_rated_games():
    assert find_average_games([["Baldur's Gate 3", 0]]) == {}
    assert find_average_games(
        [["Call of Duty", 5], ["Farmville", 17]]) == {}
    assert find_average_games([
        ["Deep Rock Galactic", 24], ["Farming Simulator 22", 11],
        ["Overcooked 2", 1]]) == {}


@pytest.mark.skip()
@pytest.mark.it(
    ("find_average_games: when called with a list with mixed scoring "
     "games, function should return dictionary with keys and "
     "values of average games"))
def test_find_average_games_returns_dict_with_average_games_mixed_scoring():
    assert find_average_games([["Minecraft", 67], ["Baldur's Gate 3", 0]]) == {
        "Minecraft": 67}
    assert find_average_games(
        [["The Elder Scrolls IV: Oblivion", 82], ["Minecraft", 67],
         ["Tony Hawk's Pro Skater 2", 99], ["Baldur's Gate 3", 0]]) == {
        "Minecraft": 67}
    assert find_average_games([
        ["Deep Rock Galactic", 24], ["Farming Simulator 22", 11],
        ["Old School Runescape", 100], ["The Sims 2", 50],
        ["World of Warcraft", 33]]) == {
        "The Sims 2": 50, "World of Warcraft": 33}
