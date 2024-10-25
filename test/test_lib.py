from typing import reveal_type as reveal_type

import pytest

import pyo3


def test_add_function():
    assert pyo3.sum_as_string(1, 2) == "3"


def test_add_function_kw1():
    assert pyo3.sum_as_string(a=1, b=2) == "3"


@pytest.mark.xfail(reason="wrong arg name")
def test_add_function_kw2():
    assert pyo3.sum_as_string(x=1, y=2) == "3"  # type: ignore


@pytest.mark.skip(reason="value is too large, anyway")
def test_add_huge_ints():
    assert pyo3.sum_as_string(0x23456789123456789123456789, 1) == "..."


# reveal_type(pyo3.say_hello)


def test_check_bad_file():
    with pytest.raises(FileNotFoundError):
        assert pyo3.check_reg("/etc/FOOBAR", "FOOBAR") == "xx"

def test_check_user():
    assert pyo3.check_reg("/etc/passwd", "nobody") == "You're OK"

def test_check_no():
    assert pyo3.check_reg("/etc/passwd", "FOOBAR") == "Sorry, nope"
