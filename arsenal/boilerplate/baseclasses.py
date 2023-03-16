from typing import Callable

def _repr_fill_dotdotdot(_) -> str:
    """Utility function for dataclasses that replaces the default repr with '...'"""
    return "..."

if __name__ == "__main__":
    from attrs import define, field
    @define
    class Test:
        x: int = field(repr=_repr_fill_dotdotdot)
    
    t = Test(1)
    print(t)