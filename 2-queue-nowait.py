from random import random 
import time
import asyncio

# coroutine to generate work 
async def producer (queue): 
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
    await queue.put (None) 
    print (f'{time.ctime()} Producer: Done')

# coroutine to consume work 
async def consumer(queue):
    print('Consumer: Running')
    #consume work
    while True:
        # get a unit of work without blocking 
        try:
            item = queue.get_nowait() 
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waiting a while...') 
            await asyncio.sleep(0.5)
            continue
        # check for stop
        if item is None:
            break
        # report
        print (f'{time.ctime()} >got {item}')
    # all done
    print (f'{time.ctime()} Consumer: Done')

# entry point coroutine 
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers 
    await asyncio.gather (producer(queue), consumer(queue))
# start the asyncio program 
asyncio.run(main())

# Producer: Running
# Consumer: Running
# Wed Aug 23 14:34:51 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:52 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:52 2023 >got 0.6957113032561415
# Wed Aug 23 14:34:52 2023 >got 0.2902642482515494
# Wed Aug 23 14:34:52 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:53 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:53 2023 >got 0.7458854584337525
# Wed Aug 23 14:34:53 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:54 2023 >got 0.7890616981730612
# Wed Aug 23 14:34:54 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:54 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:55 2023 >got 0.9740432088557498
# Wed Aug 23 14:34:55 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:55 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:56 2023 >got 0.836694804067696
# Wed Aug 23 14:34:56 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:56 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:57 2023 >got 0.7683668339748777
# Wed Aug 23 14:34:57 2023 >got 0.01545714870580972
# Wed Aug 23 14:34:57 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:57 2023 >got 0.7774016852638173
# Wed Aug 23 14:34:57 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:34:58 2023 Producer: Done
# Wed Aug 23 14:34:58 2023 >got 0.49521220447895076
# Wed Aug 23 14:34:58 2023 Consumer: Done
