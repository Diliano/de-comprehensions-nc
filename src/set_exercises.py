def get_unique_departments(employees):
    unique_departments = []

    for employee in employees:
        if employee["department"] not in unique_departments:
            unique_departments.append(employee["department"])

    return unique_departments


def get_unique_words(words):
    pass
