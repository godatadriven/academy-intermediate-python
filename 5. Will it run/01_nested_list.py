from rich.traceback import install
install(show_locals=True)

def will_it_run():
    row = ['']*3  #  one row of three columns
    field = [row]*3 # field of three rows
    field[0][0] = 'X'  # fill top left row with an X

    expected = [["X", "", ""],["","",""],["","",""]]

    assert field == expected

    print("🎉🎉🎉 It all ran!!! 🎉🎉🎉")

if __name__ == "__main__":
    will_it_run()