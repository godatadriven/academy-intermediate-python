from dataclasses import dataclass
from rich.traceback import install

install(show_locals=True)


def will_it_run():
    x = 5

    class SomeClass:
        x = 17
        y = [x]*10
        z = [x for _ in range(10)]

    assert SomeClass.y[0] == 17
    assert SomeClass.z[0] == 5

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
