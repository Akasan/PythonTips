class InvalidArgumentError(Exception):
    def __init__(self, desired_args, specified_args):
        mes = f"Please set argument as {desired_args} (specified {specified_args})"
        super().__init__(mes)


def check_annotation(func):
    annotations = func.__annotations__
    del annotations["return"]
    desired_args = list(annotations.values())

    def wrapper(*args):
        specified_args = [type(arg) for arg in args]
        assert desired_args == specified_args, InvaludArgumentError(
                desired_args, specified_args
        )

        result = func(*args)
        return result

    return wrapper
