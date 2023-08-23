import asyncio
import time
from random import random

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()  
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)  

    await queue.put(None)  
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consum work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal  
        if item is None:
            break
        # report  
        print(f'{time.ctime()} > got {item}')  
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:34:18 2023 Producer: Running
# Wed Aug 23 14:34:18 2023 Consumer: Running
# Wed Aug 23 14:34:18 2023 > got 0.7667560830003483
# Wed Aug 23 14:34:19 2023 > got 0.19736497109290674
# Wed Aug 23 14:34:19 2023 > got 0.3902465274386291
# Wed Aug 23 14:34:19 2023 > got 0.16116303621333028
# Wed Aug 23 14:34:20 2023 > got 0.6244989074521644
# Wed Aug 23 14:34:20 2023 > got 0.3232134077922094
# Wed Aug 23 14:34:21 2023 > got 0.9406625885748218
# Wed Aug 23 14:34:21 2023 > got 0.19357445810544005
# Wed Aug 23 14:34:22 2023 > got 0.8042977963697283
# Wed Aug 23 14:34:23 2023 Producer: Done
# Wed Aug 23 14:34:23 2023 > got 0.9959262142295023
# Wed Aug 23 14:34:23 2023 Consumer: Done