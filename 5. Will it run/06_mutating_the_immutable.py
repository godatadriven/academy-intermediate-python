from rich.traceback import install
import pytest

install(show_locals=True)

def mutating_the_immutable():
    some_tuple = ("A", "tuple", "with", "values")
    another_tuple = ([1, 2], [3, 4], [5, 6])

    with pytest.raises(TypeError):
        some_tuple[2] = "change this"

    another_tuple[1].append(9)

    with pytest.raises(TypeError):
        another_tuple[2] += [99, 999]

    assert another_tuple == ([1, 2], [3, 4, 9], [5, 6, 99, 999])

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")

if __name__ == "__main__":
    mutating_the_immutable()
