from rich.traceback import install

install(show_locals=True)


def will_it_run():
    assert round(1.5) == round(2.5)

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
