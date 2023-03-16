from attrs import field
import numpy as np

def _repr_fill_dotdotdot(_: str) -> str:
    """Utility function for dataclasses that replaces the default repr with '...'."""
    return "..."

def np_field(repr: str = "short") -> field:
    """Utility function for dataclasses that returns a field with converter for numpy arrays."""
    kwargs = {"converter": np.array}
    if repr.lower() == "short": kwargs.append("repr": _repr_fill_dotdotdot)
    return field(**kwargs)

if __name__ == "__main__":
    from attrs import define, field
    @define
    class Test:
        x: int = field(repr=_repr_fill_dotdotdot)
    
    t = Test(1)
    print(t)