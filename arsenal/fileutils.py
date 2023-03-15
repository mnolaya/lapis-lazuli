from typing import Callable
from io import TextIOBase
from pathlib import Path

def open_text_file(filepath: str | Path, func: Callable, mode="r") -> TextIOBase:
    """Open file containing text and read contents to TextIO buffer.

    Args:
        filepath (str | Path): Path to valid file containing text.
        mode (str, optional): Open mode. Defaults to "r".

    Returns:
        TextIOBase: File contents stored in buffer.
    """
    def opendo(f, e):
        with open(f, mode, encoding=e) as f:
            return func(f)
    try:
        encoding = "utf-8"
        return opendo(filepath, encoding)
    except UnicodeDecodeError:
        encoding = "windows-1252"
        return opendo(filepath, encoding)
    
def read_textio_lines(io: TextIOBase) -> list[list[str]]:
    """Read lines from TextIO into line-by-line lists."""
    return io.readlines()

if __name__ == "__main__":
    test_txt_file = "E:/repos/material-characterization/characterize/kinetics/tests/!6.1.txt"
    
    lines = open_text_file(test_txt_file, read_textio_lines, mode="r")
    # print(lines)