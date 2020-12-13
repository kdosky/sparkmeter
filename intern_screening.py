import asyncio
import logging
# added import that was missing 
import os
# added import that was missing 
import datetime 

logger = logging.getLogger(__name__)
SLEEP_DURATION = os.getenv("SLEEP_DURATION")

class Pipeline:
    # method was missing slef as argument 
    async def __init__(self, *args, **kwargs): 
        default_sleep_duration = kwargs["default_sleep_duration"]
    # SLEEP_DURATION should have been in all cap just like variable    
    async def sleep_for(self, coro, SLEEP_DURATION, *args, **kwargs):
        # SLEEP_DURATION should have been in all cap just like variable 
        asyncio.sleep(SLEEP_DURATION)
        # SLEEP_DURATION should have been in all cap just like variable
        # line needed to be indented correctly  
        logger.info("Slept for %s seconds", SLEEP_DURATION)
        # added datetime
        start = datetime.datetime.now()
        # kwargs was spelled as kwarg
        await coro(*args, **kwargs)
        # added datetime
        # line needed to be indented correctly 
        end = datetime.datetime.now()
        # line needed to be indented correctly 
        time_elapsed = (start - end).total_seconds()
        # line needed to be indented correctly 
        logger.debug(f"Executed the coroutine for {time_elapsed} seconds")

