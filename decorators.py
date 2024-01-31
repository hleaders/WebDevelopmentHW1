import matplotlib.pyplot as plt

import timeit

fib_timer_data = []

def timer(func):
    def timer_wrap(*args, **kwargs):  
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        func_running_time = timeit.default_timer() - start_time
        fib_timer_data.append((args[0], func_running_time))
        print(f"Finished in {func_running_time}s: f({args[0]}) -> {result}")
        return result
    return timer_wrap

def plot_data():
    fib_numbers, running_times = zip(*fib_timer_data)

    plt.plot(fib_numbers, running_times, marker='o')
    plt.title('Fibonacci Calculation Time')
    plt.xlabel('Fibonacci Number')
    plt.ylabel('Running Time (s)')
    plt.show()
    