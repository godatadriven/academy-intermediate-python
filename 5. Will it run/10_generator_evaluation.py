from rich.traceback import install

install(show_locals=True)


def will_it_run():
    array = [1, 8, 15]

    # Select each number that occurs at least once.
    gen = (x for x in array if array.count(x) > 0)

    array = [2, 8, 22]

    result = list(gen)
    assert result == [1, 8, 15]

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
