from attrs import field
import numpy as np

def _repr_fill_dotdotdot(_: str) -> str:
    """Utility function for dataclasses that replaces the default repr with '...'."""
    return "..."

def np_field(short_repr: bool = True, **kwargs) -> field:
    """Utility function for dataclasses that returns a field with converter for numpy arrays."""
    field_kwargs = {"converter": np.array}
    field_kwargs.update(**kwargs)
    if short_repr: field_kwargs.update({"repr": _repr_fill_dotdotdot})
    return field(**field_kwargs)

if __name__ == "__main__":
    from attrs import define, field
    @define
    class Test:
        x: int = field(repr=_repr_fill_dotdotdot)
    
    t = Test(1)
    print(t)