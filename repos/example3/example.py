from typing import Iterable, List, Literal, Optional, Set, Type, Union

nums = [1, 2, 3, 4]
nums: List[int] = []

x: int = 1

three_dimensional_vector: tuple[int, ...] = (1, 2, 3)

# fruits: Set[str] = {"a", "b", "k"}
fruits: Iterable[str]


misc_items: list[Union[int, float, str]] = [1, 2.0, "abc", 6, 9.5]

y: Union[int, str, float, Type]
z: int | str | float

t = None
t = 1

s: Union[int, None] = None

u: Optional[int] = None

def greet(name: str | None = None):

