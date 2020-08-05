import time


def timer(*dargs, **dkwargs):
    def decorator(func):
        def wrapper(*args, **kwargs):
            st = time.time()
            iteration = dkwargs["iteration"]
            
            for _ in range(iteration):
                func(*args, **kwargs)
            
            avg_time = (time.time() - st) / iteration
            print(f"Average Time: {avg_time}   (iteration: {iteration})")
    
        return wrapper
    
    return decorator
    
    
if __name__ == "__main__":
    @timer(iteration=100)
    def timer_test():
        time.sleep(0.01)
    
    timer_test()
    # >>> Average Time: 0.0118611478805542   (iteration: 100)
