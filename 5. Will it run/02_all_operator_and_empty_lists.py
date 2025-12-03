from rich.traceback import install
install(show_locals=True)

def will_it_run():
    # hey, do you know the built-in `all` function? it's pretty easy
    assert all([True, True, True]) is True
    assert all([True, True, False]) is False

    # or, is it? let's check below
    assert all([]) is True
    assert all([[]]) is False
    assert all([[[]]]) is True

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")

if __name__ == "__main__":
    will_it_run()