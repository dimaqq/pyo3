import rusting


def test_add_function():
    assert rusting.sum_as_string(1, 2) == "3"


def test_add_huge_ints():
    assert rusting.sum_as_string(0x23456789123456789123456789, 1) == "..."
