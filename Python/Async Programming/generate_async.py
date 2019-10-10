import asyncio
import time
import random
import datetime
import colorama

def main():
    
    loop = asyncio.get_event_loop()
    data = asyncio.Queue()

    task1 = loop.create_task(generate_data(10, data))
    task2 = loop.create_task(process_data(10, data))

    full_task = asyncio.gather(task1, task2)

    t_start = time.time()
    loop.run_until_complete(full_task)
    t_end = time.time()
    print("")
    print(colorama.Fore.CYAN + "Total processing time: ", t_end - t_start, "seconds.")
    
async def generate_data(i: int, data: asyncio.Queue):
    '''
    generate random amounts of dummy data.
    returns the generated data as list.
    '''

    t_start = time.time()
    print("")
    print(colorama.Fore.YELLOW + "start data generation at", datetime.datetime.now())

    for n in range(i + 1):
        item = [x for x in range(random.randint(5,30))]
        await data.put(item)
        print(colorama.Fore.WHITE + "generating data set", n, "of", i)
        await asyncio.sleep(random.randint(2,4))

    t_end = time.time()
    print("")
    print(colorama.Fore.YELLOW + "data generation finished in", t_end - t_start, "seconds.")

async def process_data(num: int, data: asyncio.Queue):
    '''
    process the data passed as argument.
    '''

    t_start = time.time()
    processed = 0
    print("")
    print(colorama.Fore.YELLOW + "start data processing at", datetime.datetime.now())

    while processed <= num:
        item = await data.get()
        print(colorama.Fore.WHITE + "processing item", processed, "of", num, ":", item)
        processed += 1
        await asyncio.sleep(random.randint(3,8))

    t_end = time.time()
    print("")
    print(colorama.Fore.YELLOW + "data processing finished in", t_end - t_start, "seconds.")

main()
