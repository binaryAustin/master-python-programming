import multiprocessing as mp


counter = mp.Value("i", 1)

# counter = 1


def increment(c):
    # global counter
    c.value += 1


if __name__ == "__main__":
    for i in range(10):
        process = mp.Process(target=increment, args=(counter,))
        process.start()
        process.join()

    print(counter.value)
