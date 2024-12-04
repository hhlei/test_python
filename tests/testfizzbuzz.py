import pytest
from test_python.fizzbuzz import playFizzBuzz

def test_playFizzBuzz_nominal():
    output_str = playFizzBuzz(15)
    true_str = "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz"
    assert output_str == true_str
    
