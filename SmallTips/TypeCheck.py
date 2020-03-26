def check_type(data, _type):
    """ check data type
    Arguments:
        data {any} -- data you want to check data-type
        _type {any} -- data-type
    Returns:
        {bool} -- return True when data type is _type
    """
    return True if type(data) == _type else False
