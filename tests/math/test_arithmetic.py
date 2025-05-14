from pywander.math.arithmetic import get_approximate_number, format_float

def test_get_approximate_number():

    result = get_approximate_number(1.414576, 1.4142135623730951)
    assert format_float(*result) == "0.00037"

    result = get_approximate_number(1.452876, 1.4142135623730951)
    assert format_float(*result) == '0.039'

