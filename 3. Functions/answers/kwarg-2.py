def make_sentence(**words):
    return ' '.join(word for word in words.values()).capitalize()

make_sentence(a="using", b="kwargs", c="can", d="make", e="a", f="function", g="flexible")