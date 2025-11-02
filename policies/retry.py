import time
from typing import Callable, Tuple

def retry(times: int = 3, delay: float = 0.2):
  
    def deco(func: Callable):
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    time.sleep(delay)
            raise last_exc
        return wrapper
    return deco
