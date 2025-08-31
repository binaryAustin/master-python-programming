import multiprocessing as mp
import time


def deposit(balance_param, lock_param):
    for _ in range(100):
        time.sleep(0.01)
        lock_param.acquire()
        balance_param.value += 1
        lock_param.release()


def withdraw(balance_param, lock_param):
    for _ in range(100):
        time.sleep(0.01)
        lock_param.acquire()
        balance_param.value -= 1
        lock_param.release()


if __name__ == "__main__":
    balance = mp.Value("f", 500.0)

    lock = mp.Lock()

    p1 = mp.Process(target=deposit, args=(balance, lock))
    p2 = mp.Process(target=withdraw, args=(balance, lock))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(f"Balance: {balance.value}")
