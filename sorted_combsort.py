import matplotlib.pyplot as plt
import math

def logariphm(x):
    return x * math.log2(x)

def get_graph():
    fig = plt.figure(figsize=(25, 25))
    plt.title("Сортированный вектор CombSort")
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [19499, 44846, 73236, 101638, 132021, 158417, 191798, 227193, 255601, 293976, 809841, 1769601, 3839091],
        color="green",
        linestyle="--",
        label="Кол-во сравнений для CombSort",
    )
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        color="blue",
        linestyle="--",
        label="Кол-во копий для CombSort",
    )
    list_x = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000]
    list_y = list(map(logariphm, list_x))
    plt.plot(
        list_x,
        list_y,
        color="red",
        linestyle="--",
        label="Теория",
    )
    plt.xlabel("длина массива")
    plt.ylabel("кол-во")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    get_graph()