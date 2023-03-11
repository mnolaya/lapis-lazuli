def read_file_lines(filepath, encoding="utf-8"):
    """Open a file, read, and return list of lines containing file contents.

    Args:
        filepath (str of Path): Valid path to text-readable file.
        encoding (str, optional): File encoding. Defaults to "utf-8".

    Returns:
        list: List containing file contents line-by-line.
    """
    def readlines(f, m, e):
        with open(f, m, encoding=e) as f:
            return f.readlines()
    try:
        lines = readlines(filepath, "r", encoding)
    except:
        encoding = "windows-1252"
        lines = readlines(filepath, "r", encoding)
    return lines

test = "hello"