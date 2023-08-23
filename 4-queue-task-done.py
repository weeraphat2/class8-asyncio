from random import random
import asyncio 
import time

# coroutine to generate work
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
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work 
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running') 
    # consume work 
    while True:
        # get a unit of work.
        item = await queue.get()
        # report 
        print (f'{time.ctime()} >got {item}') 
        # block while processing
        if item:
            await asyncio.sleep(item) 
        # mark the task as done 
        queue.task_done()
# entry point coroutine 
async def main():
    # create the shared queue 
    queue =asyncio.Queue()
    #  start the consumer
    _ = asyncio.create_task(consumer(queue)) 
    # start the producer and wait for it to finish 
    await asyncio.create_task(producer(queue)) 
    #wait for all items to be processed 
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:32:31 2023 Consumer: Running
# Producer: Running
# Wed Aug 23 14:32:32 2023 >got 0.48519734521017566
# Wed Aug 23 14:32:32 2023 >got 0.009485376530739553
# Wed Aug 23 14:32:32 2023 >got 0.4291226165124242
# Wed Aug 23 14:32:33 2023 >got 0.6449610839160451
# Wed Aug 23 14:32:34 2023 >got 0.5083723578472746
# Wed Aug 23 14:32:34 2023 >got 0.792262016268848
# Wed Aug 23 14:32:35 2023 >got 0.9237311540201323
# Wed Aug 23 14:32:36 2023 >got 0.04928285295439161
# Wed Aug 23 14:32:36 2023 >got 0.25613042251748364
# Wed Aug 23 14:32:36 2023 Producer: Done
# Wed Aug 23 14:32:36 2023 >got 0.9438911643367769