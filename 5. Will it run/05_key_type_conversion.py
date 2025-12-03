from rich.traceback import install
install(show_locals=True)


def will_it_run():
    d = {1: 'a', True: 'b', 1.0: 'c'}

    assert 'c' in d.values()
    assert 'b' in d.values()
    assert 'a' in d.values()
    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
