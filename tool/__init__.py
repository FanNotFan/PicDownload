import time
import functools
from tool.queue import log


def print_method_execute_time(arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if arg and isinstance(arg, str):
                print('Decorator Pass Parameters：%s' % arg)
            # print('start execute')
            start_time = time.time()
            res = func(*args, **kw)
            # print('end execute')
            end_time = time.time()
            log("[METHOD_NAME: "+func.__name__+'] takes %ss' % int(end_time - start_time))
            print("[Method Name: "+func.__name__+'] takes %ss' % int(end_time - start_time))
            return res
        return wrapper
    if callable(arg):
        return decorator(arg)
    return decorator


# without return
def decorator_calc_exec_time(arg):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            # print('start execute')
            start_time = time.time()
            func(*args, **kw)
            # print('end execute')
            end_time = time.time()
            # log("["+func.__name__+'] time consuming：%ss' % int(end_time - start_time))
            print("["+func.__name__+'] time consuming：%ss' % int(end_time - start_time))
        return wrapper
    if callable(arg):
        return decorator(arg)
    return decorator