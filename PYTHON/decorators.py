import time
import functools


def time_func(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Before function {func.__name__}")
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"After function {func.__name__}")

        print("-"*50)
        print(f"Execution Time: {end_time - start_time}")
        print("-"*50)

        return res
    return wrapper


@time_func
def sample_func(n=50_000):
    for _ in range(n):
        x = n


sample_func(100_000)

# It is the same thing as saying


def sample_func_2(n=50_000):
    for _ in range(n):
        x = n


sample_func_2 = time_func(sample_func_2)
sample_func_2(100_000)


def repeat_func(times=3):
    def decorator(func):
        functools.wraps(func)

        def wrapper(*args, **kwargs):
            # Before
            for _ in range(times):
                res = func(*args, **kwargs)
            # After
            return res
        return wrapper
    return decorator


@repeat_func(3)
def say_my_name():
    print("Heisenberg")


say_my_name()


def say_my_name_2():
    print("You're goddamn right.")


# Having the two decorators, or giving an argument is same as
# The below statements.
say_my_name_2 = repeat_func(3)(say_my_name_2)
say_my_name_2()


# Stacking decorators on top of each other. Or Nesting.
@time_func
@repeat_func(10)
def sample_func_3(n=100_000):
    for _ in range(n):
        x = n


sample_func_3()


# Class Decorators.
# Suppose you want to keep track of the number of calls or something
# Might come in handy, if you want to keep track of it.


class CountCalls:
    def __init__(self, func):
        self.func = func
        self.call_times = 0

    def __call__(self, *args, **kwargs):
        # Over Riding the call function. Would work when I call the object
        # For example, cc = CountCalls()
        # cc() would use this function.

        self.call_times += 1
        print(f"Function {self.func.__name__}. Called Time: {self.call_times}")
        res = self.func(*args, **kwargs)
        return res


@CountCalls
def sample():
    print("Hey there! I am a simple function!")


sample()
sample()
sample()
sample()

repeat_func(7)(sample)()