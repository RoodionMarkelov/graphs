import matplotlib.pyplot as plt

def square(x):
    return x**2;

def get_graph():
    fig = plt.figure(figsize=(25, 25))
    plt.title("Обратнотсортированный вектор InsertionSort")
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [504499, 2000999, 4501499, 8001999, 12502499, 18002999, 24503499, 32003999, 40504499, 50004999,
         312512499, 1250024999, 5000049999],
        color="green",
        linestyle="--",
        label="Кол-во сравнений для insertionSort",
    )
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [501498, 2002998, 4504498, 8005998, 12507498, 18008998, 24510498, 32011998, 40513498, 50014998, 312537498,
         1250074998, 5000149998],
        color="blue",
        linestyle="--",
        label="Кол-во копий для insertionSort",
    )
    list_x = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000]
    list_y = list(map(square, list_x))
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