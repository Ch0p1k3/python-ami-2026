import functools
import time
from datetime import datetime


def time_it(func):
    @functools.wraps(func)
    def wrap(*args, **kwargs):
        start = datetime.now()
        answer = func(*args, **kwargs)
        wrap.last_time_taken = (datetime.now() - start).total_seconds()
        return answer

    wrap.last_time_taken = 0.
    return wrap


@time_it
def foo(*args):
    time.sleep(2)
    return 3


# foo = time_it(foo)


ans = foo(1, 2, 3)
print(f"{foo.last_time_taken=}, {ans=}")
