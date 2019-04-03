"""
Sleep Sorting Algorithm:

For every element X on the sequence the program does this:
1) Sleeps for X seconds
2) Prints X

Usage:
$ python sleep_sort.py 8 6 10 2 15 7
"""

import sys
import asyncio

from typing import List


async def sleepprint(i: int) -> None:
    await asyncio.sleep(i)
    print(i, end=" ", flush=True)


async def sleepsort(l: List[int]) -> None:
    # Create all coroutines before starting them
    tasks = [asyncio.create_task(sleepprint(i)) for i in l]
    # Run coroutines
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    args = [int(val) for val in sys.argv[1:]]
    asyncio.run(sleepsort(args))
