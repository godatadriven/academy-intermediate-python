from rich.traceback import install
install(show_locals=True)

def will_it_run():
    # Get a slice of this!
    x = list(range(10))
    x[1::2] = '#####'
    assert x == [0, '#', 2, '#', 4, '#', 6, '#', 8, '#']

    x[1::2] = 'xxxx'
    assert x == [0, 'x', 2, 'x', 4, 'x', 6, 'x', 8, 'x']

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
