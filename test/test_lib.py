from typing import reveal_type

import pytest

import pyo3


def test_add_function():
    assert pyo3.sum_as_string(1, 2) == "3"


@pytest.mark.skip(reason="xxx")
def test_add_huge_ints():
    assert pyo3.sum_as_string(0x23456789123456789123456789, 1) == "..."


reveal_type(pyo3.say_hello)


def test_check_bad_file():
    with pytest.raises(FileNotFoundError):
        assert pyo3.check_reg("/etc/FOOBAR", "FOOBAR") == "xx"

def test_check_user():
    assert pyo3.check_reg("/etc/passwd", "nobody") == "You're OK"

def test_check_no():
    assert pyo3.check_reg("/etc/passwd", "FOOBAR") == "Sorry, nope"
