import asyncio
import time
import random
import datetime
import colorama

def main():
    data, t_generating = generate_data(10)
    t_processing = process_data(data)
    print("")
    print(colorama.Fore.CYAN + "Total processing time {}".format(t_generating + t_processing))

def generate_data(i: int):
    '''
    generate random amounts of dummy data.
    returns: 1) the generated data as list 2) the total processing time needed by this function.
    '''

    t_start = time.time()
    data = []
    print("")
    print(colorama.Fore.YELLOW + "start data generation at", datetime.datetime.now())

    for n in range(i + 1):
        item = [x for x in range(random.randint(5,30))]
        data.append(item)
        print(colorama.Fore.WHITE + "generating data set", n, "of", i)
        time.sleep(random.randint(2,4))

    t_end = time.time()
    print("")
    print(colorama.Fore.YELLOW + "data generation finished in", t_end - t_start, "seconds.")

    return data, t_end - t_start

def process_data(data: list) -> float:
    '''
    process the data passed as argument.
    returns the total processing time of this function.
    '''

    t_start = time.time()
    print("")
    print(colorama.Fore.YELLOW + "start data processing at", datetime.datetime.now())

    for item in data:
        print(colorama.Fore.WHITE, item)
        time.sleep(random.randint(3,8))

    t_end = time.time()
    print("")
    print(colorama.Fore.YELLOW + "data processing finished in", t_end - t_start, "seconds.")

    return t_end - t_start

main()
