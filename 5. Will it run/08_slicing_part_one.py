from rich.traceback import install
install(show_locals=True)

def will_it_run():
    # Get a slice of this!
    x = list(range(10))

    assert x[0] == 0
    assert x[-100:100] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
