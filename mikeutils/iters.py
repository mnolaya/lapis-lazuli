import itertools

def dict_product(dictionary: dict[str, list]) -> itertools.product:
    """Return a Cartesian product generator from a dictionary of lists where each item yielded is a dictionary of key, value pairs from one of the products."""
    itemized = [[{k: val} for val in dictionary[k]] for k in dictionary.keys()]
    for p in itertools.product(*itemized):
        yield {k: v for d in p for k, v in d.items()}

if __name__ == "__main__":
    test_dict = {
        "1": [1, 2, 3],
        "2": ["hi", "5", "10"],
        "3": [5, 6, 9]
    }
    p = dict_product(test_dict)
    print(list(p))