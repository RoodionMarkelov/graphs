import matplotlib.pyplot as plt
import math

def logariphm(x):
    return x * math.log2(x)

def get_graph():
    fig = plt.figure(figsize=(25, 25))
    plt.title("Сортированный вектор QuickSort")
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [7987, 17964, 28917, 39917, 51822, 63822, 75822, 87822, 100631, 113631, 317248, 684481, 1468946],
        color="green",
        linestyle="--",
        label="Кол-во сравнений для QuickSort",
    )
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [1533, 3096, 5928, 6141, 8856, 11856, 12285, 12285, 14712, 17712, 49149, 98301, 196605],
        color="blue",
        linestyle="--",
        label="Кол-во копий для QuickSort",
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