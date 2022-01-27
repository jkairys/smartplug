import os, asyncio, random
from typing import List
from loguru import logger


async def monitor(plugs: List[any]):
    # loop = asyncio.get_event_loop()
    while True:
        for p in plugs:
            power = await p.async_get_instant_metrics()
            logger.info(f'plug: {p.name}, metrics: {power}')
        await asyncio.sleep(5)
