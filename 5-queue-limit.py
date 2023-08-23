from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue, id):
    print(f'{time.ctime()} Producer: Running')
     # generate work
    for i in range(10):
         # generate a value
        value = random() 
        # block to simulate work
        await asyncio.sleep((id+1)*0.1)
        # add to the queue, may block  
        await queue.put(value)  
    print(f'{time.ctime()} Producer: {id} Done')

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
    producers = [producer(queue, i) for i in range(5)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for the consumer to process all items
    await queue.join()

# start the asyncio program
asyncio.run(main())


# Wed Aug 23 15:23:53 2023 Consumer: Running
# Wed Aug 23 15:23:53 2023 Producer: Running
# Wed Aug 23 15:23:53 2023 Producer: Running
# Wed Aug 23 15:23:53 2023 Producer: Running
# Wed Aug 23 15:23:53 2023 Producer: Running
# Wed Aug 23 15:23:53 2023 Producer: Running
# Wed Aug 23 15:23:53 2023 > got 0.23885691904488793
# Wed Aug 23 15:23:53 2023 > got 0.9197181450407855
# Wed Aug 23 15:23:54 2023 > got 0.20561064270856855
# Wed Aug 23 15:23:54 2023 > got 0.9937910443464992
# Wed Aug 23 15:23:55 2023 > got 0.7405666191097121
# Wed Aug 23 15:23:56 2023 > got 0.2769831419677977
# Wed Aug 23 15:23:56 2023 > got 0.82699137669081
# Wed Aug 23 15:23:57 2023 > got 0.341122582045136
# Wed Aug 23 15:23:58 2023 > got 0.24743165072791484
# Wed Aug 23 15:23:58 2023 > got 0.41660120340204077
# Wed Aug 23 15:23:58 2023 > got 0.02664788726119849
# Wed Aug 23 15:23:58 2023 > got 0.9693680237229896
# Wed Aug 23 15:23:59 2023 > got 0.9224007616001597
# Wed Aug 23 15:24:00 2023 > got 0.5565253837807835
# Wed Aug 23 15:24:01 2023 > got 0.35732423499581634
# Wed Aug 23 15:24:01 2023 > got 0.13787292891503466
# Wed Aug 23 15:24:01 2023 > got 0.9338720125272473
# Wed Aug 23 15:24:02 2023 > got 0.6133846432735108
# Wed Aug 23 15:24:03 2023 > got 0.29804269901280855
# Wed Aug 23 15:24:03 2023 > got 0.8355570856842138
# Wed Aug 23 15:24:04 2023 > got 0.6261761583737843
# Wed Aug 23 15:24:05 2023 > got 0.4085878526070782
# Wed Aug 23 15:24:05 2023 > got 0.8009423180926996
# Wed Aug 23 15:24:06 2023 > got 0.11406537183624876
# Wed Aug 23 15:24:06 2023 > got 0.5385751226095273
# Wed Aug 23 15:24:07 2023 > got 0.011255514235383624
# Wed Aug 23 15:24:07 2023 > got 0.7572827794343573
# Wed Aug 23 15:24:07 2023 > got 0.9614033048098737
# Wed Aug 23 15:24:08 2023 > got 0.3334234611704876
# Wed Aug 23 15:24:09 2023 > got 0.18329671351932908
# Wed Aug 23 15:24:09 2023 > got 0.38314143484997465
# Wed Aug 23 15:24:09 2023 > got 0.5290345644080848
# Wed Aug 23 15:24:10 2023 > got 0.6966545157603804
# Wed Aug 23 15:24:10 2023 > got 0.7750444765008176
# Wed Aug 23 15:24:11 2023 > got 0.11685252444432692
# Wed Aug 23 15:24:11 2023 > got 0.3402252290080441
# Wed Aug 23 15:24:12 2023 > got 0.2611733199783147
# Wed Aug 23 15:24:12 2023 > got 0.9350051985122397
# Wed Aug 23 15:24:12 2023 Producer: 0 Done
# Wed Aug 23 15:24:13 2023 > got 0.4713663957284996
# Wed Aug 23 15:24:13 2023 > got 0.06691488760435405
# Wed Aug 23 15:24:13 2023 > got 0.41242040761797305
# Wed Aug 23 15:24:14 2023 > got 0.024314134243672347
# Wed Aug 23 15:24:14 2023 > got 0.6775930136154381
# Wed Aug 23 15:24:14 2023 Producer: 1 Done
# Wed Aug 23 15:24:15 2023 > got 0.25292044718917883
# Wed Aug 23 15:24:15 2023 Producer: 2 Done
# Wed Aug 23 15:24:15 2023 > got 0.5176127143977243
# Wed Aug 23 15:24:15 2023 > got 0.44619721393500456
# Wed Aug 23 15:24:16 2023 > got 0.9501795363312798
# Wed Aug 23 15:24:16 2023 Producer: 3 Done
# Wed Aug 23 15:24:17 2023 > got 0.09945398592643317
# Wed Aug 23 15:24:17 2023 Producer: 4 Done
# Wed Aug 23 15:24:17 2023 > got 0.5040647367082325
# Wed Aug 23 15:24:17 2023 > got 0.056202513311937596