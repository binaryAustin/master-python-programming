import multiprocessing as mp


def squares(numbers_param, squares_list_param):
    for n in numbers_param:
        squares_list_param.append(n**2)
    print(f"square_list inside process {squares_list_param}")


def cubes(numbers_param, result_param):
    i = 0
    for num in numbers_param:
        result_param[i] = num**3
        i += 1

    print(f"Result array inside process/function: {result_param[::]}")


if __name__ == "__main__":
    numbers = [1, 2, 3]
    squares_list = []

    p = mp.Process(target=squares, args=(numbers, squares_list))
    p.start()
    p.join()

    print(f"squares_list outside process: {squares_list}")

    result = mp.Array("i", len(numbers))

    p1 = mp.Process(target=cubes, args=(numbers, result))
    p1.start()
    p1.join()
    print(f"Result array outside process: {result[::]}")
