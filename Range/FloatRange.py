def float_range(min_: float, max_: float, step_size: int, 
                round_pos: int = 5, is_ascending: bool = True):
    """ iterator for providing range that data-type is float

    Arguments:
        min_ {float} -- minimum boundary value
        max_ {float} -- maximum boundary value
        step_size {int} -- how much you want to step
        round_pos {int} -- which position to round error (default: 5)
        is_ascending {bool} -- if you want to sort in ascending order, set this as True
                               (default: True)
    """
    assert not step_size == 0, "Please specified step_size over 0"

    step_num = int((max_ - min_) / step_size)

    if is_ascending:
        value = [round(min_ + step_size * i, round_pos) for i in range(step_num)]
    else:
        value = [round(max_ - step_size * i, round_pos) for i in range(step_num)]

    for v in value:
        yield v
