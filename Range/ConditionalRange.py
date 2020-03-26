from copy import deepcopy
from pprint import pprint

__default = {
    "is_end": False,
    "is_reverse": False,
    "step": 1,
    "condition_function": lambda x: True,
    "preset_condition_function": None,
}


__PRESET_CONDITION_FUNCTION = {
    "odd": lambda x: x % 2 == 1,
    "even": lambda x: x % 2 == 0,
    None: lambda x: True
}


def crange(_min, _max, **kwargs):
    """ range function with conditions

    Arguments:
        start {int} -- start value
        end {int} -- end value

    Keyword Arguments:
        is_end {bool} -- True when you want to get end (default: False)
        is_reverse {bool} -- True when you want to get value reverse order (default: False)
        step {int} -- the number of step of 1 iteration (default: 1)
        condition_function {function} -- function for set conditions
                                         when condition_function returns True, the value will be yielded
        preset_condition_function {str or None} -- use preset function (default: None)

    """
    __default.update(kwargs)
    for k, v in __default.items():
        globals()[k] = v

    _start = _max if is_reverse else _min
    if is_end:
        _end = _min -1 if is_reverse else _max + 1

    else:
        _end = _min if is_reverse else _max

    sign = -1 if is_reverse else 1

    for i in range(_start, _end, sign*step):
        if condition_function(i):
            yield i


if __name__ == "__main__":
    for i in crange(0, 10, is_end=True, is_reverse=True):
        print(i)
