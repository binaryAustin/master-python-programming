import threading
import time
from typing import List


def name_and_time(name: str):
    print(f"Hello {name}, current time: {time.time()}")
    print("😪 Sleeping for 2 seconds...")
    time.sleep(2.0)
    print("After sleeping...Exiting function")


if __name__ == "__main__":
    # These are forked threads
    threads: List[threading.Thread] = []

    for i in range(10):
        thread = threading.Thread(target=name_and_time, args=("Austin",))
        threads.append(thread)

    for th in threads:
        th.start()

    # Make the main process wait for all forked threads to finish
    for th in threads:
        th.join()

    # Without making the process wait, this code is executed even if forked threads haven't finished yet
    print("Other instructions of the main module...")
    print("End of script")
