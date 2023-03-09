from typing import Union, Sequence
from functools import lru_cache

#
def car_paths(n: int, m: int) -> list[list[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """
    list_ = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    #list_ = [[0]*5]*5


    @lru_cache()
    def lazy_method(n, m):

        if n == 0 and m == 0:
            list_[m][n] = 1
            return 1
        if n < 0 or m < 0:
            return 0

        list_[m][n] = lazy_method(n, m-1) + lazy_method(n-1, m) + lazy_method(n-1, m-1)

        return list_[m][n]
      # TODO решить задачу с помощью динамического программирования
    lazy_method(n - 1, m - 1)
    print("лист рекурсивный ")
    print(list_[0])
    print(list_[1])
    print(list_[2])
    print(list_[3])
    print(list_[4])

    def iterat(n, m):
        list_[0][0] = 1

        for x in range(1, n+1):
            list_[x][0] = 1

        for y in range(1, m+1):
            list_[0][y] = 1

        for y in range(1, m+1):
            for n in range(1, n+1):
                list_[n][y] = list_[n-1][y] + list_[n][y-1] + list_[n-1][y-1]
        print("лист итеративный ")
        print(list_[0])
        print(list_[1])
        print(list_[2])
        print(list_[3])
        print(list_[4])
    iterat(n-1, m-1)
    return list_

if __name__ == '__main__':
    n = 5
    m = 3
    paths = car_paths(n, m)
    print("paths", paths)
    print(paths[n-1][m-1])  # 7


