def flatten_list(nested_list):
    flattened_list = []

    for sub_list in nested_list:
        for el in sub_list:
            flattened_list.append(el)

    return flattened_list


def create_square_matrix(num):
    pass
