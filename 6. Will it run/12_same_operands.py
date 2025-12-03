from rich.traceback import install

install(show_locals=True)


def will_it_run():
    a = [1, 2, 3, 4]
    b = a
    a = a + [5, 6, 7, 8]

    c = [1, 2, 3, 4]
    d = c
    c += [5, 6, 7, 8]

    assert d == b

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
