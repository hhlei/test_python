import pytest
from fizzbuzz.fizzbuzz import FizzBuzzify

def test_playFizzBuzz_nominal():
    output_str = FizzBuzzify(15)
    true_str = "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz"
    assert output_str == true_str
    
def test_playFizzBuzz_string():
    with pytest.raises(TypeError) as e_info:
        output_str = FizzBuzzify("abc")
        
def test_playFizzBuzz_float():
    with pytest.raises(TypeError) as e_info:
        output_str = FizzBuzzify(0.1234152)
        
def test_playFizzBuzz_non_positive():
    with pytest.raises(ValueError) as e_info:
        output_str = FizzBuzzify(-4)
