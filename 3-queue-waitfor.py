import asyncio
import time
from random import random

# Coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()  
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue  
        await queue.put(value)  
    # send an all done signal
    await queue.put(None)  
    print(f'{time.ctime()} Producer: Done')

# consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        try:
            item = await asyncio.wait_for(queue.get(), timeout=0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: gave up waiting...')
            continue
        # Check for stop
        if item is None:
            break
        # report  
        print(f'{time.ctime()} > got {item}')  
    print('Consumer: Done')

# Entry point coroutine
async def main():
    # Create the shared queue
    queue = asyncio.Queue()
    # Run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# Start the asyncio program
asyncio.run(main())

# Producer: Running
# Wed Aug 23 14:35:37 2023 Consumer: Running
# Wed Aug 23 14:35:37 2023 Consumer: gave up waiting...
# Wed Aug 23 14:35:37 2023 > got 0.8187054653004054
# Wed Aug 23 14:35:38 2023 Consumer: gave up waiting...
# Wed Aug 23 14:35:38 2023 > got 0.7971714067946251
# Wed Aug 23 14:35:39 2023 Consumer: gave up waiting...
# Wed Aug 23 14:35:39 2023 > got 0.7490094363966389
# Wed Aug 23 14:35:39 2023 Consumer: gave up waiting...
# Wed Aug 23 14:35:40 2023 > got 0.7586216880404593
# Wed Aug 23 14:35:40 2023 Consumer: gave up waiting...
# Wed Aug 23 14:35:41 2023 > got 0.938742770987367
# Wed Aug 23 14:35:41 2023 Consumer: gave up waiting...
# Wed Aug 23 14:35:41 2023 > got 0.8193976819521919
# Wed Aug 23 14:35:41 2023 > got 0.0063193488759341054
# Wed Aug 23 14:35:42 2023 Consumer: gave up waiting...
# Wed Aug 23 14:35:42 2023 > got 0.9512071982641732
# Wed Aug 23 14:35:43 2023 Consumer: gave up waiting...
# Wed Aug 23 14:35:43 2023 > got 0.923758919161265
# Wed Aug 23 14:35:44 2023 Producer: Done
# Wed Aug 23 14:35:44 2023 > got 0.12827577857975758
# Consumer: Done