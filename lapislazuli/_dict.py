import itertools
from collections.abc import Generator

class LapisDict(dict):   

    def __repr__(self) -> str:
        kw = ", ".join([f"{key}={value}" for key, value in self.items()])
        return f"LapisDict({kw})"
    
    @property    
    def records(self) -> list[dict]:
        """Return a list of records from dictionary containing key: sequence pairs."""
        return list(self.zip())
    
    @property
    def cartesian_product(self) -> list[dict]:
        """Return a list of records containing the cartesian product of a dictionary with key: sequence pairs."""
        return list(self.product())
            
    def zip(self) -> Generator[dict, None, None]:
        """Generate records from base dictionary containing key: sequence pairs."""
        for vals in zip(*self.values(), strict=True):
            yield LapisDict({key: value for key, value in zip(self.keys(), vals)})
            
    def product(self) -> Generator[dict, None, None]:
        """Generate a Cartesian product of base dictionary with containing key: sequence pairs."""
        for vals in itertools.product(*self.values()):
            yield LapisDict({key: value for key, value in zip(self.keys(), vals)})