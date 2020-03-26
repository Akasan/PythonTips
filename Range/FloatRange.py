def float_range(_min, _max, step_size, round_pos=5, is_ascending=True):
    """ iterator for providing range that data-type is float

    Arguments:
        _min {float} -- minimum boundary value
        _max {float} -- maximum boundary value
        step_size {int} -- how much you want to step
        round_pos {int} -- which position to round error (default: 5)
        is_ascending {bool} -- if you want to sort in ascending order, set this as True
                               (default: True)
    """
    assert not step_size == 0, "Please specified step_size over 0"

    step_num = int((_max - _min) / step_size)

    if is_ascending:
        value = [round(_min + step_size * i, round_pos) for i in range(step_num)]
    else:
        value = [round(_max - step_size * i, round_pos) for i in range(step_num)]

    for v in value:
        yield v


if __name__ == "__main__":
    for i in float_range(_min=0, _max=100, step_size=1/3):
        print(i)
