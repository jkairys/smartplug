import asyncio
import os
from typing import Callable


def run_sync(fn: Callable, *args, **kwargs):
    # Windows and python 3.8 requires to set up a specific event_loop_policy.
    #  On Linux and MacOSX this is not necessary.
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    loop = asyncio.get_event_loop()
    ret = loop.run_until_complete(fn(*args, **kwargs))
    # loop.close()
    return ret


def run_forever(fn: Callable, *args, **kwargs):
    loop = asyncio.get_event_loop()
    loop.create_task(fn(*args, **kwargs))
    loop.run_forever()
