#pip install pytest to install pytest

import pytest #importing pytest
def fuzzy_math(num1,operator, num2): # method that we will be testing on
    if type(num1) != int or type(num2) !=int:
        raise Exception ('fuzzy_math function requires the numbers to be integer')
    
    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1*num2
    else:
        raise Exception(f"I don't know how to do math with '{operator}'")

    if result < 0:
        return 'A negative number, what does that even mean? Can you hold it?'
    elif result < 10:
        return 'A small number. I can deal with that.'
    elif result < 20:
        return 'A medium-sized number. Ok.'
    else:
        return 'A really big number, way toooo big for me and my processing power'

class TestFuzzyMath: #its nice practice to first write the scenarios and then later implement them
    def test_non_int_input_for_num1(self): # works but pytest has better way
        error = None
        try:
            fuzzy_math('hi', '+', 2)
        except Exception as e: #catching an error
            error = e # assigning value of e to error
        assert error is not None # asserting that the error is not None

    def test_non_int_input_for_num2(self): #doing it with pytest
        with pytest.raises(Exception) as exc_info: # with takes exception class and wraps it to exc_info.
            fuzzy_math(2, '+','hi') # if we dont get exception pytest.raises will raise an exception because we are telling it that we're expecting an exception
        assert 'fuzzy_math function requires' in str(exc_info) # asserting the raised exception and changing it to string format so we can read it

    def test_addition_with_negative_result(self):
        pass

    def test_addition_with_small_result(self): # Happy path testcase
        #assert fuzzy_math(2,'+',2) == 'A small number. I can deal with that.' #checking exact output
        assert 'small number' in fuzzy_math(2,'+',2)  #more fuzzy way to test but still testing

    def test_addition_with_medium_sized_result(self):
        assert 'medium-sized' in fuzzy_math(9,'+',9)

    def test_addition_with_big_result(self):
        assert 'really big number' in fuzzy_math(11,'+',11)

    def test_multiplication_with_negative_result(self):
        #assert 'negative number' in fuzzy_math(-1, '+', 1)
        pass
    def test_multiplication_with_small_result(self):
        pass

    def test_multiplication_with_medium_sized_result(self):
        pass

    def test_multiplication_with_big_result(self):
        pass
    
    def test_invalid_opreator(self):
        pass
