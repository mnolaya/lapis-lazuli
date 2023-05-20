
import logging
from typing import Union
from pathlib import Path

from attrs import define, field

_DEF_FMT = "%(levelname)s:%(name)s:%(asctime)s: %(message)s"

@define
class Logger(logging.Logger):
    name: str
    level: int = logging.DEBUG
    log_format:  str = field(default=_DEF_FMT, repr=False)
    formatter: logging.Formatter = field(init=False, repr=False)
    
    def __attrs_post_init__(self):
        super().__init__(self.name)
        self.setLevel(self.level)
        self.formatter = logging.Formatter(self.log_format)
    
    def set_file_logger(self, filename: str | Path, level: int = None, encoding: str = "utf-8") -> None:
        """Set a file logger up for the instance"""
        fh = logging.FileHandler(filename, encoding=encoding)
        if level is None: level = self.level
        fh.setLevel(level)
        fh.setFormatter(self.formatter)
        self.addHandler(fh)
    
    @classmethod
    def make_test_logger(cls, log_name: str, filename: str | Path = "testlog.log", level: int = logging.DEBUG):
        """Helper method to create a logger with file handler for testing purposes. 
        Defaults to a file named "testlog.log" placed in the working directory."""
        logger = cls(log_name)
        logger.set_file_logger(filename, level)
        return logger       

if __name__ == "__main__":
    logger = Logger("test", level=logging.DEBUG)
    logger.set_file_logger("test.log")
    logger.debug(logger.name)