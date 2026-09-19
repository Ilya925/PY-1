import asyncio
import time


async def f1(n):
    print(n ** 2)
    print(allways)
    await asyncio.sleep(3)
    print('f1 completed')


async def f2(n):
    print(n * 2)
    await asyncio.sleep(2)
    print('f2 completed')
    print(allways)


async def main():
    # task1 = asyncio.create_task(f1(5))
    # task2 = asyncio.create_task(f2(50))
    # await task1
    # await task2
    await asyncio.gather(f1(5), f2(50))


if __name__ == '__main__':
    allways = 1209
    start = time.time()
    asyncio.run(main())
    stop = time.time()
    duration = round(stop - start, 2)
    print(duration)
