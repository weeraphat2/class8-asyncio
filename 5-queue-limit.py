from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
     # generate work
    for i in range(10):
         # generate a value
        value = random() 
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue, may block  
        await queue.put(value)  
    print(f'{time.ctime()} Producer: Done')

# coroutine to 
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} > got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
            # mark as completed
            queue.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue) for _ in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for the consumer to process all items
    await queue.join()

# start the asyncio program
asyncio.run(main())

# Wed Aug 23 14:36:07 2023 Consumer: Running
# Wed Aug 23 14:36:07 2023 Producer: Running
# Wed Aug 23 14:36:07 2023 Producer: Running
# Wed Aug 23 14:36:07 2023 Producer: Running
# Wed Aug 23 14:36:07 2023 Producer: Running
# Wed Aug 23 14:36:07 2023 Producer: Running
# Wed Aug 23 14:36:07 2023 > got 0.16637000297047855
# Wed Aug 23 14:36:08 2023 > got 0.2109051156065448
# Wed Aug 23 14:36:08 2023 > got 0.2591372426664872
# Wed Aug 23 14:36:08 2023 > got 0.35858233746545765
# Wed Aug 23 14:36:08 2023 > got 0.005275964119455967
# Wed Aug 23 14:36:08 2023 > got 0.40600834034630073
# Wed Aug 23 14:36:09 2023 > got 0.29136902757484273
# Wed Aug 23 14:36:09 2023 > got 0.21654664375550026
# Wed Aug 23 14:36:09 2023 > got 0.7352782893008614
# Wed Aug 23 14:36:10 2023 > got 0.7739497973210284
# Wed Aug 23 14:36:11 2023 > got 0.19826542423528648
# Wed Aug 23 14:36:11 2023 > got 0.7455711911418401
# Wed Aug 23 14:36:12 2023 > got 0.685631974408079
# Wed Aug 23 14:36:12 2023 > got 0.45589538508904637
# Wed Aug 23 14:36:13 2023 > got 0.6108281996209504
# Wed Aug 23 14:36:14 2023 > got 0.6639952550317804
# Wed Aug 23 14:36:14 2023 > got 0.8829091770861943
# Wed Aug 23 14:36:15 2023 > got 0.87314776163576
# Wed Aug 23 14:36:16 2023 > got 0.05636653641494982
# Wed Aug 23 14:36:16 2023 > got 0.8519854371298092
# Wed Aug 23 14:36:17 2023 > got 0.677753465949987
# Wed Aug 23 14:36:18 2023 > got 0.7224051206417463
# Wed Aug 23 14:36:18 2023 > got 0.7138050736485906
# Wed Aug 23 14:36:19 2023 > got 0.29667533530269363
# Wed Aug 23 14:36:19 2023 > got 0.661919559439906
# Wed Aug 23 14:36:20 2023 > got 0.24918479980093455
# Wed Aug 23 14:36:20 2023 > got 0.4283445809244222
# Wed Aug 23 14:36:21 2023 > got 0.9974094270073806
# Wed Aug 23 14:36:22 2023 > got 0.603779601493964
# Wed Aug 23 14:36:22 2023 > got 0.3212861433337916
# Wed Aug 23 14:36:23 2023 > got 0.204317113446719
# Wed Aug 23 14:36:23 2023 > got 0.9189277731625809
# Wed Aug 23 14:36:24 2023 > got 0.013494518576780856
# Wed Aug 23 14:36:24 2023 > got 0.4351129450660618
# Wed Aug 23 14:36:24 2023 > got 0.05515980399114073
# Wed Aug 23 14:36:24 2023 Producer: Done
# Wed Aug 23 14:36:24 2023 > got 0.2813123009543599
# Wed Aug 23 14:36:25 2023 > got 0.14204391054421794
# Wed Aug 23 14:36:25 2023 > got 0.23864147293868332
# Wed Aug 23 14:36:25 2023 > got 0.5304573637286822
# Wed Aug 23 14:36:26 2023 > got 0.2851732466329454
# Wed Aug 23 14:36:26 2023 > got 0.2627024417720889
# Wed Aug 23 14:36:26 2023 > got 0.9903040452394934
# Wed Aug 23 14:36:27 2023 > got 0.5513941919250266
# Wed Aug 23 14:36:28 2023 > got 0.13893608711160488
# Wed Aug 23 14:36:28 2023 > got 0.14850219611739934
# Wed Aug 23 14:36:28 2023 Producer: Done
# Wed Aug 23 14:36:28 2023 > got 0.10967496132250265
# Wed Aug 23 14:36:28 2023 Producer: Done
# Wed Aug 23 14:36:28 2023 > got 0.451356682528389
# Wed Aug 23 14:36:28 2023 Producer: Done
# Wed Aug 23 14:36:29 2023 > got 0.7294317832224353
# Wed Aug 23 14:36:29 2023 Producer: Done
# Wed Aug 23 14:36:29 2023 > got 0.021341817034450816
# Wed Aug 23 14:36:29 2023 > got 0.8146314286214009