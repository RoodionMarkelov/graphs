import matplotlib.pyplot as plt
import math

def logariphm(x):
    return x * math.log2(x)

def get_graph():
    fig = plt.figure(figsize=(40, 40))
    plt.title("Рандомный вектор QuickSort")
    plt.plot(
    [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [6690, 17572, 26970, 35570, 47774, 58744, 70899, 89484, 97485, 109402, 272307, 594433, 1232776],
        label="Кол-во сравнений для quickSort",
        color="green",
        linestyle="--",
    )
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [7866, 17001, 26628, 37041, 46854, 57903, 68379, 79395, 89274, 101487, 282102, 606543, 1312515],
        label="Кол-во копий для quickSort",
        color="blue",
        linestyle="--",
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
    plt.legend(loc=1, prop={"size": 5})
    plt.xlabel("длина массива")
    plt.ylabel("кол-во")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    get_graph()