from rich.traceback import install

install(show_locals=True)


def some_func(default_arg=[]):
    default_arg.append("some_string")
    return default_arg


def will_it_run():
    some_func()
    some_func()
    some_func([])

    assert some_func() == ['some_string', 'some_string', 'some_string']

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")


if __name__ == "__main__":
    will_it_run()
