import multiprocessing as mp
import time
from typing import List


def name_and_time(name: str):
    print(f"Hello {name}, current time: {time.time()}")
    print("😪 Sleeping for 2 seconds...")
    time.sleep(2.0)
    print("After sleeping...Exiting function")


if __name__ == "__main__":
    # These are forked processes
    processes: List[mp.Process] = []

    for i in range(10):
        process = mp.Process(target=name_and_time, args=("Austin",))
        processes.append(process)

    for p in processes:
        p.start()

    # Make the main process wait for all forked processes to finish
    for p in processes:
        p.join()

    # Without making the process wait, this code is executed even if forked processes haven't finished yet
    print("Other instructions of the main module...")
    print("End of script")
