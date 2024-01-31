from functools import lru_cache
from decorators import timer, plot_data

@timer
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1 
    else:
        return fib(n-1) + fib(n-2)
    
if __name__ == "__main__":
    fib(20)
    plot_data()