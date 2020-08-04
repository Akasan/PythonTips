import time


def timer(func):
    def wrapper(*args, **kwargs):
        st = time.time()
        func(*args, **kwargs)
        print(f"Process time : {time.time() - st}")
       
    return wrapper
    
    
if __name__ == "__main__":
    @timer
    def timer_test():
        print("Timer test function")
    
    timer_test()
