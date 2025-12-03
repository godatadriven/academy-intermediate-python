from rich.traceback import install

install(show_locals=True)


def will_it_run():
    x, y = (0, 1) if True else None, None
    assert (x,y) == (0, 1)

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
