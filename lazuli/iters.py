import itertools, typing, enum

T = typing.TypeVar('T')

def itemize_dict(dictionary: dict[str, list[T]]) -> list[list[dict[str, T]]]:
    """Create a list of lists of dictionaries containing the key and each value associated with the key of the original dictionary."""
    return [[{k: val} for val in dictionary[k]] for k in dictionary.keys()]

def dict_product(dictionary: dict[str, list[T]]) -> dict[str, T]:
    """Return a Cartesian product generator from a dictionary of lists where each item yielded is a dictionary of key, value pairs from one of the products."""
    itemized = itemize_dict(dictionary)
    for p in itertools.product(*itemized):
        yield {k: v for d in p for k, v in d.items()}

def dict_zip(dictionary: dict[str, list[T]]) -> dict[str, T]:
    """Return a zip generator from a dictionary of lists where each item yielded is a dictionary of key, value pairs from one of the zips."""
    itemized = itemize_dict(dictionary)
    for p in zip(*itemized):
        yield {k: v for d in p for k, v in d.items()}

if __name__ == "__main__":
    test_dict = {
        "1": [1, 2, 3],
        "2": ["hi", "5", "10"],
        "3": [5, 6, 9]
    }
    p = dict_product(test_dict)
    for p in dict_zip(test_dict):
        print(p)