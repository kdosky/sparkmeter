import asyncio
import logging
import os
import datetime 

logger = logging.getLogger(__name__)
SLEEP_DURATION = os.getenv("SLEEP_DURATION")

class Pipeline:
    async def __init__(self, *args, **kwargs): 
        sleep_duration = kwargs["default_sleep_duration"]
    async def sleep_for(self, coro, sleep_duration, *args, **kwargs): 
        asyncio.sleep(sleep_duration)
        logger.info("Slept for %s seconds", sleep_duration)
        start = datetime.datetime.now()
        await coro(*args, **kwargs) 
        end = datetime.datetime.now()
        time_elapsed = (start - end).total_seconds()
        logger.debug(f"Executed the coroutine for {time_elapsed} seconds")

