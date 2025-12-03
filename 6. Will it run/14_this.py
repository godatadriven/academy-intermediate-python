
from rich.traceback import install

install(show_locals=True)

def will_it_run():
    import this
    print("-"*20)
    love = this

    assert this is love
    # assert love is True
    # assert love is False
    assert love is not True or False
    assert love is love

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
