import traceback


def exception_catcher(to_file=True, log_filename="error.log"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                print(f"Start function {func.__name__}.")
                func(*args, **kwargs)
                print("End function without exceptions.")

            except Exception as e:
                if to_file:
                    with open(log_filename, 'w') as f:
                        print(f"Error was raised.\nPlease refer to '{log_filename}'.")
                        traceback.print_exc(file=f)
                else:
                    traceback.print_exc()

        return wrapper

    return decorator


# sample
@exception_catcher()
def hoge(a, b):
    print(a/b)

hoge(1. 2)
# Start function hoge.
# 0.5
# End function without exceptions.

hoge(1, 0)
# Start function hoge.
# Error was raised.
# Please refer to 'error.log'.
