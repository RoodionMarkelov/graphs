import matplotlib.pyplot as plt

def square(x):
    return x**2;

def get_graph():
    fig = plt.figure(figsize=(25, 25))
    plt.title("Рандомный вектор InsertionSort")
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [245591, 997858, 2273335, 4081581, 6310790, 9048252, 12332917, 16099177, 20384159, 25156706, 157016168,
         626390621, 2507195226],
        color="green",
        linestyle="--",
        label="Кол-во сравнений для insertionSort",
    )
    plt.plot(
        [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 25000, 50000, 100000],
        [246590, 999857, 2276334, 4085580, 6315789, 9054251, 12339916, 16107176, 20393158, 25166705, 157041167,
         626440620, 2507295225],

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