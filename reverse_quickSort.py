import matplotlib.pyplot as plt
import math

def logariphm(x):
    return x * math.log2(x)

def get_graph():
    fig = plt.figure(figsize=(25, 25))
    plt.title("Обратнотсортированный вектор QuickSort")
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [6996, 15974, 25928, 35928, 46834, 57834, 68834, 79834, 91644, 103644, 292262, 634496, 1368962],
        color="green",
        linestyle="--",
        label="Кол-во сравнений для QuickSort",
    )
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [3030, 6066, 10428, 12138, 16356, 20856, 22782, 24282, 28212, 32712, 86646, 173298, 346602],
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