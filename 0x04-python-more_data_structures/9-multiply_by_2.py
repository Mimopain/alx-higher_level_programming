def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}

def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
