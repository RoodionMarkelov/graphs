import matplotlib.pyplot as plt

def get_graph():
    fig = plt.figure(figsize=(25, 25))
    plt.title("Сортированный вектор InsertionSort")
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [999, 1998, 2999, 3999, 4999, 5999, 6999, 7999, 8999, 9999, 24999, 49999, 99999],
        color="green",
        linestyle="--",
        label="Кол-во сравнений для insertionSort",
    )
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [1998, 3998, 5998, 7998, 9998, 11998, 13998, 15998, 17998, 19998, 49998, 99998, 199998],
        color="blue",
        linestyle="--",
        label="Кол-во копий для insertionSort",
    )
    list_x = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000]
    plt.plot(
        list_x,
        list_x,
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