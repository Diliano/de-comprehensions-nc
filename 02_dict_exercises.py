from test_api.checks import run_test, skip_test, format_err_msg


def find_word_lengths(words):
    word_lengths = {}

    for word in words:
        word_lengths[word] = len(word)

    return word_lengths


@run_test
def test_find_word_lengths_passed_empty_list_returns_empty_dict():
    assert find_word_lengths([]) == {}, format_err_msg(
        {}, find_word_lengths([])
    )


@skip_test
def test_find_word_lengths_returns_dict_with_single_key():
    assert find_word_lengths(["hello"]) == {"hello": 5}, format_err_msg(
        {"hello": 5}, find_word_lengths(["hello"])
    )
    assert find_word_lengths(["goodbye"]) == {"goodbye": 7}, format_err_msg(
        {"goodbye": 7}, find_word_lengths(["goodbye"])
    )
    assert find_word_lengths(["hi"]) == {"hi": 2}, format_err_msg(
        {"hi": 2}, find_word_lengths(["hi"])
    )


@skip_test
def test_find_word_lengths_returns_dict_with_keys_and_values():
    assert find_word_lengths(["hello", "goodbye"]) == {
        "hello": 5,
        "goodbye": 7,
    }, format_err_msg(
        {"hello": 5, "goodbye": 7}, find_word_lengths(["hello", "goodbye"])
    )

    assert find_word_lengths(["hi", "there"]) == {
        "hi": 2,
        "there": 5,
    }, format_err_msg(
        {"hi": 2, "there": 5}, find_word_lengths(["hi", "there"])
    )
    assert find_word_lengths(["hey", "there", "you"]) == {
        "hey": 3,
        "there": 5,
        "you": 3,
    }, format_err_msg(
        {"hey": 3, "there": 5, "you": 3},
        find_word_lengths(["hey", "there", "you"]),
    )
    assert find_word_lengths(["hey", "there", "you", "are"]) == {
        "hey": 3,
        "there": 5,
        "you": 3,
        "are": 3,
    }, format_err_msg(
        {"hey": 3, "there": 5, "you": 3, "are": 3},
        find_word_lengths(["hey", "there", "you", "are"]),
    )
    assert find_word_lengths(["hey", "there", "you", "are", "awesome"]) == {
        "hey": 3,
        "there": 5,
        "you": 3,
        "are": 3,
        "awesome": 7,
    }, format_err_msg(
        {"hey": 3, "there": 5, "you": 3, "are": 3, "awesome": 7},
        find_word_lengths(["hey", "there", "you", "are", "awesome"]),
    )
    assert find_word_lengths(
        ["hey", "there", "you", "are", "awesome", "and", "cool"]
    ) == {
        "hey": 3,
        "there": 5,
        "you": 3,
        "are": 3,
        "awesome": 7,
        "and": 3,
        "cool": 4,
    }, format_err_msg(
        {
            "hey": 3,
            "there": 5,
            "you": 3,
            "are": 3,
            "awesome": 7,
            "and": 3,
            "cool": 4,
        },
        find_word_lengths(
            ["hey", "there", "you", "are", "awesome", "and", "cool"]
        ),
    )


def switch_name_and_id(data):
    switched_data = {}

    for record in data.items():
        switched_data[record[1]] = record[0]

    return switched_data


@skip_test
def test_switch_name_and_id_passed_empty_dict_returns_empty_dict_():
    assert switch_name_and_id({}) == {}, format_err_msg(
        {}, switch_name_and_id({})
    )


@skip_test
def test_switch_name_and_id_returns_dict_with_single_swapped_key_and_value():
    assert switch_name_and_id({"Alex": "a7d29w"}) == {
        "a7d29w": "Alex"
    }, format_err_msg(
        {"a7d29w": "Alex"}, switch_name_and_id({"Alex": "a7d29w"})
    )
    assert switch_name_and_id({"Chon": "z2r51e"}) == {
        "z2r51e": "Chon"
    }, format_err_msg(
        {"z2r51e": "Chon"}, switch_name_and_id({"Chon": "z2r51e"})
    )
    assert switch_name_and_id({"Cat": "p3f44m"}) == {
        "p3f44m": "Cat"
    }, format_err_msg({"p3f44m": "Cat"}, switch_name_and_id({"Cat": "p3f44m"}))


