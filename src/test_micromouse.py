from .micromouse import convert_micro_mouse


def test_convert():
    block = [
        "o---o---o",
        "|       |",
        "o   o   o",
        "| S | G |",
        "o---o---o",
    ]

    expected = [
        " # # # # #",
        " #       #",
        " #   #   #",
        " # S # E #",
        " # # # # #",
    ]

    actual = convert_micro_mouse(block)
    assert actual == expected