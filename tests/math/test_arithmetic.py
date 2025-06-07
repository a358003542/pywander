from pywander.math.arithmetic import get_approximate_number, format_float

from pywander.math.arithmetic import BinaryFlags


def test_get_approximate_number():

    result = get_approximate_number(1.414576, 1.4142135623730951)
    assert format_float(*result) == "0.00037"

    result = get_approximate_number(1.452876, 1.4142135623730951)
    assert format_float(*result) == '0.039'

def test_binary_flags():
    flags = BinaryFlags()

    flags.set_flag(31)
    flags.set_flag(0)
    assert flags.check_flag(0)
    assert flags.check_flag(31)
    assert not flags.check_flag(30)
    flags.clear_flag(0)
    assert not flags.check_flag(0)