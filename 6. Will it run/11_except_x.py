from rich.traceback import install

install(show_locals=True)


def will_it_run():
    x = 5
    try:
        raise Exception()
    except Exception as x:
        pass

    assert x == 5

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")

if __name__ == "__main__":
    will_it_run()
