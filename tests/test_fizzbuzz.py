import pytest
from fizzbuzz.fizzbuzz import FizzBuzzify, playFizzBuzz


def test_FizzBuzzify_nominal():
    output_str = FizzBuzzify(15)
    true_str = (
        "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz"
    )
    assert output_str == true_str


def test_FizzBuzzify_string():
    with pytest.raises(TypeError) as e_info:
        output_str = FizzBuzzify("abc")


def test_FizzBuzzify_float():
    with pytest.raises(TypeError) as e_info:
        output_str = FizzBuzzify(0.1234152)


def test_FizzBuzzify_non_positive():
    with pytest.raises(ValueError) as e_info:
        output_str = FizzBuzzify(-4)


def test_playFizzBuzz(monkeypatch, capfd):
    rounds = 15
    monkeypatch.setattr("builtins.input", lambda _: rounds)
    playFizzBuzz()
    out, err = capfd.readouterr()
    assert (
        out
        == "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz\n"
    )