@skip_test
def test_switch_name_and_id_returns_dict_with_swapped_keys_and_values():
    assert switch_name_and_id({"Alex": "a7d29w", "Chon": "z2r51e"}) == {
        "a7d29w": "Alex",
        "z2r51e": "Chon",
    }, format_err_msg(
        {"a7d29w": "Alex", "z2r51e": "Chon"},
        switch_name_and_id({"Alex": "a7d29w", "Chon": "z2r51e"}),
    )
    assert switch_name_and_id(
        {"Simon": "a7d29w", "Joe": "z2r51e", "Paul": "p3f44m"}
    ) == {
        "a7d29w": "Simon",
        "z2r51e": "Joe",
        "p3f44m": "Paul",
    }, format_err_msg(
        {"a7d29w": "Simon", "z2r51e": "Joe", "p3f44m": "Paul"},
        switch_name_and_id(
            {"Simon": "a7d29w", "Joe": "z2r51e", "Paul": "p3f44m"}
        ),
    )
    assert switch_name_and_id(
        {
            "Kyle": "a7d29w",
            "Danika": "z2r51e",
            "Liam": "p3f44m",
            "Cat": "q4r55t",
        }
    ) == {
        "a7d29w": "Kyle",
        "z2r51e": "Danika",
        "p3f44m": "Liam",
        "q4r55t": "Cat",
    }, format_err_msg(
        {
            "a7d29w": "Kyle",
            "z2r51e": "Danika",
            "p3f44m": "Liam",
            "q4r55t": "Cat",
        },
        switch_name_and_id(
            {
                "Kyle": "a7d29w",
                "Danika": "z2r51e",
                "Liam": "p3f44m",
                "Cat": "q4r55t",
            }
        ),
    )


def create_multiplication_table(multiplier, limit):
    pass


@skip_test
def test_create_multiplication_table_limit_0():
    assert create_multiplication_table(1, 0) == {}, format_err_msg(
        {}, create_multiplication_table(1, 0)
    )
    assert create_multiplication_table(5, 0) == {}, format_err_msg(
        {}, create_multiplication_table(5, 0)
    )
    assert create_multiplication_table(10, 0) == {}, format_err_msg(
        {}, create_multiplication_table(10, 0)
    )


@skip_test
def test_create_multiplication_table_limit_1_single_key():
    assert create_multiplication_table(1, 1) == {1: 1}, format_err_msg(
        {1: 1}, create_multiplication_table(1, 1)
    )
    assert create_multiplication_table(5, 1) == {1: 5}, format_err_msg(
        {1: 5}, create_multiplication_table(5, 1)
    )
    assert create_multiplication_table(10, 1) == {1: 10}, format_err_msg(
        {1: 10}, create_multiplication_table(10, 1)
    )


@skip_test
def test_create_multiplication_table_returns_dict_with_keys_from_1_to_limit():
    assert create_multiplication_table(1, 2) == {1: 1, 2: 2}, format_err_msg(
        {1: 1, 2: 2}, create_multiplication_table(1, 2)
    )
    assert create_multiplication_table(5, 5) == {
        1: 5,
        2: 10,
        3: 15,
        4: 20,
        5: 25,
    }, format_err_msg(
        {1: 5, 2: 10, 3: 15, 4: 20, 5: 25},
        create_multiplication_table(5, 5),
    )
    assert create_multiplication_table(10, 10) == {
        1: 10,
        2: 20,
        3: 30,
        4: 40,
        5: 50,
        6: 60,
        7: 70,
        8: 80,
        9: 90,
        10: 100,
    }, format_err_msg(
        {
            1: 10,
            2: 20,
            3: 30,
            4: 40,
            5: 50,
            6: 60,
            7: 70,
            8: 80,
            9: 90,
            10: 100,
        },
        create_multiplication_table(10, 10),
    )


def square_even_numbers(number_list):
    pass


@skip_test
def test_square_even_numbers_passed_empty_list_returns_empty_dict():
    assert square_even_numbers([]) == {}, format_err_msg(
        {}, square_even_numbers([])
    )


@skip_test
def test_square_even_numbers_returns_dict_with_squared_nums_all_evens():
    assert square_even_numbers([10]) == {10: 100}, format_err_msg(
        {10: 100}, square_even_numbers([10])
    )
    assert square_even_numbers([10, 20]) == {10: 100, 20: 400}, format_err_msg(
        {10: 100, 20: 400}, square_even_numbers([10, 20])
    )


