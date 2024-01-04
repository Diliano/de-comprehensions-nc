def find_word_lengths(words):
    word_lengths = {}

    for word in words:
        word_lengths[word] = len(word)

    return word_lengths


def switch_name_and_id(data):
    switched_data = {}

    for record in data.items():
        switched_data[record[1]] = record[0]

    return switched_data


def create_multiplication_table(multiplier, limit):
    pass


def square_even_numbers(number_list):
    pass


def find_average_games(games):
    pass
