def read_file_lines(filepath, mode="rb"):
    """Open a file, read, and return list of lines containing file contents.

    Args:
        filepath (str of Path): Valid path to text-readable file.
        mode (str, optional): Open mode. Defaults to "rb".

    Returns:
        list: List containing file contents line-by-line.
    """
    with open(filepath, mode) as f:
        return f.readlines()