@skip_test
def test_square_even_numbers_returns_empty_dict_when_passed_odd_numbers():
    assert square_even_numbers([1]) == {}, format_err_msg(
        {}, square_even_numbers([1])
    )
    assert square_even_numbers([1, 3, 5, 7, 9]) == {}, format_err_msg(
        {}, square_even_numbers([1, 3, 5, 7, 9])
    )
    assert square_even_numbers([11, 13, 15, 17, 19]) == {}, format_err_msg(
        {}, square_even_numbers([11, 13, 15, 17, 19])
    )


@skip_test
def test_square_even_numbers_mixed_list_of_odds_and_evens():
    assert square_even_numbers([1, 2, 3, 4, 5]) == {2: 4, 4: 16}
    assert square_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]) == {
        2: 4,
        4: 16,
        6: 36,
        8: 64,
    }


def find_average_games(games):
    pass


@skip_test
def test_find_average_games_passed_empty_list_returns_empty_dict():
    assert find_average_games([]) == {}


@skip_test
def test_find_average_games_returns_dict_with_average_games():
    assert find_average_games([["Minecraft", 67]]) == {"Minecraft": 67}
    assert find_average_games(
        [["The Sims 2", 50], ["World of Warcraft", 33]]
    ) == {"The Sims 2": 50, "World of Warcraft": 33}


@skip_test
def test_find_average_games_returns_empty_dict_when_only_highly_rated_games():
    assert find_average_games([["Old School Runescape", 100]]) == {}
    assert (
        find_average_games([["Terraria", 89], ["Age of Empires 2", 95]]) == {}
    )
    assert (
        find_average_games(
            [
                ["The Elder Scrolls IV: Oblivion", 82],
                ["Halo 3", 79],
                ["Tony Hawk's Pro Skater 2", 99],
            ]
        )
        == {}
    )


@skip_test
def test_find_average_games_returns_empty_dict_when_only_poorly_rated_games():
    assert find_average_games([["Baldur's Gate 3", 0]]) == {}
    assert find_average_games([["Call of Duty", 5], ["Farmville", 17]]) == {}
    assert (
        find_average_games(
            [
                ["Deep Rock Galactic", 24],
                ["Farming Simulator 22", 11],
                ["Overcooked 2", 1],
            ]
        )
        == {}
    )


@skip_test
def test_find_average_games_returns_dict_with_average_games_mixed_scoring():
    assert find_average_games([["Minecraft", 67], ["Baldur's Gate 3", 0]]) == {
        "Minecraft": 67
    }
    assert find_average_games(
        [
            ["The Elder Scrolls IV: Oblivion", 82],
            ["Minecraft", 67],
            ["Tony Hawk's Pro Skater 2", 99],
            ["Baldur's Gate 3", 0],
        ]
    ) == {"Minecraft": 67}
    assert find_average_games(
        [
            ["Deep Rock Galactic", 24],
            ["Farming Simulator 22", 11],
            ["Old School Runescape", 100],
            ["The Sims 2", 50],
            ["World of Warcraft", 33],
        ]
    ) == {"The Sims 2": 50, "World of Warcraft": 33}


if __name__ == "__main__":
    test_find_word_lengths_passed_empty_list_returns_empty_dict()
    test_find_word_lengths_returns_dict_with_single_key()
    test_find_word_lengths_returns_dict_with_keys_and_values()
    test_switch_name_and_id_passed_empty_dict_returns_empty_dict_()
    test_switch_name_and_id_returns_dict_with_single_swapped_key_and_value()
    test_switch_name_and_id_returns_dict_with_swapped_keys_and_values()
    test_create_multiplication_table_limit_0()
    test_create_multiplication_table_limit_1_single_key()
    test_create_multiplication_table_returns_dict_with_keys_from_1_to_limit()
    test_square_even_numbers_passed_empty_list_returns_empty_dict()
    test_square_even_numbers_returns_dict_with_squared_nums_all_evens()
    test_square_even_numbers_returns_empty_dict_when_passed_odd_numbers()
    test_square_even_numbers_mixed_list_of_odds_and_evens()
    test_find_average_games_passed_empty_list_returns_empty_dict()
    test_find_average_games_returns_dict_with_average_games()
    test_find_average_games_returns_empty_dict_when_only_highly_rated_games()
    test_find_average_games_returns_empty_dict_when_only_poorly_rated_games()
    test_find_average_games_returns_dict_with_average_games_mixed_scoring()
